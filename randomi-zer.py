import requests, random, time, os
from pprint import pprint

# Put your TOKEN here
TOKEN = ""
#

def get_song(headers):
    s = random.randint(100000, 2200000)
    req_url = "https://api.genius.com/songs/" + str(s)
    
    r = requests.get(req_url, headers = headers)
    if r.json()["meta"]["status"] == 200:
        print("Found you a song! \n")
        return r
    else:
        print("404, trying again")
        get_song(headers)



def get_yt_link(r):
    yt = r["response"]["song"]["media"]
    
    if yt:
        for d in yt:
            try:
                if d["provider"] == "youtube":
                    print("Watch on YT @", d["url"])
            except:
                pass
    
    
def get_date(r):
    date = r["response"]["song"]["release_date_for_display"]
    
    if date:
        print("Out in", date)
   
   
            
def main():
    # Authorization header
    headers = {"User-Agent": "CompuServe Classic/1.22",
    "Accept": "application/json",
    "Host": "api.genius.com",
    "Authorization": "Bearer " + TOKEN
}
    
    # Fetch a song at random
    try:
        r = get_song(headers).json()
    except:
        print("Unknown error happened.")
        break
    # Prints the result
    print("Got you", r["response"]["song"]["full_title"])
    print("@", r["response"]["song"]["url"])
    
    # Prints date if it exists
    get_date(r)
    # Prints YT link if it exists
    get_yt_link(r)



if __name__ == "__main__":
    # User Interface
    W, H = os.get_terminal_size()
    print(" Welcome to genius randomi-zer v1.0".center(W, "-"))
    print("Getting you a song... \n")
    time.sleep(1.618033)
    
    main()
