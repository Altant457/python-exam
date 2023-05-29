import requests
from bs4 import BeautifulSoup


def check_reviewpagenumbers():
    reviewliste = []
    count = 1

    while True:
        url = f"https://steamcommunity.com/id/PEYOTEISGOODFORYOU/recommended/?p={count}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        review_list_div = soup.find("div", class_="review_box_content")

        if review_list_div is not None:
            reviewliste.append(count)
            count += 1
        else:
            break    
        
    return reviewliste

antal_spilanmeldelser_array = check_reviewpagenumbers()

def get_reviews(antal_spilanmeldelser_array):
    # Define the URL of the Steam profile reviews page

    for i in range(len(antal_spilanmeldelser_array)):
        i+=1
        url = f"https://steamcommunity.com/id/PEYOTEISGOODFORYOU/recommended/?p={i}"

        # Send a GET request to the URL
        response = requests.get(url)

        # Create a BeautifulSoup object with the response content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the review containers on the page
        review_list_div = soup.find("div", class_="review_list")

        reviews = review_list_div.find_all("div", class_="title")

        for review in reviews:
            print(review)

get_reviews(antal_spilanmeldelser_array)



