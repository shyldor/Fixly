from config import olx_search_urls
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"} # Потрібно для браузера

# Функція для отримання опису з кожного оголошення
def get_description(item_url, headers):
    page = requests.get(item_url, headers)
    soup = BeautifulSoup(page.text, "html.parser")
    description_block = soup.select_one('div[data-cy="ad_description"]')

    if description_block:
        description = description_block.find("div")  # бере 1 дочірній div

    return description.get_text(strip=True) if description else "Опис відсутній"

# Функція для парсера сторінки
def parse_olx(url):
    print(f"Парсимо {url}\n" + "=" * 100)
    ads = []
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    keywords = ["jbl", "iphone", "відновлення", "восстановл", "ремонт", "запчасти", "запчастини"]

    # Кожне оголошення зараз лежить у <div data-cy="l-card">
    for item in soup.select('div[data-cy="l-card"]'):

        title_elem = item.select_one('h4')  # Заголовок
        price_elem = item.select_one('p[data-testid="ad-price"]')  # Ціна
        link_elem = item.select_one('a')

        if not title_elem or not link_elem:
            continue

        link_elem = link_elem.get("href")
        if link_elem.startswith("/"):
            link_elem = "https://www.olx.ua" + link_elem # посилання


        descr_elem = get_description(link_elem, headers) # опис
        title = title_elem.get_text(strip=True)
        if any(word in title.lower() for word in keywords):
            ads.append({
                "title": title_elem.get_text(strip=True),
                "price": price_elem.get_text(strip=True) if price_elem else "—",
                "link": link_elem,
                "description": descr_elem
            })


        for ad in ads:
            ad_info = "*" *30 + "\n" + ad["title"] + "\nЦіна: " + ad["price"] + "\nОпис: " + ad["description"] + "\nПосилання: " + ad["link"]
            print(ad_info)


    return ads


 #analyze_ad(ads[0])



# Вивід результатів парсера
def showAds():
    for url in olx_search_urls: # перебір посилань для парсера
        parse_olx(url)




showAds()








