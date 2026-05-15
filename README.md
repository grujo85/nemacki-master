---

# 🇩🇪 Nemački Master

- **Nemački Master** je interaktivna web aplikacija dizajnirana da pomogne korisnicima u učenju nemačke gramatike,
   fokusirajući se na imenice, njihove rodove, množinu i deklinaciju kroz padeže.

## 👥 Autori
*   **Idejni tvorac & UI/UX koncept:** Andrijana Kostić
*   **Programiranje & Realizacija:** Vladimir Grujović

---

## 🚀 Glavne Funkcije
*   **Automatsko određivanje roda:** Koristi naprednu logiku sufiksa i eksterne API-je za precizno određivanje da li je reč *der*, *die* ili *das*.
*   **Deklinacija kroz padeže:** Automatski generiše oblike za Nominativ, Genitiv, Dativ i Akuzativ, uključujući i pokazne zamenice (*dieser*).
*   **Pametna Množina:** Predviđa oblike množine na osnovu gramatičkih pravila nemačkog jezika.
*   **Audio Izgovor:** Integrisana glasovna podrška koja izgovara reči na čistom nemačkom jeziku.
*   **Dinamički dizajn:** Pozadina aplikacije se menja u zavisnosti od roda reči (Plava za muški, Roze za ženski, Zelena za srednji rod) radi lakšeg pamćenja.

## 🛠️ Tehnologije
*   **Backend:** Python & Flask
*   **Frontend:** HTML5, CSS3 (Glassmorphism dizajn), JavaScript
*   **API integracije:** Deep Translator (Google) & MyMemory API

---

## 📦 Instalacija i Pokretanje

1.  **Kloniraj repozitorijum:**
    ```bash
    git clone https://github.com/tvoj-username/nemacki-master.git
    cd nemacki-master
    ```

2.  **Instaliraj potrebne biblioteke:**
    ```bash
    pip install flask requests deep-translator
    ```

3.  **Pokreni aplikaciju:**
    ```bash
    python app.py
    ```

4.  **Pristupi aplikaciji:**
    Otvori brauzer i idi na `[http://127.0.0.1:5000](http://127.0.0.1:5000)`

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
    └── index.html        # HTML interfejs sa Jinja2 šablonima
