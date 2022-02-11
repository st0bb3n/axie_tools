from requests import get
from datetime import datetime

API_URL = "https://game-api.axie.technology/api/v1/0x"

def generate_url(ronin):
    if len(ronin) == 46:
        url = API_URL + ronin[6:]
        return url
    else:
        dead = "https://game-api.axie.technology/api/v1/0x0"
        return dead
    
while True:
    address = str(input("Whats the ronin address?: "))
    data_url = generate_url(address)
    response = get(data_url)
    print("API Status: ", response.status_code)
    data_dict = response.json()

    if data_dict != {}:
        print("------Account Details------")
        print("Name: ", data_dict["name"])
        print("MMR: ", data_dict["mmr"])
        print("Rank: ", data_dict["rank"])
        print("------SLP------")
        print("Current: ", data_dict["in_game_slp"])
        print("Total Claimed: ", data_dict["lifetime_slp"])
        unix = data_dict["next_claim"]
        unix2 = data_dict["last_claim"]
        print("Last Claim: ", (datetime.utcfromtimestamp(unix2).strftime('%Y-%m-%d %H:%M:%S')))
        print("Next Claim: ", (datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')))

    else:
        print("Invalid Ronin Address")
