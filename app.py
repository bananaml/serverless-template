import spacy

import codecs
import sys
import os

import json
import glob
import regex

import urllib.request

class MultiModel:
    MODELS_URL = "https://raw.githubusercontent.com/explosion/spacy-models/master/compatibility.json"

    def __init__(self):
        self.data = {}
        self.models = self.find_models()

    def find_models(self):
        version = ".".join(spacy.__version__.split(".")[0:2])
        with urllib.request.urlopen(self.MODELS_URL) as file:
            compatibility = json.load(file)
            model_pattern = regex.compile('^[a-z]{2}_core_(web|news)_sm')
            all_models = compatibility['spacy'][version].keys()
            good_models = [model for model in all_models if model_pattern.match(model)]
            self.model_dictionary = { model[0:2] : model for model in good_models }

            # print("Supported languages: {}".format(" ".join(model_dictionary.keys())))
            return self.model_dictionary

    def print_languages(self):
        print("Supported languages: {}".format(" ".join(self.model_dictionary.keys())))

    def model(self, language):
        if self.models.get(language) == None:
            print("Language {} not supported".format(language))
            return;

        if self.data.get(language) == None:
            self.load_model(language)

        return self.data.get(language)

    def download_model(self, language):
        print("Loading language {}".format(language))
        model = self.models.get(language)
        command = "python3 -m spacy download {}".format(model)
        print("Downloading model:\n{}".format(command))
        os.system(command)

    def load_model(self, language):
        model = self.models.get(language)
        self.data[language] = spacy.load(model)

        return self.data[language]

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    language = os.environ['LEMMATIZE_LANGUAGE']
    multimodel = MultiModel()
    model = multimodel.model(language)

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    if prompt == None:
        return {'message': "No prompt provided"}

    raw_output = []
    doc = model(prompt)

    for word in doc:
        word_data = {}
        word_data['token'] = word.text
        word_data['lemma'] = word.lemma_
        word_data['pos'] = word.pos_
        word_data['tag'] = word.tag_
        word_data['dep'] = word.dep_
        word_data['shape'] = word.shape_
        word_data['alpha'] = word.is_alpha
        word_data['stop'] = word.is_stop
        word_data['lowercased'] = word.lower_
        word_data['normalized'] = word.norm_
        word_data['probability'] = word.prob
        word_data['oov'] = word.is_oov
        raw_output.append(word_data)

    return { 'result': raw_output }
