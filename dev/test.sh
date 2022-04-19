#!/bin/bash
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Hello I am a [MASK] model."}' http://localhost:8000/