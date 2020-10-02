import os
import sys

import regex
from flask import Flask, jsonify, render_template, request
from transformers import MarianMTModel, MarianTokenizer

os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = Flask(
    __name__
)

models={}
tokenizers={}

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
    tgt_text = translate(source_lang, target_lang, src_text)
    return jsonify(translation=tgt_text)

def translate(source_lang, target_lang, src_text):
    global models, tokenizers
    model = models.get("{0}-{1}".format(source_lang, target_lang))
    if not model:
        init()
        model = models.get("{0}-{1}".format(source_lang, target_lang))
    tokenizer = tokenizers.get("{0}-{1}".format(source_lang, target_lang))
    translated = model.generate(**tokenizer.prepare_seq2seq_batch(src_text))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return "\n".join(tgt_text)

def getModel(model="en-ml"):
    model_name = "Helsinki-NLP/opus-mt-{0}".format(model)
    print('Preparing model %s' % model_name )
    return MarianMTModel.from_pretrained(model_name)

def getTokenizer(model="en-ml"):
    model_name = "Helsinki-NLP/opus-mt-{0}".format(model)
    return MarianTokenizer.from_pretrained(model_name)

def init():
    global models, tokenizers
    models = {"en-ml": getModel("en-ml"), "ml-en": getModel("ml-en")}
    tokenizers = {"en-ml": getTokenizer("en-ml"), "ml-en": getTokenizer("ml-en")}

if __name__ == "__main__":
    init()

