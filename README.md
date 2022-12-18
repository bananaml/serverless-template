
# 🍌 Banana Serverless

This repo gives a framework to serve ML models in production using simple HTTP servers.

# Quickstart
**[Follow the quickstart guide in Banana's documentation to use this repo](https://docs.banana.dev/banana-docs/quickstart).** 

*(choose "GitHub Repository" deployment method)*

<br>

# Helpful Links
Understand the 🍌 [Serverless framework](https://docs.banana.dev/banana-docs/core-concepts/inference-server/serverless-framework) and functionality of each file within it.

Generalize this framework to [deploy anything on Banana](https://docs.banana.dev/banana-docs/resources/how-to-serve-anything-on-banana).

<br>

# Local testing

## With docker

To test the Serverless Framework with docker locally, you need to build the docker container and then run it.
In the root of this directory, run:
```
docker build . -t serverless-template
```
After which you can run the container. Here we also forward the port to access the localhost url outside of the
container and enable gpu acceleration.

```
docker run serverless-template -p 8000:8000 --gpus
```

## Without docker

Testing your code without docker is straight forward. Remember to pass in the Hugging Face model name as 
an ENV variable. In this case:
```
export HF_MODEL_NAME=bert-base-uncased
```

And then simply run the server.py
```
python3 server.py
```

<br>

## Use Banana for scale.
