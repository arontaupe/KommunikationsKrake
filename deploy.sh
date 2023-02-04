#!/bin/zsh
# this script should take changes made to the github repo and automatically deploy them to the Ällei Server.


# Text Color Variables
GREEN='\033[32m' # Green
CLEAR='\033[0m'  # Clear color and formatting


build-docker() {
    docker-compose build 
    docker push arontaupe/allei   
    #docker-compose up
    echo -e "${GREEN}PLEASE CHECK THE FUNCTIONALITY OF THE DOCKER CONTAINER. This script does none of the checking for you. ${CLEAR}"
    read -p "Press any key to continue if the check is clear... " -n1 -s
    gcloud run deploy
    }

build-docker