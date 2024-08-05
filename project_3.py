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
from typing import List, Tuple


def get_html(link: str) -> BeautifulSoup:
    """Fetch HTML from a given URL and return a BeautifulSoup object."""
    response = requests.get(link)
    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    print("Fetching data from URL:", link)
    return BeautifulSoup(response.text, "html.parser")


def get_towns(soup: BeautifulSoup) -> List[str]:
    """Return a list of town names in a given district."""
    return [town.text for town in soup.find_all("td", "overflow_name")]


def get_links(soup: BeautifulSoup) -> List[str]:
    """Return a list of URLs to obtain details of each municipality in a given district."""
    return [f"https://volby.cz/pls/ps2017nss/{link.a['href']}" for link in soup.find_all("td", "cislo")]


def get_ids(soup: BeautifulSoup) -> List[str]:
    """Return a list of IDs for each municipality."""
    return [i.text for i in soup.find_all("td", "cislo")]


def collect_parties(soup: BeautifulSoup) -> List[str]:
    """Return a list of political parties running in a given district."""
    first_town_link = get_links(soup)[0]
    first_town_html = get_html(first_town_link)
    return [party.text for party in first_town_html.find_all("td", "overflow_name")]


def get_voter_stats(link: str) -> Tuple[List[str], List[str], List[str]]:
    """Return voter statistics for a given link."""
    html = get_html(link)
    voters = [v.text.replace('\xa0', ' ') for v in html.find_all("td", headers="sa2")]
    attendance = [a.text.replace('\xa0', ' ') for a in html.find_all("td", headers="sa3")]
    valid_votes = [c.text.replace('\xa0', ' ') for c in html.find_all("td", headers="sa6")]
    return voters, attendance, valid_votes


def collect_votes(links: List[str]) -> List[List[str]]:
    """Return a list of lists where each sublist contains the vote percentages
    for each political party in each municipality."""
    votes = []
    for link in links:
        html = get_html(link)
        votes_search = html.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
        votes.append([f"{v.text} %" for v in votes_search])
    return votes


def create_rows(soup: BeautifulSoup) -> List[List[str]]:
    """Return a list of lists where each sublist contains data for a single municipality,
    including its municipality_id, name, registered voters, participating voters, valid votes, and
    percentage results for each political party."""
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
    for municipality_id, town, voter, attend, valid, vote in zip(ids, towns, voters, attendance, valid_ones, votes):
        rows.append([municipality_id, town, voter, attend, valid] + vote)
    return rows


def election2017(url: str, output_filename: str) -> None:
    """Main function that generates a CSV file with election results using the above functions."""
    try:
        soup = get_html(url)  # Moved inside the function to avoid code outside of functions
        header = ['Municipality Code', 'Municipality Name', 'Registered Voters', 'Issued Envelopes', 'Valid Votes']
        rows = create_rows(soup)
        parties = collect_parties(soup)

        print("Saving data to file:", output_filename)

        header.extend(parties)
        with open(output_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Process completed successfully.")
    except requests.exceptions.RequestException as e:
        print(f"HTTP error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Incorrect number of arguments. Expected 3: script name, URL, and output CSV filename.')
        sys.exit(1)

    url_arg, output_file_arg = sys.argv[1], sys.argv[2]
    election2017(url_arg, output_file_arg)
