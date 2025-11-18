ads = [
    {
        "title" : "jbl charge 3",
        "price" : "4324 грн",
        "link" : "https://www.google.com/search?q=jbl+charge+3"
    },
    {
        "title" : "jbl charge 4",
        "price" : "1114",
        "link" : "https://www.google.com/search?q=jbl+charge+4"
    }
]

for ad in ads:
    ad_info = ad["title"] + "\nЦіна: " + ad["price"] + "\nПосилання: " + ad["link"]
    print(ad_info)