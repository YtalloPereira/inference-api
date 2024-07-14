#!/bin/bash

# Update system

sudo yum update -y

# Install docker

sudo yum install docker -y

# Start docker service

sudo service docker start

# Start container with docker image hosted on Docker Hub

sudo docker run -d -p 80:8000 inference/image:latest
