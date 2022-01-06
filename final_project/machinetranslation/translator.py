"""Importing necessary methods"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    """English text will convert into french"""
    frenchtext = language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    frenchtext = frenchtext['translations'][0]['translation']
    return frenchtext

def french_to_english(frenchtext):
    """French text will convert into english"""
    englishtext = language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    englishtext = englishtext['translations'][0]['translation']
    return englishtext
