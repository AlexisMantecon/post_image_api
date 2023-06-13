from flask import Flask, request

app = Flask(__name__)


@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the image file from the request
    image = request.files['image']

    # Process the image here
    # Save the image to a specified location
    save_path = 'images/image_processed.jpg'
    image.save(save_path)

    # Return a response
    return 'Image processed successfully'
