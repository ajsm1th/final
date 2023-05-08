# Azure Cognitive Service | Computer Vision API 
Optical character recognition, using Python with help of Azure Cognitive Service | Computer Vision API
Currently this code only works for images located on a web server.

What is Optical Character Recognition?
Optical Character Recognition (OCR) is the process of detecting and reading text in images through computer vision.

![final pic6](https://user-images.githubusercontent.com/122126853/236873381-2d2aa774-b175-4b8a-830b-3fa23382d85b.JPG)


How does OCR work?
OCR algorithms can be based on traditional image processing and machine learning-based approaches or deep learning-based methods.
Traditional Approaches to OCR go through a series of pre-processing steps where the inspected document is cleaned and made noise-free. Following this, the document is binarized for subsequent contour detection to aid in the detection of lines and columns.

![final pic5](https://user-images.githubusercontent.com/122126853/236874449-a20f4cf0-30b5-47ad-aa0f-c1ef1696cef4.JPG)

ref: https://www.v7labs.com/blog/ocr-guide

I used a Digital Ocean to create a droplet to run tests and check for functionality.


# Try Out

The server endpoint is 
http://134.209.113.53:5000

API Endpoint
http://134.209.113.53:5000/api/v1/read

Post Request Body
{"url":"<The url you would like the text converted from goes here>"}

Please configure Postman with your content-type as application/json.
Please make sure "raw" is selected in the menu


![final pic1](https://user-images.githubusercontent.com/122126853/236354162-d9eb5154-caac-40b2-bb51-f9ec9485e7a7.JPG)

The result will be displayed in the bottom section of Postman.

# Possible Response Codes

Response code	Description
200		OK
400		Input Validation Failed
500		Internal Server Error


There are several choices for how you would like your data to be returned.  The choices are JSON, XML, HTML, Text, or Auto
For this example I have chosen JSON.  To change the result just change what you have chosen from the drop down.  There is no need to resubmit your request.

![Final pic2](https://user-images.githubusercontent.com/122126853/236354814-b7b71f2c-bce8-42a8-953c-72cf47ac6a55.JPG)

In this image you can see the url you submitted.
The contect-type you are using 
The text in the url you have submitted.

To change your request put in the url for what you would like analyzed.
Such as "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/printed_text.jpg"
which returns the following (this is what the HTML return would look like)

![Final pic3](https://user-images.githubusercontent.com/122126853/236356800-18b57918-7b77-4240-96c9-4468f520234c.JPG)

This is what the JSON return looks like

![final pic4](https://user-images.githubusercontent.com/122126853/236357032-ca951f16-237f-42da-a12d-ac567091d805.JPG)


Example entries if you would like to try:

https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/handwritten_text.jpg
https://imgv3.fotor.com/images/blog-richtext-image/How-to-Make-Text-Stand-Out-And-More-Readable.jpg

Or choose your own image with text.
