# English Malayalam machine translation system

https://translate.smc.org.in/

This system uses huggingface transformers with NLLB language models for translation.

Currently the api from https://huggingface.co/spaces/santhosh/NLLB-Translator/ is used. But the repository
also contains a python flask server to run the model from a local machine, assuming it has enough RAM and processing capacity.

## How to use

In a virtual environment,

```
pip install -r requirements.txt
gunicorn -w 4 translate:app
```
