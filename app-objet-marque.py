import random

# Liste XXL d'objets
objets = [
    "chaise", "table", "lampe", "montre", "sac", "vélo", "bouteille", "ordinateur",
    "smartphone", "écouteurs", "voiture", "avion", "train", "skateboard", "trottinette",
    "stylo", "livre", "cahier", "valise", "parfum", "lunettes", "chaussures", "veste",
    "canapé", "lit", "oreiller", "tasse", "assiette", "fourchette", "couteau", "frigo",
    "machine à café", "aspirateur", "drone", "console de jeux", "caméra", "enceinte",
    "piano", "guitare", "batterie", "microphone", "robot", "montagne russe", "bague",
    "collier", "pantalon", "pull", "casque de réalité virtuelle", "planche de surf",
    "raquette de tennis", "ballon de foot", "ballon de basket", "ballon de rugby",
    "skis", "snowboard", "trottinette électrique", "hoverboard", "trampoline",
    "machine à laver", "sèche-linge", "four", "plaque de cuisson", "mixeur",
    "grille-pain", "bouilloire", "ventilateur", "radiateur", "climatiseur",
    "aspirateur robot", "brosse à dents", "rasoir", "sèche-cheveux", "fer à lisser",
    "fer à repasser", "machine à écrire", "projecteur", "écran", "imprimante",
    "scanner", "tablette", "routeur", "clé USB", "disque dur", "carte graphique",
    "manette de jeu", "volant gaming", "chaise gaming", "bureau", "étagère",
    "bibliothèque", "lampe torche", "lanterne", "bougie", "horloge", "calendrier",
    "carte", "globe terrestre", "maquette", "figurine", "jouet", "poupée",
    "peluche", "lego", "jeu de société", "jeu de cartes", "dominos", "échecs",
    "ballon de plage", "parasol", "serviette", "maillot de bain", "palmes",
    "masque de plongée", "tente", "sac de couchage", "matelas gonflable",
    "chaussures de randonnée", "bâton de marche", "gourde", "thermos",
    "couteau suisse", "boussole", "jumelles", "appareil photo", "caméscope",
    "drone caméra", "casque audio", "enceinte Bluetooth", "lecteur MP3",
    "platine vinyle", "CD", "DVD", "Blu-ray", "clé HDMI", "câble USB",
    "chargeur", "powerbank", "station de recharge", "panneau solaire",
    "éolienne miniature", "kit électronique", "Arduino", "Raspberry Pi",
    "capteur", "imprimante 3D", "scanner 3D", "robot éducatif"
]

# Liste XXL de marques
marques = [
    "Apple", "Nike", "Adidas", "Lego", "Tesla", "Ikea", "Chanel", "Sony", "Samsung",
    "Microsoft", "Google", "Amazon", "Louis Vuitton", "Gucci", "Prada", "Hermès",
    "Rolex", "Cartier", "Puma", "Reebok", "Under Armour", "North Face", "Patagonia",
    "Zara", "H&M", "Uniqlo", "Balenciaga", "Versace", "Ferrari", "BMW", "Mercedes",
    "Toyota", "Honda", "Peugeot", "Renault", "Airbus", "Boeing", "SpaceX", "Netflix",
    "Disney", "Pixar", "Warner Bros", "PlayStation", "Xbox", "Nintendo", "Dell",
    "HP", "Lenovo", "Canon", "Nikon", "GoPro", "Dyson", "Philips", "Panasonic",
    "LG", "Huawei", "Oppo", "Xiaomi", "OnePlus", "Motorola", "Intel", "AMD",
    "Nvidia", "Qualcomm", "Red Bull", "Coca-Cola", "Pepsi", "Sprite", "Fanta",
    "Evian", "Volvic", "Nestlé", "Danone", "Kellogg's", "Oreo", "Nutella",
    "Haribo", "Kinder", "Milka", "Lindt", "Starbucks", "McDonald's", "Burger King",
    "KFC", "Subway", "Domino's", "Pizza Hut", "Uber", "Lyft", "Airbnb", "Booking",
    "Tripadvisor", "Expedia", "Nike Jordan", "Converse", "Vans", "Timberland",
    "Crocs", "Birkenstock", "New Balance", "Asics", "Mizuno", "Salomon",
    "Decathlon", "Go Sport", "Intersport", "Patagonia", "Columbia", "Arc'teryx",
    "Moncler", "Canada Goose", "Lacoste", "Tommy Hilfiger", "Ralph Lauren",
    "Calvin Klein", "Diesel", "Levi's", "Wrangler", "Lee", "Dockers",
    "Benetton", "Superdry", "Abercrombie", "Hollister", "Gap", "Old Navy",
    "Primark", "Marks & Spencer", "Next", "Mango", "Massimo Dutti"
]

def generateur():
    objet = random.choice(objets)
    marque = random.choice(marques)
    return f"{objet} – {marque}"

# Générer quelques exemples
if __name__ == "__main__":
    print("💡 Inspirations XXL pour designers :")
    for _ in range(20):
        print(generateur())