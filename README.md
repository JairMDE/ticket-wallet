# Ticket-Wallet

## Introduction 
This application provides an OCR (Optical Character Recognition) service, allowing users to upload their receipts, and get back the products and prices that were spent on that specific date. 

## Installation
To install and get the app to function you can follow these steps:
- Clone the repository and switch to the branch called `Cynthia/DBM`.
- Make sure you have Postman installed as well as Docker and Docker compose.

## Features
- Extract text from images using OCR.
- Easy Deployment with Docker Compose.
- Supports images in base64 format sent as JSON (this in Postman).

## Dependencies
The `requirements.txt` will work, when building the docker-compose, as a caller to make the installation of all the used libraries and dependencies.

This includes:
- Flask
- Numpy
- OpenCV - Python
- Pillow
- Pytesseract

There are also some dependencies for the OCR:
- ffmpeg
- libsm6
- libxext6
- tesseract-ocr

### Reminder: You do not have to install these, when building the docker-compose, it will gather the installations automatically. 

# Docker Compose (building and running the app)
1. Navigate to the application directory.
2. Run `docker compose up --build`, you will see the Docker container building and it would look like this:
![image](https://github.com/JairMDE/ticket-wallet/assets/73959705/cd534c92-06ee-4956-b9ea-a60410cae21b)

3. Then you will have an output giving you two addresses, but you will choose the first one:


<img width="961" alt="Screenshot 2024-02-26 at 8 01 40 p m" src="https://github.com/JairMDE/ticket-wallet/assets/73959705/27310cd8-2716-4cda-9899-247b987e2389">



Copy that address and copy it in the Postman application. You have to click on new, the HTTP, and paste the address.


After that, you will have to change from GET to POST and add after the address `/image2text`. 


<img width="995" alt="Screenshot 2024-02-26 at 8 08 06 p m" src="https://github.com/JairMDE/ticket-wallet/assets/73959705/c7206fef-17f8-4066-b9c4-77946319da2b">




Then you should go to the space `body` in Postman and click on `raw` so you can input the image in the base64 format and make the JSON.

# Test the service 

To test the output, for now, you have to input an image in base64 format. 
Construct a JSON object with the key `img` and the base64 string as the value. 
Example for any image:
`{"img": "base64EncodedImageString"}`

The output should look like this after pasting the string.


![image](https://github.com/JairMDE/ticket-wallet/assets/73959705/a1522e38-f3ce-4eda-803d-1aed13187016)


This is an example of a base64 string image, just for testing the service:
[b64.txt](https://github.com/JairMDE/ticket-wallet/files/14413444/b64.txt)
