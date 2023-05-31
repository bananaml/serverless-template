# Must use a Cuda version 11+
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /

# Install git
RUN apt-get update && apt-get install -y git

# Install python packages
RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# We add the banana boilerplate here
COPY server.py .

# Add your model weight files 
# (in this case we have a python script)
COPY download.py .
RUN python3 download.py


# Add your custom app code, init() and inference()
COPY app.py .

EXPOSE 8000

CMD python3 -u server.py
