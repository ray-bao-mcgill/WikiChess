import wikipediaapi
import random

def get_wikipedia_page(word):
    wiki_wiki = wikipediaapi.Wikipedia('User-Agent: wiki-chess/0.1 (613-298-7995);')
    page = wiki_wiki.page(word)
    return page if page.exists() else None

def generate_words(genres):
    # A sample dictionary with some single-word terms related to specific genres
    genre_words = {
    "technology": [
        "robotics", "cybernetics", "blockchain", "nanotechnology", "AI", "automation",
        "biotechnology", "cloud", "cryptography", "data", "deepfake", "digital", "drones",
        "encryption", "fiberoptics", "hardware", "hyperloop", "infotech", "internet",
        "IoT", "machinelearning", "microprocessor", "neuralnetwork", "optics", "quantum",
        "sensors", "software", "telecommunications", "virtualreality", "augmentedreality",
        "bionics", "quantumcomputing", "genomics", "biometrics", "wearable", "nanorobotics",
        "smartphones", "webdevelopment", "artificialintelligence", "cybersecurity", 
        "blockchain", "cryptocurrency", "bigdata", "datamining", "cloudcomputing", 
        "distributedcomputing", "informationsecurity", "5G", "internetofthings", "VR", "AR",
        "biocomputing", "bioinformatics", "haptics", "nanomaterials", "photovoltaics", 
        "semiconductors", "speechrecognition", "computervision", "naturalprocessing", 
        "computational", "embedded", "microelectronics", "nanofabrication", "optomechanics",
        "selfdriving", "telemedicine", "telepresence", "3Dprinting", "cyborg", "smartgrid",
        "bioengineering", "cloudstorage", "edgecomputing", "neuromorphic", "quantumcryptography",
        "spacetechnology", "syntheticbiology", "wearabletechnology", "wirelesscharging", 
        "drone", "exoskeleton", "smartwatch", "braincomputer", "internetsecurity", 
        "nanotechnology", "roboticsprocess", "biohacking", "selflearning", "digitalcurrency",
        "computing", "augmentedreality", "hydrogenfuel", "virtualassistant", "quantumphysics",
        "5Gnetwork", "cloudinfrastructure", "cyberforensics", "fintech", "greentech"
    ],
    "art": [
        "cubism", "surrealism", "impressionism", "fauvism", "baroque", "abstract", 
        "expressionism", "minimalism", "popart", "futurism", "neoclassicism", "romanticism", 
        "rococo", "realism", "symbolism", "artdeco", "artnouveau", "dadaism", "mannerism", 
        "constructivism", "pointillism", "conceptual", "photorealism", "installation", 
        "streetart", "graffiti", "collage", "sculpture", "tapestry", "printmaking", 
        "mosaic", "fresco", "lithography", "etching", "caricature", "illustration", 
        "calligraphy", "stencil", "graffito", "woodcut", "watercolor", "acrylic", 
        "oilpainting", "pastel", "encaustic", "tempera", "mural", "portraiture", 
        "landscape", "stilllife", "anatomy", "composition", "perspective", "chiaroscuro", 
        "sfumato", "impasto", "underpainting", "varnish", "hatching", "stippling", 
        "tonalism", "fauvism", "orphism", "suprematism", "purism", "deconstructivism", 
        "postmodernism", "outsiderart", "kitsch", "grotesque", "naiveart", "lowbrow", 
        "artbrut", "opart", "stuckism", "hyperrealism", "verism", "narrativeart", 
        "urbanart", "glitchart", "netart", "cyberart", "mediaart", "bioart", 
        "soundart", "lightart", "environmentalart", "landart", "performanceart", 
        "intermedia", "newmedia", "kineticart", "concreteart", "patternpainting", 
        "actionpainting", "videoart", "relationalart", "participatoryart", "newaesthetic"
    ],
    "science": [
        "biology", "chemistry", "physics", "geology", "astronomy", "ecology", 
        "genetics", "biochemistry", "zoology", "botany", "meteorology", "oceanography", 
        "geophysics", "paleontology", "anthropology", "sociology", "psychology", 
        "neuroscience", "microbiology", "immunology", "toxicology", "pharmacology", 
        "biophysics", "biotechnology", "astrobiology", "astrophysics", "quantummechanics", 
        "relativity", "thermodynamics", "optics", "acoustics", "mechanics", "fluiddynamics", 
        "electromagnetism", "quantumfieldtheory", "particlephysics", "nuclearphysics", 
        "condensedmatter", "solidstatephysics", "materials", "nanoscience", "nanotechnology", 
        "computationalphysics", "chaostheory", "complexsystems", "systemsbiology", 
        "syntheticbiology", "bioinformatics", "structuralbiology", "developmentalbiology", 
        "evolutionarybiology", "molecularbiology", "cellbiology", "ecotoxicology", 
        "environmentalscience", "earthscience", "spaceexploration", "planetaryscience", 
        "cosmology", "exoplanets", "quantumcomputing", "stringtheory", "superconductivity", 
        "biogeochemistry", "geochemistry", "astrochemistry", "geobiology", "planetarygeology", 
        "volcanology", "seismology", "hydrology", "climatology", "paleoclimatology", 
        "paleobotany", "archaeology", "forensicscience", "criminology", "environmentalbiology", 
        "ecophysiology", "behavioralbiology", "conservationbiology", "marinebiology", 
        "entomology", "ornithology", "herpetology", "ichthyology", "mammalogy", 
        "parasitology", "virology", "bacteriology", "mycology", "phycology", "protozoology", 
        "algology", "malacology", "herpetofauna", "taphonomy", "biomechanics", 
        "biomedicalengineering", "biomaterials", "bioelectronics", "biomimetics", 
        "bionanotechnology", "biomechatronics"
    ],
    "literature": [
        "novel", "poetry", "drama", "essay", "fiction", "nonfiction", "biography", 
        "autobiography", "shortstory", "fable", "myth", "legend", "folklore", 
        "fairytale", "epic", "narrative", "prose", "verse", "lyric", "ode", 
        "sonnet", "haiku", "ballad", "elegy", "satire", "parody", "tragedy", 
        "comedy", "romance", "mystery", "thriller", "horror", "fantasy", 
        "sciencefiction", "historicalfiction", "magicalrealism", "dystopian", 
        "utopian", "bildungsroman", "picaresque", "epistolary", "allegory", 
        "gothic", "realism", "naturalism", "modernism", "postmodernism", 
        "surrealism", "absurdism", "existentialism", "transcendentalism", 
        "romanticism", "neoclassicism", "classicism", "symbolism", "expressionism", 
        "metafiction", "cyberpunk", "steampunk", "slipstream", "speculativefiction", 
        "adventure", "detectivefiction", "noir", "hardboiled", "pulpfiction", 
        "urbanfantasy", "highfantasy", "lowfantasy", "grimdark", "newweird", 
        "literaryfiction", "streamofconsciousness", "psychologicalfiction", 
        "metaphysicalfiction", "philosophicalfiction", "magicrealism", 
        "postapocalyptic", "apocalyptic", "alternatehistory", "bizarro", 
        "graphicnovel", "comicbook", "manga", "lightnovel", "webfiction", 
        "fanfiction", "slashfiction", "fandom", "litcrit", "literarytheory", 
        "newcriticism", "deconstruction", "poststructuralism", "feministliterature", 
        "queerliterature", "postcolonialliterature", "minorityliterature" "indigenousliterature", "worldliterature", "comparativeliterature", 
        "oralliterature", "oraltradition", "folkliterature", "childrensliterature", 
        "youngadultliterature", "bildungsroman", "nanofiction", "flashfiction"
    ],
    "music": [
        "jazz", "blues", "rock", "classical", "pop", "hiphop", "reggae", 
        "country", "folk", "electronic", "dance", "house", "techno", "trance", 
        "dubstep", "drumandbass", "soul", "funk", "rnb", "disco", "metal", 
        "punk", "grunge", "alternative", "indie", "ska", "bluegrass", 
        "gospel", "opera", "baroque", "renaissance", "romantic", "chambermusic", 
        "symphony", "concerto", "sonata", "cantata", "oratorio", "ballet", 
        "minuet", "waltz", "swing", "bebop", "cooljazz", "hardbop", "fusion", 
        "avantgarde", "newage", "ambient", "industrial", "noise", "psychedelic", 
        "shoegaze", "dreampop", "lofi", "triphop", "downtempo", "trap", 
        "crunk", "bounce", "emo", "posthardcore", "screamo", "postpunk", 
        "newwave", "synthpop", "electropop", "futurepop", "retro", "vaporwave", 
        "chillwave", "electroclash", "chiptune", "8bit", "breakbeat", 
        "jungle", "ragga", "hardstyle", "gabber", "speedcore", "deathmetal", 
        "blackmetal", "doommetal", "sludgemetal", "thrashmetal", "heavymetal", 
        "powerballad", "folkmetal", "paganmetal", "vikingmetal", "symphonicmetal", 
        "gothicmetal", "glamrock", "progrock", "psychrock", "krautrock", 
        "postrock", "mathrock", "shoegaze", "altcountry", "altrock", 
        "artrock", "britpop", "grime", "UKgarage", "drill", "mumblecore", 
        "cloudrap", "gangstarap", "consciousrap", "neofolk", "neoclassical", 
        "minimalism", "maximalism", "fluxus", "freakfolk", "hypnagogicpop", 
        "nugaze", "futurerave", "techhouse", "electrohouse", "deeptech", 
        "microhouse", "techstep", "neurofunk", "liquidfunk", "hardbass", 
        "hardbounce", "aggrotech", "cyberpunk", "darkwave", "darkambient", 
        "drone", "neoclassicaldarkwave", "neofolk", "ritualambient", "martialindustrial", 
        "martialambient", "powernoise", "deathindustrial", "powernoise", "postindustrial", 
        "breakcore", "speedcore", "terrorcore", "extratone", "noisecore", "doomcore", 
        "doomjazz", "murderfolk", "witchhouse", "neowitch", "vogue", "kpop", 
        "jpop", "cpop", "mandopop", "trot", "enka", "citypop", "idol", 
        "idolpop", "idolkpop", "discoidolkpop", "tropikpop", "neokpop", "syndiepop", 
        "hybrid", "bassline", "kawaiimetal", "idolmetal", "idolrock", "extremeidol", 
        "deathgrind", "deathcore", "metalcore", "grindcore", "sludgecore", "postcore", 
        "mathcore", "noisecore", "bluesrock", "garagepunk", "glitchhop", "moombahcore", 
        "hyphy", "trapmetal", "trapwave", "phonk", "trapsoul", "latintrap", "latinhop", 
        "latinjazz", "latinrock", "latinpop", "salsafusion", "reggaeton", "dembow", 
        "latinhouse", "latinbounce", "latincore", "latindisco", "cumbia", "vallenato", 
        "bossa", "samba", "tango", "bolero", "cha", "mambo", "rhumba", "flamenco", 
        "mestizo", "ranchera", "mariachi", "norteno", "tehano", "grupera", 
        "banda", "duranguense", "corridos", "nueva", "regional", "salsa", 
        "merengue", "bachata", "punta", "timba", "son", "rumba", "charanga", 
        "chachacha", "conga", "bomba", "plena", "candombe", "murga", "pagode", 
        "forro", "brega", "arrocha", "lambada", "carimbo", "frevo", "maracatu", 
        "axemusic", "calypso", "socamusic", "dancehall", "mento", "reggaeska", 
        "rocksteady", "loversrock", "dubmusic", "rootsreggae", "ska", 
        "thirdwave", "2tone", "moonstomp", "skajazz", "skaore", "ska", "mod"
    ]
}
    # Randomly select a genre
    genre = random.choice(genres)
    words = genre_words.get(genre, [])

    # Ensure there are at least two words in the genre
    if len(words) < 2:
        return None, None
    
    # Randomly select two different words from the genre
    word1, word2 = random.sample(words, 2)
    
    # Check if they exist on Wikipedia
    page1 = get_wikipedia_page(word1)
    page2 = get_wikipedia_page(word2)

    if page1 and page2:
        return word1, word2
    else:
        return None, None

if __name__ == "__main__":
    genres = ["technology", "art", "science", "literature", "music"]
    word1, word2 = generate_words(genres)
    

    print(get_wikipedia_page("Catholic"))
    if word1 and word2:
        print(f"Generated words: {word1}, {word2}")
    else:
        print("Could not find two suitable words.")
