import requests, sys
from bs4 import BeautifulSoup
from .decorators import cache
import time

@cache
def get_game_details_from_appID(appID):
    url = f"https://store.steampowered.com/app/{appID}"
    response = requests.get(url)
    time.sleep(1)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    
    appName = soup.find("div", id="appHubAppName")
    appDesc = soup.find("div", class_="game_description_snippet")
    genres = [a_element.text for a_element in 
             soup.find("div", id="genresAndManufacturer")
              .find("span")
              .find_all("a")]
    
    return appName, appDesc, genres

@cache
def get_appID(appName):
    if not hasattr(get_appID, "data"):
        base_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            app_list = data['applist']['apps']
            get_appID.data = app_list
    for app in app_list:
        if app['name'] == appName:
            return app['appid']
    return None