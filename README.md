# Image-to-text-API
How to run the server:

python server.py

API Endpoint:

https://image-to-text-api.onrender.com

how to call:

make a POST request to '/' route with parameter 'file' or 'url'.If you are selecting an image from localstorage then use 'file' as key and image as value in form-data in postman.If you are using url them use 'url' parameter and give url in params in postman.

Resources used:

The API uses Azure image-to-text python SDK for detecting the text in the image.The API takes images through a POST request either from local storage or url then process the image the image and returns the text which is on the image.
