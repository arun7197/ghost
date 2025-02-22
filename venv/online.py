import requests
import pywhatkit as kit

def search_on_google(query):
    kit.search(query)
    
def youtube(video):
    kit.playonyt(video)