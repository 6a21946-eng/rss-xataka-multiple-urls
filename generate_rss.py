# generate_rss.py
import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime

# URLs que quieres scrapear
urls = [
    "https://www.xataka.com/tag/crispr",
    "https://www.xataka.com/tag/genetica",
    "https://www.xataka.com/tag/retina",
    "https://www.xataka.com/tag/toyota",
    "https://www.xataka.com/tag/helicoptero",
    "https://www.xataka.com/tag/waymo",
    "https://www.xataka.com/categoria/seguridad",
    "https://www.xataka.com/tag/antivirus",
    "https://www.xataka.com/tag/hackers",
    "https://www.xataka.com/tag/ciberseguridad",
    "https://www.xataka.com/tag/seguridad-informatica",
    "https://www.xataka.com/tag/malware",
    "https://www.xatakawindows.com/tag/seguridad",
    "https://www.xatakamovil.com/categoria/seguridad"
]

fg = FeedGenerator()
fg.title("RSS diario de Xataka")
fg.link(href="https://github.com/usuario/repositorio", rel="self")
fg.description("Titulares diarios de Xataka en varias categorías")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

for url in urls:
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # Extrae los titulares: Xataka usa h2 con clase 'article-title'
        for item in soup.find_all("h2")[:10]:  # últimos 5 titulares
            a_tag = item.find("a")
            if a_tag:
                title = a_tag.get_text(strip=True)
                link = a_tag['href']
                fe = fg.add_entry()
                fe.title(title)
                fe.link(href=link)
                fe.pubDate(datetime.now())

    except Exception as e:
        print(f"Error con {url}: {e}")

# Genera el rss.xml
fg.rss_file("rss.xml")
print("rss.xml actualizado")
