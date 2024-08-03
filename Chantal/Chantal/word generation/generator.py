import wikipediaapi
import random

def get_wikipedia_page(word):
    wiki_wiki = wikipediaapi.Wikipedia('User-Agent: wiki-chess/0.1 (613-298-7995);')
    page = wiki_wiki.page(word)
    return page if page.exists() else None

def generate_genres_and_words(genres):
    genre_words = {
    
       "animals": [
            "walrus", "spider", "squid", "frog", "pig", "sheep", "crab", "koala",
            "butterfly", "parrot", "hawk", "beetle", "lion", "tiger", "zebra",
            "seahorse", "chicken", "cow", "starfish", "shrimp", "giraffe", "whale",
            "eagle", "platypus", "rat", "wolf", "turtle", "mouse", "lobster",
            "kangaroo", "horse", "octopus", "goat", "dolphin", "squirrel", "jellyfish",
            "seal", "shark", "elephant", "deer", "ant", "albatross", "owl",
            "pelican", "rabbit", "fox", "bat", "snake", "bear", "duck", "penguin",
            "lizard"
        ],
       "sports": [
            "skiing", "taekwondo", "surfing", "baseball", "kayaking", "canoeing",
            "rugby", "skateboarding", "snooker", "gymnastics", "sailing", "badminton",
            "bowling", "judo", "shooting", "wrestling", "darts", "basketball",
            "hockey", "swimming", "karate", "row", "mma", "climbing", "speedway",
            "equestrian", "soccer", "fishing", "motorcycling", "triathlon", "tennis",
            "diving", "archery", "tabletennis", "hiking", "bmx", "hunting", "cycling",
            "marathon", "boxing", "pingpong", "pool", "rally", "cricket", "track",
            "field", "fencing", "snowboarding", "volleyball", "golf"
        ],
        
        "foods": [
            "Macaron", "Burger", "Pizza", "Fried", "Bread", "Waffle",
            "Cake", "Sorbet", "Cookie", "Noodle", "Gelato", "Juice", "Soup",
            "Casserole", "Curry", "Quiche", "Salad", "Tiramisu", "Mousse", "Sushi",
            "Grilled", "Omelette", "Pie", "Chocolate", "Dumpling", "Roast", 
            "Pudding", "Stew", "Coffee", "Croissant", "Sashimi", "Cheese", "Pancake",
            "Sandwich", "Donut", "Muffin", "Bagel", "Smoothie", "Brownie", "Samosa",
            "Tacos", "Crepe", "Yogurt", "Baked", "Pasta", "Tea"
        ],

        "professions": [
            "writer", "strategist", "economist", "producer", "poet", "psychologist",
            "scientist", "biologist", "composer", "librarian", "doctor", "politician",
            "architect", "artist", "researcher", "philosopher", "chef", "teacher",
            "businessman", "actor", "filmmaker", "leader", "inventor", "entrepreneur",
            "dancer", "journalist", "nurse", "mathematician", "explorer", "pilot",
            "athlete", "engineer", "musician", "novelist", "chemist", "historian",
            "scholar", "lawyer", "director", "author", "painter", "philanthropist",
            "activist"
        ],

       "sciences": [
            "climatology", "herpetofauna", "paleobotany", "biomechatronics", "paleontology",
            "psychology", "microbiology", "cosmology", "herpetology", "algology",
            "ecotoxicology", "astronomy", "anthropology", "archaeology", "nanotechnology",
            "chemistry", "geochemistry", "sociology", "acoustics", "malacology",
            "bionanotechnology", "entomology", "electromagnetism", "virology",
            "astrophysics", "optics", "paleoclimatology", "taphonomy", "immunology",
            "botany", "ecology", "ichthyology", "mammalogy", "volcanology", "biochemistry",
            "genetics", "relativity", "geophysics", "bacteriology", "parasitology",
            "biomimetics", "mechanics", "biophysics", "neuroscience", "thermodynamics",
            "superconductivity", "biology", "oceanography", "biotechnology", "bioinformatics",
            "astrobiology", "ornithology", "toxicology", "hydrology", "zoology", "geology",
            "meteorology", "protozoology", "biomaterials", "astrochemistry", "seismology",
            "ecophysiology", "criminology", "nanoscience", "geobiology", "phycology",
            "biomechanics", "biogeochemistry", "bioelectronics", "pharmacology", "mycology",
            "exoplanets", "materials", "physics"
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

    starting_genre = random.choice([genre for genre in genres if genre != playing_genre])
    
    word1, word2 = random.sample(words, 2)

    return playing_genre, starting_genre, word1, word2

    # playing_genre = random.choice(genres)

    # remaining_genres = [genre for genre in genres if genre != playing_genre]
    # starting_genre = random.choice(remaining_genres)

    # words = generate_genres_and_words.get(playing_genre, [])
    
    # word1, word2 = random.sample(words, 2)

    # return  playing_genre, starting_genre, word1, word2


# test 

playing_genre, starting_genre, word1, word2 = generate_genres_and_words(["animals", "sports", "foods", "professions", "sciences", "countries"])
print(f"Category: {playing_genre}")
print(f"Starting category: {starting_genre}")
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