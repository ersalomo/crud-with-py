import requests
import urllib.request as urllib


def main(url: str) -> None:
    print("""
        checking url
    """)
    reponse = urllib.urlopen(url)
    print(reponse.getcode())


print('This a sote connectivity checher program')
url = input('put u url here.?')

main(url)
