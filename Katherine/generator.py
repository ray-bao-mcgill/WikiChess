import wikipediaapi
import random

def get_wikipedia_page(word):
    wiki_wiki = wikipediaapi.Wikipedia('User-Agent: wiki-chess/0.1 (613-298-7995);')
    page = wiki_wiki.page(word)
    return page if page.exists() else None

def generate_genres_and_words(genres):

    genre_words = {
    
    "animals": [
        "Walrus", "Spider", "Squid", "Frog", "Pig", "Sheep", "Crab", "Koala",
        "Butterfly", "Parrot", "Hawk", "Beetle", "Lion", "Tiger", "Zebra",
        "Seahorse", "Chicken", "Cow", "Starfish", "Shrimp", "Giraffe", "Whale",
        "Eagle", "Platypus", "Rat", "Wolf", "Turtle", "Mouse", "Lobster",
        "Kangaroo", "Horse", "Octopus", "Goat", "Dolphin", "Squirrel", "Jellyfish",
        "Seal", "Shark", "Elephant", "Deer", "Ant", "Albatross", "Owl",
        "Pelican", "Rabbit", "Fox", "Bat", "Snake", "Bear", "Duck", "Penguin","Lizard"
    ],

    "sports": [
        "Skiing", "Taekwondo", "Surfing", "Baseball", "Kayaking", "Canoeing",
        "Rugby", "Skateboarding", "Snooker", "Gymnastics", "Sailing", "Badminton",
        "Bowling", "Judo", "Shooting", "Wrestling", "Darts", "Basketball",
        "Hockey", "Swimming", "Karate", "Row", "MMA", "Climbing", "Speedway",
        "Equestrian", "Soccer", "Fishing", "Motorcycling", "Triathlon", "Tennis",
        "Diving", "Archery", "Tabletennis", "Hiking", "BMX", "Hunting", "Cycling",
        "Marathon", "Boxing", "Pingpong", "Pool", "Rally", "Cricket", "Track",
        "Field", "Fencing", "Snowboarding", "Volleyball", "Golf"
    ],

    "foods": [
        "Macaron", "Burger", "Pizza", "Bread", "Waffle",
        "Cake", "Sorbet", "Cookie", "Noodle", "Gelato", "Juice", "Soup",
        "Casserole", "Curry", "Quiche", "Salad", "Tiramisu", "Mousse", "Sushi",
        "Grilled", "Omelette", "Pie", "Chocolate", "Dumpling", "Roast", 
        "Pudding", "Stew", "Coffee", "Croissant", "Sashimi", "Cheese", "Pancake",
        "Sandwich", "Donut", "Muffin", "Bagel", "Smoothie", "Brownie", "Samosa",
        "Tacos", "Crepe", "Yogurt", "Baked", "Pasta", "Tea"
    ],

    "professions": [
        "Writer", "Strategist", "Economist", "Producer", "Poet", "Psychologist",
        "Scientist", "Biologist", "Composer", "Librarian", "Doctor", "Politician",
        "Architect", "Artist", "Researcher", "Philosopher", "Chef", "Teacher",
        "Businessman", "Actor", "Filmmaker", "Leader", "Inventor", "Entrepreneur",
        "Dancer", "Journalist", "Nurse", "Mathematician", "Explorer", "Pilot",
        "Athlete", "Engineer", "Musician", "Novelist", "Chemist", "Historian",
        "Scholar", "Lawyer", "Director", "Author", "Painter", "Philanthropist","Activist"
    ],

       
    "sciences": [
        "Climatology", "Herpetofauna", "Paleobotany", "Biomechatronics", "Paleontology",
        "Psychology", "Microbiology", "Cosmology", "Herpetology", "Algology",
        "Ecotoxicology", "Astronomy", "Anthropology", "Archaeology", "Nanotechnology",
        "Chemistry", "Geochemistry", "Sociology", "Acoustics", "Malacology",
        "Bionanotechnology", "Entomology", "Electromagnetism", "Virology",
        "Astrophysics", "Optics", "Paleoclimatology", "Taphonomy", "Immunology",
        "Botany", "Ecology", "Ichthyology", "Mammalogy", "Volcanology", "Biochemistry",
        "Genetics", "Relativity", "Geophysics", "Bacteriology", "Parasitology",
        "Biomimetics", "Mechanics", "Biophysics", "Neuroscience", "Thermodynamics",
        "Superconductivity", "Biology", "Oceanography", "Biotechnology", "Bioinformatics",
        "Astrobiology", "Ornithology", "Toxicology", "Hydrology", "Zoology", "Geology",
        "Meteorology", "Protozoology", "Biomaterials", "Astrochemistry", "Seismology",
        "Ecophysiology", "Criminology", "Nanoscience", "Geobiology", "Phycology",
        "Biomechanics", "Biogeochemistry", "Bioelectronics", "Pharmacology", "Mycology",
        "Exoplanets", "Materials", "Physics", "Mathematics", "Statistics", "Computer",    
    ],
    "countries": [
        "Kenya", "Turkey", "Germany", "Colombia", "Thailand", "Peru", 
        "USA", "Sweden", "Finland", "Nigeria", "Iraq", "Indonesia", "Uzbekistan",
        "Laos", "Australia", "SriLanka", "France", "Georgia", "Syria", "Turkmenistan",
        "Switzerland", "Russia", "Malaysia", "Austria", "Myanmar", "Pakistan",
        "Bangladesh", "Singapore", "India", "Belgium", "Morocco", "China", "Japan",
        "NewZealand", "Lebanon", "Nepal", "Philippines", "Iran", "Azerbaijan",
        "Kazakhstan", "Venezuela", "Norway", "Yemen","Armenia",
        "Tajikistan", "Mongolia", "Egypt", "Italy", "Jordan", "Chile", "Mexico",
        "Portugal", "Brazil", "Denmark", "Bhutan", "Israel",
        "Argentina", "Vietnam", "Spain", "Kyrgyzstan", "Afghanistan", "Oman",
        "Canada", "Cambodia", "Netherlands", "Qatar", "Palestine", "Brunei"
    ]


    }

    playing_genre = random.choice(genres)
    words = genre_words.get(playing_genre, [])

     # Check if there are at least 2 words to sample from
    if len(words) < 2:
        raise ValueError(f"Not enough words for the genre '{playing_genre}'")

    starting_genre = random.choice([genre for genre in genres if genre != playing_genre])
    starting_word = random.choice(genre_words.get(starting_genre, []))

    # Ensure there are enough words to sample
    if len(words) < 2:
        raise ValueError(f"Not enough words to sample from '{playing_genre}'")
    
    word1, word2 = random.sample(words, 2)

    return playing_genre, starting_word, word1, word2

    # playing_genre = random.choice(genres)

    # remaining_genres = [genre for genre in genres if genre != playing_genre]
    # starting_genre = random.choice(remaining_genres)

    # words = generate_genres_and_words.get(playing_genre, [])
    
    # word1, word2 = random.sample(words, 2)

    # return  playing_genre, starting_genre, word1, word2


# test 

playing_genre, starting_genre, word1, word2 = generate_genres_and_words(["animals", "sports", "foods", "professions", "sciences", "countries"])
print(f"Category: {playing_genre}")
print(f"Starting word: {starting_genre}")
print(f"Words: {word1}, {word2}")







# valid words exist in the wikipedia database
#     valid_words = set()

#     # Iterate through all genres
#     for genre in genres:
#         words = genre_words.get(genre, [])

#         for word in words:
#             page = get_wikipedia_page(word)
#             if page:
#                 valid_words.add(word)

#     return valid_words

# def save_valid_words(valid_words, filename):
#     with open(filename, 'w') as file:
#         for word in valid_words:
#             file.write(f"{word}\n")

# if __name__ == "__main__":
#     genres = ["animals", "sports", "foods", "professions", "sciences", "countries"]
#     valid_words = generate_words(genres)
#     save_valid_words(valid_words, "valid_words.txt")