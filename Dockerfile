FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime

WORKDIR /

# nvidia rotated their GPG keys so need to refresh them 
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list

# Install git
RUN apt-get update && apt-get install -y git

# Install python packages
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add your model weight files 
# (in this case we have a python script)
ADD download.py .
RUN python3 download.py

# Add your custom app code, init() and inference()
ADD app.py .

EXPOSE 8000

CMD python3 -u app.py
