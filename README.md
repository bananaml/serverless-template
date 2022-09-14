
# 🍌 Banana Serverless

This repo gives a framework to serve ML models in production using simple HTTP servers.

To generalize this to deploy anything on Banana, [see the guide here](https://www.notion.so/banana-dev/How-To-Serve-Anything-On-Banana-125a65fc4d30496ba1408de1d64d052a).

# 1. Download
Choose 1 of 3 options
- [Fork this repo](https://github.com/bananaml/serverless-template/fork) to create a public install
- [Use this Template](https://github.com/bananaml/serverless-template/generate) to creates a private or public install
- Create your own repo and copy the template files from here this repo into yours

Then clone the repo to a machine with a GPU to install + test it locally 

# 2. Install
The repo default runs a [HuggingFace BERT](https://huggingface.co/docs/transformers/model_doc/bert) model.

1. Run `pip3 install -r requirements.txt` to download dependencies.
2. Run `python3 server.py` to start the server.
3. Run `python3 test.py` in a different terminal session to test an inference against it.

# 3. Make it your own

1. Edit `app.py` to load and run your model.
2. Make sure to test with `test.py`!
3. When ready to deploy:
  - edit `download.py` (or the `Dockerfile` itself) with scripts download your custom model weights at build time
  - edit `requirements.txt` with your pip packages. Don't delete the "sanic" line, as it's a banana dependency.

# 4. Ship to prod

You now have a functioning http server that should work using Docker and complete inferences on a GPU
To deploy on banana
- Log in to the [Banana App](https://app.banana.dev)
- Connect your github
- Select this repository

It'll then be built from the dockerfile, optimized, then deployed on our Serverless GPU cluster!
You can then call it with any of our SDKs
- [Python](https://github.com/bananaml/banana-python-sdk)
- [Node JS / Typescript](https://github.com/bananaml/banana-node-sdk)
- [Go](https://github.com/bananaml/banana-go)

<br>

## Use Banana for scale.
