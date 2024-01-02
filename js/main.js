function doTranslate(from, to) {
    document.getElementById('progress').style.display = "block";
    document.getElementById(`${to}_content`).innerText = '';
    const content = document.getElementById(`${from}_content`).value;
    fetch(`https://translate.wmcloud.org/api/translate`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            source_language: from,
            target_language: to,
            format: 'text',
            content: content
        })
    }).then(response => {
        if (!response.ok) {
            throw new Error('Server returned ' + response.status);
        }
        return response.json();
    }).then(result => {
        document.getElementById(`${to}_content`).innerText = result.translation
        document.getElementById('progress').style.display = "none";
    })
    .catch(error => {
        // Error handling
        console.error('An error occurred:', error);
        // Display an error message to the user
        document.getElementById('status').innerText = 'An error occurred. Please try again.';
    }).finally(()=>{
        document.getElementById('progress').style.display = "none";
    });
}
