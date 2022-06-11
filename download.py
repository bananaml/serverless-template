# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

from transformers import pipeline

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    pipeline('fill-mask', model='bert-base-uncased')

if __name__ == "__main__":
    download_model()