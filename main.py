from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def prepare_page():
    html = urlopen("https://sponsr.ru/marahovsky/20985/Piramida_tehnichnyh_dikarei_trebuet_dat_ei_spasitelnyh_negrov/")
    bsObj = BeautifulSoup(html, features="html.parser")
    print(bsObj.h2.get_text())


if __name__ == '__main__':
    prepare_page()
