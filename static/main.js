/*
function doTranslate(from, to) {
    document.getElementById('progress').style.display = "block";
    fetch('/api/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            from,
            to,
            text: document.getElementById('source_content').value
        })
    }).then(response => response.json())
        .then(result => {
            document.getElementById('target_content').innerText = result.translation
            document.getElementById('progress').style.display = "none";
        })
}*/

function doTranslate(from, to) {
    document.getElementById('progress').style.display = "block";

    const lang_map = {
        "en": 'eng_Latn',
        "ml": 'mal_Mlym'
    }
    const text = document.getElementById('source_content').value;
    const payload = {
        data : [text, lang_map[from], lang_map[to], 1000]
    }
    fetch('https://santhosh-nllb-translator.hf.space/api/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    }).then(response => response.json())
        .then(result => {
            console.dir(result);
            document.getElementById('target_content').innerText = result.data[0]
            document.getElementById('progress').style.display = "none";
        })
}