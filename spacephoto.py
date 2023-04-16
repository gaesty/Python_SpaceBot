import requests
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import time
import tweepy

# consumer_key = 'Votre clé d\'API'
# consumer_secret = 'Votre clé secrète d\'API'
# access_token = 'Votre jeton d\'accès'
# access_token_secret = 'Votre jeton secret d\'accès'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

def dl_img_nasa(): 
    # Envoyer une requête GET à la page HTML contenant l'image
    response = requests.get("https://apod.nasa.gov/apod/astropix.html")

    # Créer un objet BeautifulSoup avec la réponse de la requête
    soup = BeautifulSoup(response.text, "html.parser")

    # Récupérer l'URL de l'image à partir de la balise img
    img_url = soup.find("img")["src"]
    img_path = "https://apod.nasa.gov/apod/"
    image = img_path + img_url
    
    # Récupérer le texte contenu dans l'élément HTML sélectionné par le sélecteur CSS
    element = soup.select_one("body > p:nth-child(3)")
    text = element.text
    start_index = text.find("Explanation:")
    end_index = text.find("Tomorrow's picture")
    formatted_text = text[start_index:end_index].strip()

    # supposons que la variable 'text' contient le texte anglais à traduire
    translator = Translator()
    time.sleep(1)
    global translated_text
    translated_text = translator.translate(formatted_text, dest='fr').text
    time.sleep(1)

    # Obtenir la date actuelle
    now = datetime.now()
    global date_string
    date_string = now.strftime("%Y-%m-%d")

    # Envoyer une requête GET à l'URL de l'image et enregistrer localement
    response = requests.get(image)
    with open(f"image-{date_string}.jpg", "wb") as f:
        f.write(response.content)

dl_img_nasa()
print(translated_text)
# api.update_with_media(f"image-{date_string}.jpg",translated_text)