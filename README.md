# 🇩🇪 Nemački Master

**Nemački Master** je interaktivna web aplikacija dizajnirana da pomogne korisnicima u učenju nemačke gramatike, fokusirajući se na imenice, njihove rodove, množinu i deklinaciju kroz padeže.

## 👥 Autori
*   **Idejni tvorac & UI/UX koncept:** Andrijana Kostić
*   **Programiranje & Realizacija:** Vladimir Grujović

---

## 🚀 Glavne Funkcije
*   **Automatsko određivanje roda:** Koristi naprednu logiku sufiksa i eksterne API-je za precizno određivanje roda (*der*, *die*, *das*).
*   **Deklinacija kroz padeže:** Generiše oblike za Nominativ, Genitiv, Dativ i Akuzativ, uključujući pokazne zamenice (*dieser*).
*   **Pametna Množina:** Predviđa oblike množine na osnovu gramatičkih pravila.
*   **Audio Izgovor:** Integrisana glasovna podrška (Web Speech API).
*   **Dinamički dizajn:** Pozadina se menja u zavisnosti od roda reči (Plava/Roze/Zelena).

---

## 🛠️ Tehnologije
*   **Backend:** Python & Flask
*   **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript
*   **API:** Deep Translator & MyMemory API

---

## 📦 Instalacija i Pokretanje

1. **Kloniraj repozitorijum:**
   ```bash
   git clone [https://github.com/tvoj-username/nemacki-master.git](https://github.com/tvoj-username/nemacki-master.git)
   cd nemacki-master

    Instaliraj biblioteke:
    Bash

pip install flask requests deep-translator

Pokreni aplikaciju:
Bash

    python app.py


4. **Pristupi aplikaciji:**
   Otvori [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 Struktura Projekta
```text
/ nemacki-master
│-- app.py                # Flask backend logika
├── static/
│   └── style/
│       ├── style.css     # Dizajn aplikacije
│       └── script.js     # Logika za audio izgovor
└── templates/
    └── index.html        # HTML interfejs (Jinja2)---

---
## 🌍 Link
https://nemacki-master.onrender.com
