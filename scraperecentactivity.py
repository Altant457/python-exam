from bs4 import BeautifulSoup
import requests

#https://steamcommunity.com/profiles/76561198852767899/


profile_link = requests.get('https://steamcommunity.com/profiles/PEYOTEISGOODFORYOU/')

#Soup objektet laves
soup = BeautifulSoup(profile_link.content, "html.parser")

#Div med nyligt spillede spil findes
recent_games_div = soup.find('div', class_='recent_games')

#Checker om profil er privat eller om spiller ikke er aktiv
if recent_games_div is None:
            print("Denne profil er ikke oftenlig/ spiller er ikke aktiv")
            exit()

#Alle spil indenfor div findes
played_games = recent_games_div.find_all("div", class_="game_info")



#Her loopes der igennem spillene, .text og .strip bruges for et rent output

print("\n Nylig aktivitet: \n")

for game in played_games:
    gametitle = game.find('div', class_='game_name').text.strip()
    print(gametitle)



