from sentence_transformers import SentenceTransformer


# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    model = SentenceTransformer("sentence-transformers/paraphrase-mpnet-base-v2")


# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs: dict) -> dict:
    global model

    # Parse out your arguments
    prompt = model_inputs.get("prompt", None)
    if prompt == None:
        return {"message": "No prompt provided"}

    # Run the model
    result = model.encode(prompt)

    # Return the results as a dictionary
    return { "data": result }
