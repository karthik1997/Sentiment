import os
import urllib.parse

import requests
from bs4 import BeautifulSoup


def download_lyrics(url, dl_dir):
    path = urllib.parse.urlsplit(url).path.replace("/","")
    fname = os.path.join(dl_dir, path).replace(".html", ".txt")
    if not os.path.exists(fname):
        resp = requests.get(url)
        data = resp.text
        soup = BeautifulSoup(data, 'html.parser')
        lyrics = []
        for i in soup.find_all("p", attrs={"class":"verse"}):
            lyrics.append(i.text)
        with open(fname, "w") as f:
            f.write("\n".join(lyrics))

def download_all(url, name):
    print ("Downloading {}".format(name))
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    if not os.path.isdir(name):
        os.mkdir(name)

    document = requests.get(url, headers)
    data = document.text
    soup = BeautifulSoup(data, 'html.parser')
    tbl = soup.find('table', attrs={"class":"songs-table"})
    
    for i in tbl.find_all('a', attrs={"class":"title"}):
        print ("   {}".format(i['href']))
        download_lyrics(i['href'], name)

def main():
    # download_all("http://www.metrolyrics.com/britney-spears-lyrics.html", "spears")
    # download_all("http://www.metrolyrics.com/bob-dylan-lyrics.html", "dylan")
    # download_all("http://www.metrolyrics.com/metallica-lyrics.html", "metallica")
    # download_all("http://www.metrolyrics.com/snoop-doggy-dogg-lyrics.html", "dogg")
    # download_all("http://www.metrolyrics.com/dire-straits-lyrics.html", "straits")
    download_all("http://www.metrolyrics.com/megadeth-lyrics.html", "megadeth")


if __name__ == "__main__":
    main()
