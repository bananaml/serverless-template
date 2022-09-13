
# 🍌 Banana Serverless

This repo gives a basic framework for serving ML models in production using simple HTTP servers.

If you want to generalize this to deploy anything on Banana, [see the guide here](https://www.notion.so/banana-dev/How-To-Serve-Anything-On-Banana-125a65fc4d30496ba1408de1d64d052a).

## Quickstart:

The repo is already set up to run a basic [HuggingFace BERT](https://huggingface.co/docs/transformers/model_doc/bert) model.
1. Run `pip3 install -r requirements.txt` to download dependencies.
2. Run `python3 server.py` to start the server.
3. Run `python3 test.py` in a different terminal session to test against it.

## Make it your own:

1. Edit `app.py` to load and run your model.
2. Make sure to test with `test.py`!
3. When ready to deploy:
  - edit `download.py` (or the `Dockerfile` itself) with scripts download your custom model weights at build time
  - edit `requirements.txt` with your pip packages. Don't delete the "sanic" line, as it's a banana dependency.

## Move to prod:

At this point, you have a functioning http server for your ML model. You can use it as is, or package it up with our provided `Dockerfile` and deploy it to your favorite container hosting provider!

If Banana is your favorite GPU hosting provider (and we sure hope it is), read on!

# 🍌

# Deploy to Banana Serverless:

- Log in to the [Banana App](https://app.banana.dev)
- Select your customized repo for deploy!

It'll then be built from the dockerfile, optimized, then deployed on our Serverless GPU cluster and callable with any of our SDKs:

- [Python](https://github.com/bananaml/banana-python-sdk)
- [Node JS / Typescript](https://github.com/bananaml/banana-node-sdk)
- [Go](https://github.com/bananaml/banana-go)

You can monitor buildtime and runtime logs by clicking the logs button in the model view on the Banana Dashboard](https://app.banana.dev)

<br>

## Use Banana for scale.
