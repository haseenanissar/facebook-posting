import requests

# Your Facebook API credentials
app_id = 'id'
app_secret = 'secret key'
page_id = 'id'
access_token = 'your access token'


url = f'https://graph.facebook.com/v13.0/{page_id}/photos'

image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Caerte_van_Oostlant_4MB.jpg/1591px-Caerte_van_Oostlant_4MB.jpg?20110218154138",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Caerte_van_Oostlant_4MB.jpg/1591px-Caerte_van_Oostlant_4MB.jpg?20110218154138",
    # Add more image URLs as needed
    ]
# Loop through the image URLs and post each photo
for image_url in image_urls:
    # Specify the data for the request
    data = {
        "url": image_url,
        "access_token": access_token,
        "published": "true",  # Set to "true" if you want to publish immediately
    }

    # Make the request to post the photo
    response = requests.post(url.format(page_id=page_id), data=data)

    # Check the response
    if response.status_code == 200:
        print(f"Successfully posted image: {image_url}")
    else:
        print(f"Failed to post image: {image_url}")
        print(response.json())  # Print the error response for debugging
