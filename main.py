import threading

from fake_useragent import UserAgent
import requests
import random
from colorama import Fore

with open("fio.txt", "r", encoding="utf-8") as file:
    fio = file.readlines()

request = 0


def check():
    with open("email.txt", "r", encoding="utf-8") as file:
        emails = file.readlines()
    while True:
        try:
            email, password = random.choice(emails).split(":")
        except ValueError:
            continue

        if email.endswith(("gmail.com", "hotmail.com")):
            return email


def main() -> None:
    global request

    while True:
        headers = {
            "User-Agent": UserAgent().random
        }

        data = {
            "message": "Здравствуйте.\n\nХочу сообщить, что канал @EKATIRINABURGKILL (ID: -1002481927546) желает всем смерти, возможно канал, который затеял терракт в новый год.\n\nПрошу срочно принять меры против этого пользователя.",
            "legal_name": random.choice(fio)[:-2],
            "email": check(),
            "phone": "",
            "setln": ""
        }

        response = requests.post("https://telegram.org/support", headers=headers, data=data)
        request += 1
        print(Fore.LIGHTGREEN_EX + f"send #{request}" + Fore.RESET)

for _ in range(10):
    threading.Thread(target=main).start()
