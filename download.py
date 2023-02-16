# In this file, we define download_model
# It runs during container build time to get model weights built into the container

#!/usr/bin/env python3

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

multimodel = MultiModel()
language = os.environ["LEMMATIZE_LANGUAGE"]

multimodel.print_languages()
model = multimodel.download_model(language)
