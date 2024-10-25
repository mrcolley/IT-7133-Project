from google.cloud import vision
from google.oauth2 import service_account

def perform_ocr(image_path):
    credentials = service_account.Credentials.from_service_account_file('credentials.json')
    client = vision.ImageAnnotatorClient(credentials=credentials)

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    return "No text detected"
