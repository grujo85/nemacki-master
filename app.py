from flask import Flask, render_template, request
import requests
from deep_translator import GoogleTranslator

app = Flask(__name__)

def generisi_padeze(clan, de_rec):
    if not clan: return None
    
    zamenice = {
        "der": {"Nom": "dieser", "Gen": "dieses", "Dat": "diesem", "Aku": "diesen"},
        "die": {"Nom": "diese", "Gen": "dieser", "Dat": "dieser", "Aku": "diese"},
        "das": {"Nom": "dieses", "Gen": "dieses", "Dat": "diesem", "Aku": "dieses"}
    }
    
    z = zamenice[clan]
    s_nastavak = "es" if len(de_rec) <= 4 or de_rec.endswith(('s', 'ss', 'sch', 'z', 'x')) else "s"
    if de_rec.endswith('e'): s_nastavak = "s"

    if clan == "die":
        return {
            "Nominativ": f"die {de_rec} / {z['Nom']} {de_rec}",
            "Genitiv": f"der {de_rec} / {z['Gen']} {de_rec}",
            "Dativ": f"der {de_rec} / {z['Dat']} {de_rec}",
            "Akuzativ": f"die {de_rec} / {z['Aku']} {de_rec}"
        }
    else:
        return {
            "Nominativ": f"{clan} {de_rec} / {z['Nom']} {de_rec}",
            "Genitiv": f"des {de_rec}{s_nastavak} / {z['Gen']} {de_rec}{s_nastavak}",
            "Dativ": f"dem {de_rec} / {z['Dat']} {de_rec}",
            "Akuzativ": f"{'den' if clan == 'der' else 'das'} {de_rec} / {z['Aku']} {de_rec}"
        }

def generisi_mnozinu(clan, de_rec):
    if de_rec.endswith('e'): return de_rec + "n"
    if de_rec.endswith(('ung', 'heit', 'keit', 'ion', 'tät')): return de_rec + "en"
    if de_rec.endswith('er') and clan == 'der': return de_rec
    return de_rec + "e"

def nabavi_podatke(sr_rec):
    sr_rec = sr_rec.lower().strip()
    try:
        prevod_raw = GoogleTranslator(source='sr', target='de').translate(f"taj {sr_rec}")
        de_rec = prevod_raw.split()[-1].strip().capitalize()
        
        clan = ""
        if de_rec.endswith(('e', 'ung', 'heit', 'keit', 'schaft', 'ion', 'tät')): clan = "die"
        elif de_rec.endswith(('ismus', 'ant', 'ent', 'ling')): clan = "der"
        elif de_rec.endswith(('um', 'ment', 'chen', 'lein')): clan = "das"

        if not clan:
            res = requests.get(f"https://api.mymemory.translated.net/get?q=taj {sr_rec}&langpair=sr|de", timeout=5).json()
            full = res['responseData']['translatedText'].lower()
            if any(x in full.split() for x in ['der', 'dieser']): clan = "der"
            elif any(x in full.split() for x in ['die', 'diese']): clan = "die"
            elif 'das' in full or 'dieses' in full: clan = "das"

        if not clan: clan = "der"
        
        padezi = generisi_padeze(clan, de_rec)
        return {
            "sr": sr_rec, 
            "de": de_rec, 
            "clan": clan,
            "padezi": padezi, 
            "mnozina": generisi_mnozinu(clan, de_rec),
            "primer": f"Ich brauche {padezi['Akuzativ'].split(' / ')[0]}."
        }
    except: 
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    rezultat = None
    if request.method == "POST":
        rec = request.form.get("rec")
        if rec: 
            rezultat = nabavi_podatke(rec)
    return render_template("index.html", rezultat=rezultat)

if __name__ == "__main__":
    app.run(debug=True)
