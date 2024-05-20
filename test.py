from utils_crud import CRUDLClass

cc = CRUDLClass()

"""
arr1 = ["Jupiter", "Juno", "Neptune", "Minerva", "Mars", "Venus", "Apollo", "Diana", "Vulcan", "Vesta", "Mercury", "Ceres", "Bacchus", "Pluto", "Proserpina", "Janus", "Bellona", "Fortuna", "Aurora", "Luna", "Sol", "Faunus", "Quirinus", "Tellus", "Victoria", "Lares", "Larunda", "Hercules", "Somnus", "Salacia", "Bona Dea", "Ops", "Felicitas", "Flora", "Terminus", "Pax", "Pomona", "Juventas", "Libitina", "Mors", "Fama", "Spes", "Fides", "Concordia", "Virtus", "Honos", "Invidia", "Pietas", "Aesculapius", "Dis Pater", "Aeternitas", "Annona", "Cacus", "Cardea", "Cloacina", "Decima", "Deverra", "Edesia", "Empanda", "Ferentina", "Fides Publica", "Forculus", "Inuus", "Juturna", "Levana", "Liber", "Libertas", "Lupercus", "Mellona", "Moneta", "Mutunus Tutunus", "Nascio", "Necessitas", "Nemesis", "Orbona", "Palatua", "Pales", "Parcae", "Picumnus", "Pilumnus", "Poena", "Portunes", "Postverta", "Proca", "Pudicitia", "Quiritis", "Robigo", "Rumina", "Sancus", "Sarritor", "Securitas", "Sentia", "Silvanus", "Stata Mater", "Sterquilinus", "Strenua", "Suadela", "Tacita", "Terminus", "Tiberinus", "Trivia", "Vacuna"]
brr1 = [
    "John", "Mary", "David", "Sarah", "Michael", "Jennifer", "James", "Jessica", "Robert", "Emily",
    "William", "Melissa", "Daniel", "Kimberly", "Christopher", "Ashley", "Joseph", "Amanda", "Matthew", "Nicole",
    "Andrew", "Elizabeth", "Ryan", "Megan", "Joshua", "Lauren", "Brian", "Rachel", "Kevin", "Brittany",
    "Eric", "Samantha", "Jason", "Heather", "Justin", "Tiffany", "Brandon", "Stephanie", "Nicholas", "Amber",
    "Jonathan", "Christina", "Steven", "Katherine", "Timothy", "Michelle", "Thomas", "Alyssa", "Jeffrey", "Danielle",
    "Kenneth", "Rebecca", "Gregory", "Angela", "Benjamin", "Courtney", "Patrick", "Shannon", "Anthony", "Laura",
    "Mark", "Crystal", "Scott", "Erica", "Tyler", "Kelly", "Alexander", "Lindsey", "Zachary", "Jamie",
    "Samuel", "Erin", "Matthew", "Hannah", "Adam", "Victoria", "Nicholas", "Katie", "Jordan", "Maria",
    "Dylan", "Julie", "Jose", "Sara", "Nathan", "Anna", "Christian", "Alexis", "Kyle", "Kristen"
]
crr1 = ["Brahma", "Vishnu", "Shiva", "Lakshmi", "Saraswati", "Parvati", "Ganesha", "Kartikeya", "Rama", "Krishna", "Radha", "Hanuman", "Durga", "Kali", "Sita", "Ravana", "Indra", "Agni", "Varuna", "Vayu", "Surya", "Chandra", "Yama", "Kubera", "Ganga", "Bhu Devi", "Aditi", "Diti", "Rati", "Kamadeva", "Annapurna", "Vishwakarma", "Gayatri", "Savitri", "Dhanvantari", "Narada", "Garuda", "Shesha", "Nandi", "Nataraja", "Bhairava", "Chamunda", "Bhumi", "Matsya", "Kurma", "Varaha", "Narasimha", "Vamana", "Parashurama", "Balarama", "Buddha", "Kalki", "Yamuna", "Tulsi", "Shani", "Mangala", "Budha", "Brihaspati", "Shukra", "Rahu", "Ketu", "Chhinnamasta", "Bagalamukhi", "Matangi", "Kamala", "Tara", "Bhuvaneshwari", "Lalita", "Dhumavati", "Vajreshwari", "Anjaneya", "Ayyappa", "Murugan", "Meenakshi", "Valli", "Devayani", "Tripura Sundari", "Manasa", "Santoshi Mata", "Shitala", "Prithvi", "Svaha", "Aranyani", "Ashwatthama", "Balarama", "Bhagiratha", "Bhishma", "Draupadi", "Ganga", "Karna", "Kauravas", "Nakula", "Pandavas", "Sahadeva", "Shakuni", "Vidura", "Vishnu"]
drr1 = ["Amaterasu", "Tsukuyomi", "Susanoo", "Inari", "Hachiman", "Benten", "Daikokuten", "Ebisu", "Fukurokuju", "Jurōjin", "Bishamonten", "Kisshōten", "Sarutahiko", "Ame-no-Uzume", "Omoikane", "Ame-no-Koyane", "Futodama", "Takeminakata", "Kotoamatsukami", "Kunitsu-kami", "Takamimusubi", "Kamimusubi", "Amatsuhikone", "Umashimaji", "Ajisukitakahikone", "Otoshigo", "Toyouke", "Ukemochi", "Owatatsumi", "Watatsumi", "Izanagi", "Izanami", "Omoikane", "Konohanasakuya-hime", "Ninigi", "Yebisu", "Toyotama-hime", "Hoori", "Tamayori-hime", "Jimmu", "Omoikane", "Tsukiyomi", "Kagutsuchi", "Ame-no-Tajikarao", "Ame-no-Hohi", "Kotoshironushi", "Takemikazuchi", "Takeminakata", "Fujin", "Raijin", "Tenjin", "Bishamon", "Marishiten", "Kichijoten", "Chimata-no-kami", "Miyazu-hime", "Ukanomitama", "Kukunochi", "Ōyamatsumi", "Kayanuhime", "Kamotaketsunumi", "Toyouke-Ōmikami", "Mizuhanome", "Haniyasu-hiko", "Haniyasu-hime", "Kuraokami", "Hayaakitsuhiko", "Hayaakitsuhime", "Ishikoridome", "Amenohiboko", "Kotoshironushi", "Sarudahiko", "Ame-no-Kaguyama-hime", "Shinatsuhiko", "Ninigi-no-Mikoto", "Tajimamori", "Hoderi", "Hoori", "Hikohohodemi", "Omoikane", "Kuninotokotachi", "Amenominakanushi", "Takamimusubi", "Kamimusubi", "Iwanagahime", "Takamimusubi", "Ame-no-Minakanushi", "Toyokumono", "Ame-no-Mahitotsu", "Toyotama-hiko", "Sukuna-Biko", "Okuninushi", "Sukunahikona", "Tamayori-hime", "Yamato-Takeru"]
err1 = ["Ra", "Osiris", "Isis", "Horus", "Anubis", "Thoth", "Set", "Hathor", "Ptah", "Bastet", "Sekhmet", "Nut", "Geb", "Shu", "Tefnut", "Nephthys", "Ma'at", "Amun", "Mut", "Khonsu", "Seshat", "Hapi", "Anuket", "Khepri", "Serqet", "Taweret", "Bes", "Sobek", "Wadjet", "Hathor", "Khnum", "Montu", "Ra-Horakhty", "Aten", "Aker", "Ammit", "Anhur", "Apophis", "Babi", "Banebdjedet", "Bat", "Hedjet", "Heh", "Heket", "Heryshaf", "Ihy", "Imhotep", "Kauket", "Khepri", "Kherty", "Mafdet", "Mandulis", "Mehen", "Menhit", "Meretseger", "Meskhenet", "Min", "Mnevis", "Mut", "Nefertum", "Nehebkau", "Nekhbet", "Nun", "Pakhet", "Ptah", "Qebehsenuef", "Raet-Tawy", "Renenutet", "Reshep", "Satet", "Seker", "Selket", "Sepa", "Serapis", "Seshat", "Shai", "Shed", "Shu", "Sobek", "Sokar", "Sopdet", "Sothis", "Tatenen", "Taweret", "Tefnut", "Thoth", "Wadjet", "Wepwawet", "Yamm", "Ra-Horakhty", "Ptah-Sokar-Osiris", "Horus the Elder", "Horus the Younger", "Neith", "Anhur", "Aten"]
frr1 = ["Anu", "Enlil", "Enki", "Ninhursag", "Inanna", "Utu", "Nanna", "Dumuzi", "Ereshkigal", "Nergal", "Marduk", "Ashur", "Ishtar", "Nabu", "Tiamat", "Kingu", "Adad", "Nisaba", "Ninurta", "Gula", "Ninkasi", "Ninlil", "Lahar", "Ashnan", "Mami", "Geshtinanna", "Dagan", "Ningishzida", "Anshar", "Kishar", "Lamashtu", "Lilith", "Lulal", "Namtar", "Nanshe", "Nidaba", "Ninsun", "Ningal", "Ninazu", "Nergal", "Ninurta", "Papsukkal", "Shamash", "Sin", "Tashmetu", "Ubelluris", "Urshanabi", "Zababa", "Ziusudra", "Ninlil", "Ninhursag", "Belet-ili", "Nintu", "Ninkarrak", "Ninisina", "Ninmena", "Ninsun", "Ninkurra", "Nanshe", "Nidaba", "Ningikuga", "Ninhursag", "Nin-imma", "Uttu", "Lugalbanda", "Ninsikila", "Nindara", "Inshushinak", "Napirisha", "Kiririsha", "Nergal", "Erra", "Ishum", "Anunnaki", "Igigi", "Lahmu", "Lahamu", "Alalu", "Damkina", "Qingu", "Namtar", "Mushdamma", "Endursaga", "Ninmada", "Ninagal", "Ningikuga", "Ningizzida", "Ninsikila", "Pazuzu", "Ugallu", "Azimua", "Kubaba", "Geshtu-e", "Siduri"]
grr1 = ["Atingkok", "Atinga", "Atingpi", "Sanamahi", "Leimarel Sidabi", "Pakhangba", "Nongshaba", "Ating AA", "Panthoibi", "Thangjing", "Marjing", "Wangbrel", "Koubru", "Ibudhou", "Apanba", "Kounu", "Yumjao Lairembi", "Nongthang Leima", "Thumleima", "Eputhou Thangnarel", "Lainingthou Eputhou Pakhangba", "Konthoujam Tiren", "Khamlangba", "Lainingthou Nongshaba", "Ireima", "Ibendhou", "Nongpok Ningthou", "Pureiromba", "Khoriphaba", "Korouhanba", "Pachilpam", "Irum Ningthou", "Irum Yangoibi", "Yumjao Ningthou", "Ngaleima", "Thoudu Nungthel Leima", "Wakching Taret", "Koiremba", "Lok Ningthou", "Yumjao Ningthou", "Koubru Lairembi", "Ikop Ningthou", "Khaba Nongpok Ningthou", "Heibok Ningthou", "Yangoiningthou", "Khuman Apokpa", "Irengba", "Laisrengbao", "Waithou Pakhangba", "Moilang Ningthou", "Laikhurembi", "Thangnarel Ema", "Eputhou Thangnarel", "Leimarel Shidabi", "Khamlangba", "Langol Ningthou", "Leipakpokpi", "Koubru Angouba", "Nongpok Ningthou", "Pachilpam", "Lainingthou Chingkhei Nungnang", "Tengnongpanba", "Heimang Lai", "Maring Leima", "Khuman Pokpa", "Hikchingi", "Heimang Leima", "Heimang Hanjaba", "Heimang Ahalpa", "Heimang Ningthou", "Heimang Apanba", "Heimang Khongba", "Heimang Khamla", "Heimang Khudong", "Heimang Pukhei", "Heimang Apokpa", "Heimang Pokpa", "Khamlangba", "Thangjing", "Pureiromba", "Koubru", "Koubru Lairembi", "Ebudhou Pakhangba", "Panthoibi", "Nongshaba", "Apanba", "Koubru Sanamahi", "Lainingthou Nongpok Ningthou", "Nongpok Ningthou", "Panthoibi", "Ibudhou Marjing", "Thangjing", "Nongshaba", "Pakhangba", "Apanba", "Koubru", "Sanamahi", "Leimarel Sidabi"]
hrr1 = [
    "Zephyr", "Aurora", "Phoenix", "Luna", "Maverick", "Nova", "Blaze", "Seraphina", "Orion", "Serenity",
    "Jett", "Aria", "Ryder", "Stella", "Cruz", "Fiona", "Kai", "Lorelei", "Axel", "Raven",
    "Zara", "Dante", "Skylar", "Athena", "Cyrus", "Indigo", "Sasha", "Zane", "Jasmine", "Atlas",
    "Fable", "Xavier", "Juno", "Wilder", "Violet", "Zion", "Jade", "Wolf", "Zara", "Echo",
    "Pheonix", "Aurora", "Sage", "Loki", "Nova", "Aurora", "Onyx", "Rain", "Crimson", "Luna",
    "Kai", "Aurora", "Hunter", "Athena", "Rogue", "Aria", "Sable", "Phoenix", "Orion", "Nova",
    "Skylar", "Aurora", "River", "Luna", "Jax", "Aurora", "Phoenix", "Athena", "Zane", "Aurora",
    "Serenity", "Jett", "Aurora", "Phoenix", "Serenity", "Ryder", "Aurora", "Phoenix", "Zara", "Aurora",
    "Zephyr", "Aurora", "Phoenix", "Luna", "Maverick", "Aurora", "Phoenix", "Serenity", "Nova", "Aurora"
]
irr1 = [
    "Pixie Byte", "Cybernymph Glitch", "Quantum Sparkle", "Data Sprite", "Binary Blossom",
    "Neon Whimsy", "Byte Sprite", "Circuit Spark", "Virtual Flicker", "Techno Faerie",
    "Pixel Flutter", "Code Whisper", "Digital Glimmer", "Neon Charm", "Cyber Sylph",
    "Pixel Dust", "Byte Whirl", "Techno Glow", "Matrix Sprite", "Cyber Pixie",
    "Quantum Flitter", "Byte Bloom", "Virtual Shimmer", "Data Whisperer", "Cyber Glint",
    "Techno Fae", "Binary Luminescence", "Code Glitter", "Virtual Tinker", "Digital Glow",
    "Neon Sprite", "Matrix Spark", "Cybernymph Beam", "Pixel Whimsy", "Circuit Twinkle",
    "Quantum Wisp", "Byte Luminary", "Cybernymph Flare", "Data Twinkle", "Neon Sylph",
    "Techno Twirl", "Binary Blaze", "Code Flicker", "Virtual Sparkle", "Digital Radiance",
    "Matrix Glow", "Cyber Sprite", "Pixel Whisper", "Quantum Glitter", "Byte Twinkle",
    "Cybernymph Gleam", "Data Glow", "Neon Faerie", "Techno Glimmer", "Binary Gleam",
    "Code Sparkle", "Virtual Twirl", "Digital Luminary", "Matrix Flitter", "Cyber Glow",
    "Pixel Glint", "Quantum Pixie", "Byte Flare", "Cybernymph Spark", "Data Flicker",
    "Neon Twinkle", "Techno Shimmer", "Binary Sprite", "Code Luminescence", "Virtual Glitch",
    "Digital Whimsy", "Matrix Charm", "Cyber Whirl", "Pixel Luminary", "Quantum Glitter",
    "Byte Glimmer", "Cybernymph Flitter", "Data Glow", "Neon Faerie", "Techno Glimmer",
    "Binary Gleam", "Code Sparkle", "Virtual Twirl", "Digital Luminary", "Matrix Flitter",
    "Cyber Glow", "Pixel Glint", "Quantum Pixie", "Byte Flare", "Cybernymph Spark",
    "Data Flicker", "Neon Twinkle", "Techno Shimmer", "Binary Sprite", "Code Luminescence",
    "Virtual Glitch", "Digital Whimsy", "Matrix Charm", "Cyber Whirl", "Pixel Luminary"
]
jrr1 = [
    "Aldric", "Thia", "Gareth", "Lyra", "Finnian", "Elara", "Cedric", "Rowan", "Valeria", "Drake",
    "Isolde", "Lysander", "Eira", "Aurelius", "Maia", "Tristan", "Iliana", "Baelor", "Eowyn", "Thorin",
    "Elowen", "Soren", "Evangeline", "Cassius", "Seraphina", "Gideon", "Elara", "Emrys", "Arabella", "Rhys",
    "Aurora", "Alistair", "Selene", "Lucien", "Lyra", "Cyrus", "Elara", "Dorian", "Thalia", "Theodore",
    "Isolde", "Bastian", "Seraphina", "Caelum", "Aurelia", "Finley", "Eira", "Oberon", "Maeve", "Leonidas",
    "Elowen", "Ariadne", "Artemis", "Thalia", "Cassian", "Evangeline", "Lysander", "Aurora", "Faelan", "Elara",
    "Lorcan", "Isolde", "Caius", "Eowyn", "Cassian", "Seraphina", "Nikolai", "Lyra", "Orion", "Elara",
    "Gwynevere", "Cedric", "Maeve", "Evander", "Elowen", "Alaric", "Arabella", "Lucius", "Thalia", "Calista",
    "Evangeline", "Orion", "Aurora", "Darius", "Elara", "Ezra", "Isolde", "Thorne", "Elowen", "Lucian",
    "Lyra", "Vesper", "Eira", "Castor", "Seraphina", "Finneas", "Elara", "Cassius", "Elowen"
]
krr1 = [
    "Rose", "Lily", "Violet", "Daisy", "Ivy", "Jasmine", "Hazel", "Fern", "Willow", "Sage",
    "Luna", "Wren", "Robin", "Dove", "Phoenix", "Blossom", "Flora", "Fauna", "Juniper", "Petal",
    "Acacia", "Aster", "Dahlia", "Maple", "Birch", "Poppy", "Primrose", "Rowan", "Alder", "Thorn",
    "Saffron", "Marigold", "Lavender", "Bluebell", "Magnolia", "Olive", "Cypress", "Aspen", "Clover", "Fawn",
    "Pine", "Cedar", "Willow", "Raven", "Coral", "Lotus", "Iris", "Orchid", "Tulip", "Hyacinth",
    "Sunflower", "Dandelion", "Meadow", "Storm", "Sky", "Ocean", "River", "Rain", "Storm", "Moss",
    "Peony", "Anemone", "Amaryllis", "Azalea", "Camellia", "Carnation", "Cherry", "Daffodil", "Forget-me-not", "Heather",
    "Jonquil", "Lilac", "Mimosa", "Narcissus", "Pansy", "Snapdragon", "Thistle", "Verbena", "Zinnia", "Bee",
    "Butterfly", "Dragonfly", "Hummingbird", "Ladybug", "Firefly", "Starling", "Sparrow", "Fox", "Bear", "Wolf",
    "Falcon", "Hawk", "Eagle", "Lynx", "Panther", "Otter", "Swan", "Tiger", "Cheetah", "Leopard"
]





courses = [
    'BAPAN',
    'BAPhilo',
    'BAPOLSCI',
    'BAPSYCH',
    'BASocio',
    'BEED-SCIMAT',
    'BPE',
    'BSA',
    'BSBIO',
    'BSBIO-ANBIO',
    'BSBIO-BOT',
    'BSCA',
    'BSCE',
    'BSCHE',
    'BSCHEM',
    'BSCPE',
    'BSCS',
    'BSE',
    'BSED-BIO',
    'BSED-FIL',
    'BSED-MAT',
    'BSED-PHY',
    'BSEE',
    'BSEM',
    'BSENE',
    'BSESE',
    'BSHM',
    'BSIS',
    'BSIT',
    'BSMAT',
    'BSMB',
    'BSME',
    'BSMETE',
    'BSN',
    'BSNursing',
    'BSPHY',
    'BSPSYCH',
    'BSSTAT'
]

import random
from utils_crud import CRUDLClass

def randArray():
    num = random.randint(1, 9)
    if num==1:
        return arr1
    if num==2:
        return brr1
    if num==3:
        return crr1
    if num==4:
        return drr1
    if num==5:
        return err1
    if num==6:
        return frr1
    if num==7:
        return grr1
    if num==8:
        return hrr1
    if num==9:
        return irr1
    if num==10:
        return jrr1
    if num==11:
        return krr1
    
def generate_random_name():
    name = random.choice(randArray())  # Assuming randArray() is a function you've defined elsewhere
    name += ' ' + random.choice(randArray())  # Adding parentheses to call randArray() function correctly
    return name

def generate_random_course():
    name = random.choice(courses)  # Assuming randArray() is a function you've defined elsewhere
    return name

genders = ['Man', 'Woman']
def generate_random_gender():
    name = random.choice(genders)  # Assuming randArray() is a function you've defined elsewhere
    return name

cc = CRUDLClass()

for number in range(250, 350):
    formatted_number = str(number).zfill(4).strip()
    cc.createStudent(studentID=f"2019-{formatted_number}", studentName=generate_random_name(), courseID=generate_random_course(), yearLevel=5, gender = generate_random_gender())
"""