from transformers import pipeline
import torch
import os

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model

    # In this example, we get the model name as an ENV variable defined in the Dockerfile
    hf_model_name = os.getenv("HF_MODEL_NAME")
    
    device = 0 if torch.cuda.is_available() else -1
    model = pipeline('fill-mask', model=hf_model_name, device=device)

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    if prompt == None:
        return {'message': "No prompt provided"}
    
    # Run the model
    result = model(prompt)

    # Return the results as a dictionary
    return result
