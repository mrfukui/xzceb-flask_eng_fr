"""translator document with apikey and url"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('Bh6RMQTDmmZgp48U4ayheGbgCZChPasK0zOviPUBphV8')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ed6775b3-80a2-40af-8132-7f5f433dcdf0')

def english_to_french(english_text):
    """english to french translation function"""
    frenchtranslation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return frenchtranslation["translations"][0]["translation"]

def french_to_english(french_text):
    """french to english translation function"""
    englishtranslation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return englishtranslation["translations"][0]["translation"]
