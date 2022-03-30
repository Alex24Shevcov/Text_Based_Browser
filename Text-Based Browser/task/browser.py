import argparse
import re
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore


parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()


def my_create_folder(name_dir) -> None:
    if not os.access(f'./{name_dir}', os.F_OK):
        os.mkdir(f'./{name_dir}')


def my_create_file(path_to_file, text) -> str:
    with open(path_to_file, "w") as file:
        file.write(text)
    return text


def tag_processing(html_text) -> str:
    soup = BeautifulSoup(html_text, 'html.parser')
    unswer = ""
    for i in soup.find_all("p"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("h1"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("h2"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("h3"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("h4"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("h5"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("h6"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("a"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("ul"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("ol"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    for i in soup.find_all("li"):
        if len(i.text) > 0:
            if i.name == "a":
                unswer += Fore.BLUE + i.text.strip() + "\n"
            else:
                unswer += i.text.strip() + "\n"

    return unswer

my_create_folder(args.folder)

while (user_input := input()) != "exit":
    if not re.search(r"\..+$", user_input):
        print("Error: Incorrect URL")
        continue
    try:
        file_name = re.sub(r"\..+$", "", user_input)
        r = requests.get("https://" + user_input)
        s_text = tag_processing(r.content)
        print(my_create_file(f"./{args.folder}/{file_name}", s_text))
    except:
        print("Error: Incorrect URL")
