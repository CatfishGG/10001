import requests
def fetch_memes(num_memes):
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)
    data = response.json()
    
    memes = data["data"]["memes"][:num_memes]
    
    with open("memes.txt", "w") as file:
        for meme in memes:
            file.write(f"{meme['name']}: {meme['url']}\n")
    
    print(f"{num_memes} memes fetched and saved to memes.txt")

# Customize the number of memes to fetch
num_memes = 10

fetch_memes(num_memes)