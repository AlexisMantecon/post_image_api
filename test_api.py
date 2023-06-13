import requests

# Specify the image file path
image_path = 'images/image.jpg'

# Create a dictionary to hold the file
files = {'image': open(image_path, 'rb')}

# Send a POST request to the API endpoint
response = requests.post('http://localhost:5000/process_image', files=files)

# Print the response
print(response.text)