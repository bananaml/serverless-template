from potassium import Potassium, Request, Response

from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize

app = Potassium("my_app")

# @app.init runs at startup, and loads models into the app's context
@app.init
def init():
    model = SentenceTransformer("sentence-transformers/paraphrase-mpnet-base-v2")
   
    context = {
        "model": model
    }

    return context

# @app.handler runs for every call
@app.handler()
def handler(context: dict, request: Request) -> Response:
    prompt = request.json.get("prompt")
    model = context.get("model")
    # Run the model
    sentence_embeddings = model.encode(prompt)
    normalized_embeddings = normalize(sentence_embeddings)

    # Convert the output array to a list
    output = normalized_embeddings.tolist()

    return Response(
        json = {"data": output}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()