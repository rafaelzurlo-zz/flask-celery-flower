# POC flask with worker background (Flask, Celery and Flower)

## Dependencies

In order to build and run the application you need to have Docker installed and running in your machine: [Install docker](https://docs.docker.com/install/)

## Setup:

## Application setup
#### Create the containers web / celery / flower
`$ docker-compose build`

#### Set the container up web
`$ docker-compose up web`

### The application will start at `localhost:5000` \o/
### The flower will start at `localhost:5555` \o/
