import os
import torch
from flask import Flask, jsonify, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = Flask(
    __name__
)

model=None
tokenizer=None
device = 0 if torch.cuda.is_available() else -1
TASK = "translation"
MODEL = "facebook/nllb-200-distilled-600M"

lang_map = {
    "en": 'eng_Latn',
    "ml": 'mal_Mlym'
}

@app.route("/", defaults={"path": ""})
def index(path):
    return render_template("index.html",)

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


@app.route("/api/translate", methods=["POST", "GET"])
def do_translate():
    text = None
    source_lang = "en"
    target_lang = "ml"
    if request.method == "POST":
        text = request.json.get("text")
        source_lang = request.json.get("from")
        target_lang = request.json.get("to")
    else:
        text = request.args.get("text")
        source_lang = request.args.get("from")
        target_lang = request.args.get("to")
    src_text = text.strip().splitlines()
    tgt_text = translate(lang_map[source_lang], lang_map[target_lang], src_text)
    return jsonify(translation=tgt_text)

def translate(src_lang, tgt_lang, src_text):
    """
    Translate the text from source lang to target lang
    """
    global model, tokenizer
    TASK = "translation"
    if not model:
        init()
    translation_pipeline = pipeline(TASK,
                                    model=model,
                                    tokenizer=tokenizer,
                                    src_lang=src_lang,
                                    tgt_lang=tgt_lang,
                                    max_length=1000,
                                    device=device)

    result = translation_pipeline(src_text)
    return result[0]['translation_text']

def getModel():
    print('Preparing model %s' % MODEL )
    return AutoModelForSeq2SeqLM.from_pretrained(MODEL)

def getTokenizer():
    return AutoTokenizer.from_pretrained(MODEL)

def init():
    global model, tokenizer
    model = getModel()
    tokenizer = getTokenizer()

if __name__ == "__main__":
    init()

