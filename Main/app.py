from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase
import requests
from bs4 import BeautifulSoup
import localGame as lg
from generator import generate_genres_and_words
import datetime
app = Flask(__name__)
app.config["SECRET_KEY"] = "secretKey"
socketio = SocketIO(app)

rooms = {}

game = lg.LocalGame()


# Function to scrape the Wikipedia page for its HTML content and remove language elements
def scrape_wikipedia_page(url):
    response = requests.get(url)
    if response.status_code == 200: # if successful 
        soup = BeautifulSoup(response.text, 'html.parser') #parse html content of the page 

        # Remove the sidebar with languages
        if soup.find(id="p-lang"):
            soup.find(id="p-lang").decompose()

        # Remove any other language links
        for lang_link in soup.select('li.interlanguage-link'):
            lang_link.decompose()

        # Extract the main content of the Wikipedia page
        content = soup.find(id="mw-content-text") #via id 
        return str(content) #cleaned up html content of wiki page w/out lang elements 
    else:
        return "<p>Error: Unable to fetch the page.</p>"


def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break
    
    return code

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/local")
def local():
    playing_genre,starting_genre, word1, word2 = generate_genres_and_words(["animals", "sports", "foods", "professions", "sciences", "countries"])
    game.set_target1(word1)
    game.set_target2(word2)
    return render_template("local.html", word1=word1, word2=word2, genre1 = starting_genre, genre2 = playing_genre)

@app.route("/online", methods=["POST", "GET"])
def online():   
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("online.html", error="Please enter a name.", code=code, name=name)

        if join != False and not code:
            return render_template("online.html", error="Please enter a room code.", code=code, name=name)
        
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("online.html", error="Room does not exist.", code=code, name=name)
        
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))

    return render_template("online.html")

@app.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("online"))

    return render_template("room.html", code=room, messages=rooms[room]["messages"])

@app.route("/localGame", methods=['GET', 'POST'])
def localGame():

    playing_genre, starting_word, word1, word2 = generate_genres_and_words(["animals", "sports", "foods", "professions", "sciences", "countries"])
    starting_url = "https://en.wikipedia.org/wiki/" + starting_word

    html_content = scrape_wikipedia_page(starting_url)
    
    return render_template('localGame.html', html_content=html_content, 
                           moves1=game.get_past_moves1(), 
                           moves2=game.get_past_moves2(),
                           scores1=game.get_past_scores1(),
                           scores2=game.get_past_scores2(),
                           starting_genre=starting_word)


@app.route('/switchTurn', methods=['GET', 'POST'])
def switchTurn():
        previous_player = game.getTurn()
        game.switchTurn()
        if previous_player == "White":
            return render_template('torreyBlackTurn.html', url = "/wiki/"+game.get_past_moves1()[-1])
        elif previous_player == "Black":
            return render_template('torreyWhiteTurn.html', url = "/wiki/"+game.get_past_moves2()[-1])

@app.route('/<path:path>')
def catch_all(path):
    print(path)
    if path:
        word = path.split('/')[1]
    if word:
        check = ('').join(word.split('_'))
    else:
        check = ""
    if check.lower() == game.get_target1().lower():
        game.add_past_move1("REACHED")
        # return render_template('winscreen' player=player1)
    elif check.lower() == game.get_target2().lower():
        game.add_past_move2("REACHED")

    if game.getTurn() == "White":
        l = game.get_past_moves1()
        if len(l) > 0:
            if l[-1] == word:
                game.add_past_move1(word)
                game.add_past_score1(100)
        else:
            game.add_past_move1(word)
            game.add_past_score1(100)
    else:
        l = game.get_past_moves2()
        if len(l) > 0:
            if l[-1] == word:
                game.add_past_move2(word)
                game.add_past_score2(100)
        game.add_past_move2(word)
        game.add_past_score2(100)
    return render_template('localGame.html', 
                           html_content=scrape_wikipedia_page("https://en.wikipedia.org/" + path), 
                           moves1=game.get_past_moves1(), 
                           moves2=game.get_past_moves2(),
                           scores1=game.get_past_scores1(),
                           scores2=game.get_past_scores2(),
    )



@socketio.on("asdf")
def asdf(data):
    room = session.get("room")
    if room not in rooms:
        return
    content = {
        "name": "fixed",
        "message": "hello world"
    }
    send(content, t =room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return 
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")

if __name__ == "__main__":
    socketio.run(app, debug=True)