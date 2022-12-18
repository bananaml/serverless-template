# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

from transformers import pipeline
import os

def download_model():

    # In this example, we get the model name as an ENV variable defined in the Dockerfile
    hf_model_name = os.getenv("HF_MODEL_NAME")
    
    # do a dry run of loading the huggingface model, which will download weights
    pipeline('fill-mask', model=hf_model_name)

if __name__ == "__main__":
    download_model()