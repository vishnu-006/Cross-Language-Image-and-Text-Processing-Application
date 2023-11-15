#                                                      MEANINGS OF THE GIVEN WORDS
import nltk
# nltk.download('punkt')
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from googletrans import Translator

word = set(stopwords.words("english"))
res = []
punc = {'.', ',', '?', ')', '&', '=', '+', '/', '(', '<', '>', '!', '@'}


def Tokenize(text):
    # print("insisde tokenize")
    word_tokens = word_tokenize(text)
    for k in word_tokens:
        if k.lower() not in word and k not in punc and not k.isdigit() and len(k) > 2:
            res.append(k)
    lan = input('''Select language : 
        1 . English
        2 . Telugu
        3 . Hindi   ''')
    if lan == "1":
        English()
    elif lan == "2":
        translate_to_telugu()
    else:
        translate_to_Hindi()


def Meaning(wrd):
    # print("insisde meaning")
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{wrd}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            # Assuming the JSON structure you provided
            meanings = data[0].get("meanings", [])
            if meanings:
                # Extract the first meaning's definition
                definition = meanings[0]["definitions"][0]["definition"]
                return definition
        return "Meaning not found"
    else:
        return "API request failed"


ans = []


def English():
    for q in res:

        call = Meaning(q)
        ans.append(call)
        print("{} = {}".format(q, call))
        # print(q)
        # translate_to_telugu(q)


def translate_to_telugu():
    translator = Translator()
    for q in res:
        translation = translator.translate(q, src='en', dest='te')  # 'en' for English, 'te' for Telugu
        print("{} = {} ".format(q,translation.text))
def translate_to_Hindi():
    translator = Translator()
    for q in res:
        translation = translator.translate(q, src='en', dest='hi')  # 'en' for English, 'te' for Telugu
        print("{} = {} ".format(q,translation.text))
