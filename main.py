# program that gets hypixel stats and stuff
# must do "pip install -u requests" to use
import requests

username = input("What is your minecraft username? ")
data = requests.get(f'https://api.slothpixel.me/users/{username}).json()
                    
if data['error']:
    print("bad")
                    
