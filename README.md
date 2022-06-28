
# 🍌 Banana Serverless

This repo gives a basic framework for serving ML models in production using simple HTTP servers.

## Quickstart:

The repo is already set up to run a basic [HuggingFace BERT](https://huggingface.co/docs/transformers/model_doc/bert) model.
1. Run `pip3 install -r requirements.txt` to download dependencies.
2. Run `python3 server.py` to start the server.
3. Run `python3 test.py` in a different terminal session to test against it.

## Make it your own:

1. Edit `app.py` to load and run your model.
2. Make sure to test with `test.py`!

if deploying using Docker:

3. Edit `download.py` (or the `Dockerfile` itself) with scripts download your custom model weights at build time.

## Move to prod:

At this point, you have a functioning http server for your ML model. You can use it as is, or package it up with our provided `Dockerfile` and deploy it to your favorite container hosting provider!

If Banana is your favorite GPU hosting provider (and we sure hope it is), read on!

# 🍌

# Deploy to Banana Serverless:

Four steps:
1. Create your own copy of this template repo. Either:
- Click "[Fork](https://github.com/bananaml/serverless-template/fork)" (creates a public repo)
- Click "[Use this Template](https://github.com/bananaml/serverless-template/generate)" (creates a private or public repo)
- Create your own repo and copy the template files into it

2. Install the [Banana Github App](https://github.com/apps/banana-serverless) to your new repo.

3. Get your Banana API Key by [logging in here](https://app.banana.dev).

4. Email us at `onboarding@banana.dev` with the following message:

```
Hello, I'd like to be onboarded to serverless.
My github username is: YOUR_GITHUB_USERNAME
My Banana API Key is: YOUR_API_KEY
My preferred billing email is: YOU@EMAIL.COM
```
Your github username, banana api key, and email are required for us to authorize you into the system.
We will reply and confirm when you're added.
<br>

From then onward, any pushes to the default repo branch (usually "main" or "master") trigger Banana to build and deploy your server, using the Dockerfile.
Throughout the build we'll sprinkle in some secret sauce to make your server extra snappy 🔥

It'll then be deployed on our Serverless GPU cluster and callable with any of our serverside SDKs:

- [Python](https://github.com/bananaml/banana-python-sdk)
- [Node JS / Typescript](https://github.com/bananaml/banana-node-sdk)
- [Go](https://github.com/bananaml/banana-go)

You can monitor the progress of builds by running a cURL to our logs API:<br>
```bash
curl -X POST -H "Content-Type: application/json" -d '{"apiKey":"YOUR_API_KEY"}' https://logs.banana.dev | json_pp

```

Once you receive your modelKey from the first build, you can add the optional "modelKey" value to the curl json to filter the return down to a single model.<br>
```bash
curl -X POST -H "Content-Type: application/json" -d '{"apiKey":"YOUR_API_KEY", "modelKey":"YOUR_MODEL_KEY"}' https://logs.banana.dev | json_pp

```

<br>

## Use Banana for scale.
