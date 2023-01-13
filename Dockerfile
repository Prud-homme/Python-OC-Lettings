# pull official base image
FROM python:3.11.0-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# expose port 8000
EXPOSE 8000

# create and set work directory
ADD . /oc_lettings/
WORKDIR /oc_lettings

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run gunicorn
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT