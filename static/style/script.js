let germanVoice = null;

function loadVoices() {
    let voices = window.speechSynthesis.getVoices();
    germanVoice = voices.find(v => v.lang === 'de-DE' || v.lang.includes('de_DE'));
    if (!germanVoice) germanVoice = voices.find(v => v.lang.includes('de'));
}

window.speechSynthesis.onvoiceschanged = loadVoices;
loadVoices();

function speak(word) {
    window.speechSynthesis.cancel();
    if (!word) return;
    let msg = new SpeechSynthesisUtterance(word);
    msg.lang = 'de-DE';
    msg.rate = 0.85;
    if (germanVoice) msg.voice = germanVoice;

    const btn = document.getElementById('audioBtn');
    if (btn) {
        btn.style.transform = "scale(1.2)";
        setTimeout(() => btn.style.transform = "scale(1)", 200);
    }
    window.speechSynthesis.speak(msg);
}

document.body.addEventListener('click', function() {
    window.speechSynthesis.speak(new SpeechSynthesisUtterance(""));
}, { once: true });
