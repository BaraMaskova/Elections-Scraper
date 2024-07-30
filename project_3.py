"""
project_3.py: třetí projekt do Engeto Online Python Akademie
author: Barbora Mašková
email: baramaskova@seznam.cz
discord: baramaskova
"""
import sys
import csv
import requests
from bs4 import BeautifulSoup


def get_html(link: str) -> BeautifulSoup:
    """Uložení HTML z adresy v argumentu. Vrací třídu BeautifulSoup."""
    response = requests.get(link)
    html = BeautifulSoup(response.text, "html.parser")
    print("STAHUJI DATA Z URL:", link)
    return html


if len(sys.argv) != 3:
    print('Zadal jsi nesprávný počet argumentů. Argumenty musí být 3. '
          'Název souboru, url adresa v uvozovkách a libovolný název výstupního .csv.')
    sys.exit()

url, output_file = sys.argv[1], sys.argv[2]
html = get_html(url)


def get_towns(soup: BeautifulSoup) -> list[str]:
    """Vrací seznam měst v daném okrese."""
    return [town.text for town in soup.find_all("td", "overflow_name")]


def get_links(soup: BeautifulSoup) -> list[str]:
    """Vrací URL adresu k získání detailů jednotlivých obcí požadovaného okresu."""
    return [f"https://volby.cz/pls/ps2017nss/{link.a['href']}" for link in soup.find_all("td", "cislo")]


def get_ids(soup: BeautifulSoup) -> list[str]:
    """Vrací identifikační čísla jednotlivých obcí."""
    return [i.text for i in soup.find_all("td", "cislo")]


def collect_parties(soup: BeautifulSoup) -> list[str]:
    """Vrací seznam kandidujících stran v daném okresu."""
    first_town_link = get_links(soup)[0]
    first_town_html = get_html(first_town_link)
    return [party.text for party in first_town_html.find_all("td", "overflow_name")]


def get_voter_stats(link: str) -> tuple[list[str], list[str], list[str]]:
    """Vrací statistiky voličů pro daný link."""
    html = get_html(link)
    voters = [v.text.replace('\xa0', ' ') for v in html.find_all("td", headers="sa2")]
    attendance = [a.text.replace('\xa0', ' ') for a in html.find_all("td", headers="sa3")]
    valid_votes = [c.text.replace('\xa0', ' ') for c in html.find_all("td", headers="sa6")]
    return voters, attendance, valid_votes


def collect_votes(links: list[str]) -> list[list[str]]:
    """Funkce vrací list listů, kde je chronologicky uveden procentuální
    výsledek každé z politických stran v každé z obcí."""
    votes = []
    for link in links:
        html = get_html(link)
        votes_search = html.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
        votes.append([f"{v.text} %" for v in votes_search])
    return votes


def create_rows(soup: BeautifulSoup) -> list[list[str]]:
    """Pomocná funkce pro tvorbu csv souboru vrací list listů, kdy v každém listu je chronologicky
    uvedeno ID konkrétní obce, její název, registrovaní voliči, zúčastnění voliči, platné hlasy a
    procentuální výsledky každé z kandidujících stran."""
    towns = get_towns(soup)
    ids = get_ids(soup)
    links = get_links(soup)

    voters, attendance, valid_ones = [], [], []
    for link in links:
        v, a, vo = get_voter_stats(link)
        voters.extend(v)
        attendance.extend(a)
        valid_ones.extend(vo)

    votes = collect_votes(links)
    rows = []
    for id, town, voter, attend, valid, vote in zip(ids, towns, voters, attendance, valid_ones, votes):
        rows.append([id, town, voter, attend, valid] + vote)
    return rows


def election2017(url: str, output_file: str) -> None:
    """Hlavní část funkce, která za pomoci výše uvedených funkcí vytváří csv soubor
    s volebními výsledky."""
    try:
        header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
        rows = create_rows(html)
        parties = collect_parties(html)

        print("UKLÁDÁM DATA DO SOUBORU:", output_file)

        header.extend(parties)
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)

        print("UKONČUJI:", sys.argv[0])
    except Exception as e:
        print(f"Nastala chyba: {e}")
        sys.exit(1)


if __name__ == '__main__':
    election2017(url, output_file)
