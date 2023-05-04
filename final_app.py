# IMPORTS
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import time, json, os
from flask import Flask, request, jsonify

# CONSTANTS
SUBSCRIPTION_KEY = "f9ddbc5aa459428499ff21edcb0d7dfa"
ENDPOINT = "https://computer-vision-api-final.cognitiveservices.azure.com/"
APP = Flask(__name__)

# FUNCTIONS
def callComputerVisionAPI_url(_url):
    # Create result
    _result = {'url': _url,
               'Content-type': 'application/json'}
    
    # Create Computer Vision Object
    cvClient = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(SUBSCRIPTION_KEY))
    
    # Call API with URL and raw response (allows you to get the operation location)
    readResponse = cvClient.read(_url,  raw=True)

    # Check to make sure Call was Successful
    
    
    if readResponse.response.status_code in [200, 201, 202]:
        opId = readResponse.headers["Operation-Location"].split("/")[-1]
        _result['statusCode'] = readResponse.response.status_code
    else:
        _result['statusCode'] = readResponse.response.status_code
        return json.dumps(_result)
    
    # Call get_read_result until result is received.
    while True:
        readResult = cvClient.get_read_result(opId)
        if readResult.status == OperationStatusCodes.succeeded:
            _result['text'] = []
            for text_result in readResult.analyze_result.read_results:
                for line in text_result.lines:
                    _result['text'].append(line.text)
            break
        elif readResult.status == OperationStatusCodes.failed:
            _result['text'] = ["Operation Failed!"]
        elif readResult.status == OperationStatusCodes.not_started or OperationStatusCodes.running:
            # Sleep for 1 second and check again
            time.sleep(1)
        else:
            break

    return json.dumps(_result)

def callComputerVisionAPI_img(_imageToProcess):
    # Create result
    _result = {'url': "",
               'Content-type': 'image/json'}
    
    # Create Computer Vision Object
    cvClient = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(SUBSCRIPTION_KEY))

    # Call API with URL and raw response (allows you to get the operation location)
    with open(os.path.join("/root/FINAL/final/images", _imageToProcess)) as image_stream:
        readResponse = cvClient.recognize_printed_text_in_stream(   image=image_stream,
                                                                    language="en")

    # Check to make sure Call was Successful
    
    if readResponse.response.status_code in [200, 201, 202]:
        opId = readResponse.headers["Operation-Location"].split("/")[-1]
        _result['statusCode'] = readResponse.response.status_code
    else:
        _result['statusCode'] = readResponse.response.status_code
        return json.dumps(_result)
    
    # Call get_read_result until result is received.
    while True:
        readResult = cvClient.get_read_result(opId)
        if readResult.status == OperationStatusCodes.succeeded:
            _result['text'] = []
            for text_result in readResult.analyze_result.read_results:
                for line in text_result.lines:
                    _result['text'].append(line.text)
            break
        elif readResult.status == OperationStatusCodes.failed:
            _result['text'] = ["Operation Failed!"]
        elif readResult.status == OperationStatusCodes.not_started or OperationStatusCodes.running:
            # Sleep for 1 second and check again
            time.sleep(1)
        else:
            break

    return json.dumps(_result)

@APP.route('/read', methods=['POST'])
def read():

    if request.headers['Content-type'] == 'application/json':
        _record = json.loads(request.data)
        _url = _record['url']
        result = callComputerVisionAPI_url(_url)
        return result
    elif 'multipart/form-data' in request.headers['Content-type']:
        if request.files:
            image = request.files["imagename"]
            print(image.mimetype)
            image.save(os.path.join("/root/FINAL/final/images", image.filename))
            result = callComputerVisionAPI_img(image.filename)
            return result

    

    
    return {}
    

def main():
    # Create Flask App to Answer API calls
    APP.run(host='0.0.0.0')

    # read_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/printed_text.jpg"

    # result = callComputerVisionAPI(read_image_url)
    # print(result)
# MAIN
if __name__ == "__main__":
    
    main()