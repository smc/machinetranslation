function doTranslate(from, to) {
    document.getElementById('progress').style.display = "block";
    document.getElementById(`${to}_content`).innerText = '';
    fetch(`https://translate.wmcloud.org/api/translate/${from}/${to}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: document.getElementById(`${from}_content`).value
        })
    }).then(response => response.json())
        .then(result => {
            document.getElementById(`${to}_content`).innerText = result.translation
            document.getElementById('progress').style.display = "none";
        })
}
