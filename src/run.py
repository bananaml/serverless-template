# In this file, we define run_model
# It runs every time the server is called

# In this example: A Huggingface BERT model

def run_model(model, prompt):

    # do preprocessing
    # N/A for this example

    # run the model
    result = model(prompt)

    # do postprocessing
    # N/A for this example

    return result