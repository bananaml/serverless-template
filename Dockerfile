FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-devel

WORKDIR /

# Install git
RUN apt-get update && apt-get install -y git

# Install python packages
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add your model weight files 
# (in this case we have a python script)
ADD src/download.py .
RUN python3 download.py

ADD src/ .

EXPOSE 8000

CMD python3 -u app.py