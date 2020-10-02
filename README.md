# English Malayalam machine translation system

https://translate.smc.org.in/

This system uses huggingface transformers with OpusMT language models for translation.

## How to use

In a virtual environment,

```
pip install -r requirements.txt
gunicorn -w 4 translate:app
```
