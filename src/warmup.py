# In this file, we define load_model
# It runs once at server startup to load the model to a GPU

# In this example: A Huggingface BERT model

from transformers import pipeline

def load_model():

    # load the model from cache or local file to the CPU
    model = pipeline('fill-mask', model='bert-base-uncased', device=0)

    # transfer the model to the GPU
    # N/A for this example, it's already on the GPU

    # return the callable model
    return model