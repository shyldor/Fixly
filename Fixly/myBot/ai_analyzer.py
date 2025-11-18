from g4f import ChatCompletion
from scipy.special import title


def find_order(ads):
    print("Шукаю пацієнта" + "."*10)
    prompt = (
       "Обери найвигідніше оголошення для ремонту за описом і потенційним прибутком."
    )

    return prompt  # ✅ бо тут уже str


# Тест:
ad = {
    "title": "JBL Boombox 2 — не працює динамік",
    "description": "Тільки один динамік працює, під’єднання Bluetooth.",
    "price": "1200 грн"
}

def single_analyze(selectedAd):
    prompt = (
        "Аналіз оголошення: проблема і рентабельність ремонту. Дуже стисло."
        f"{selectedAd['title']}"
        f"{selectedAd['price']}"
        f"{selectedAd['description']}"
    )