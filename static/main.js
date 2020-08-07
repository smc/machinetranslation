
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
}