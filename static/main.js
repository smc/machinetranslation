function doTranslate(from, to) {
    document.getElementById('progress').style.display = "block";
    fetch(`https://translate.wmcloud.org/api/translate/${from}/${to}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: document.getElementById('source_content').value
        })
    }).then(response => response.json())
        .then(result => {
            document.getElementById('target_content').innerText = result.translation
            document.getElementById('progress').style.display = "none";
        })
}
