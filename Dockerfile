FROM python:3
ADD . /oc_lettings/
WORKDIR /oc_lettings
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .