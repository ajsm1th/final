# Azure Cognitive Service | Computer Vision API 
Optical character recognition, using Python with help of Azure Cognitive Service | Computer Vision API
Currently this code only works for images located on a web server.

I used Digital Ocean to create a virtual server to host my code.
Postman will be needed to use the code for read as I did not create an application for a front end.

Please configure Postman with your content-type as application/json.
Choose POST from the drop down
your post will go to http://134.209.113.53:5000 which is my Digital Ocean virtual server.  It is listening on port 5000.
This will be a read request so please add /read to the end of your post.
Please make sure "Body" is selected in the menu
Please make sure "raw" is selected in the menu

Put the URL you would like to analyze into the request.

![final pic1](https://user-images.githubusercontent.com/122126853/236354162-d9eb5154-caac-40b2-bb51-f9ec9485e7a7.JPG)

The result will be displayed in the bottom section of Postman.

There are several choices for how you would like your data to be returned.  The choices are JSON, XML, HTML, Text, or Auto
For this example I have chosen JSON.  To change the result just change what you have chosen from the drop down.  There is no need to resubmit your request.

![Final pic2](https://user-images.githubusercontent.com/122126853/236354814-b7b71f2c-bce8-42a8-953c-72cf47ac6a55.JPG)

In this image you can see the url you submitted.
The contect-type you are using 
The text in the url you have submitted.

To change your request put in the url for what you would like analyzed.
Such as "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/printed_text.jpg"
which returns

