import requests, sys
from bs4 import BeautifulSoup
from .decorators import cache
import time

@cache
def check_reviewpagenumbers(steamID):
    reviewliste = []
    count = 1

    while True:
        url = f"https://steamcommunity.com/id/{steamID}/recommended/?p={count}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        review_list_div = soup.find("div", class_="review_box_content")
        time.sleep(1)
        if review_list_div is not None:
            reviewliste.append(count)
            count += 1
        else:
            break    
        
    return reviewliste

@cache
def get_reviews(steamID):
    # Define the URL of the Steam profile reviews page
    
    antal_spilanmeldelser_array = check_reviewpagenumbers(steamID)
    
    posReviews = []
    
    for i in range(len(antal_spilanmeldelser_array)):
        i+=1
        url = f"https://steamcommunity.com/id/{steamID}/recommended/?p={i}"
        time.sleep(1)
        # Send a GET request to the URL
        response = requests.get(url)

        # Create a BeautifulSoup object with the response content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the review containers on the page
        review_list_div = soup.find("div", class_="review_list")

        reviews = review_list_div.find_all("div", class_="title")
        
        for review in reviews:
                if not "Not" in review.string:
                    posReviews.append(review)
        
    if __name__ == "__main__":
        for review in posReviews:
            print(review)
    else:
        return posReviews
            

if __name__ == "__main__":
    try:
        get_reviews(sys.argv[1])
    except IndexError:
        print("\nUsage:\n\tpython scrapreviews.py <steamID>")
        print("\n\tYou can find someones steamID by going to their profile")
        print("\tand taking the steamID from the URL")
        print("\thttps://steamcommunity.com/id/<steamID>")
