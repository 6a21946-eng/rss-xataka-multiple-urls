import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

# Lista de URLs a scrapear
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
fg.title("RSS Xataka Personalizado")
fg.link(href="https://www.xataka.com")
fg.description("Feed generado automáticamente con GitHub Actions")

print("Iniciando scrap de URLs...")

for url in urls:
    print(f"Leyendo {url}")
    try:
        r = requests.get(url, timeout=10)  # timeout 10s
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al leer {url}: {e}")
        continue

    soup = BeautifulSoup(r.content, "html.parser")
    # Extraemos titulares de artículos (ajustable según HTML)
    articles = soup.select("h2 a")  # selector genérico
    for a in articles:
        title = a.get_text(strip=True)
        link = a.get("href")
        if title and link:
            fe = fg.add_entry()
            fe.title(title)
            fe.link(href=link)

rss_file_path = "rss.xml"
fg.rss_file(rss_file_path)
print(f"RSS generado correctamente en {rss_file_path}")
