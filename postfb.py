import requests

# Your Facebook API credentials
app_id = 'your app id'
app_secret = 'your app secret'
page_id = 'your page id'
access_token = 'your long lived access token'
# Function to post on Facebook
def post_image_on_facebook(image_url,caption):
    url = f'https://graph.facebook.com/v13.0/{page_id}/photos'
    params = {
        #commented ones are to post images from the web
       # 'url': image_url,
        'caption': caption,
        'access_token': access_token,
    }


    try:
        with open(image_url, 'rb') as photo:
            files = {'source': photo}
            print(photo)
            response = requests.post(url,params=params,files=files)
            print('Image post successful!')
            """
            response = requests.post(url, params=params)
            response.raise_for_status()
            print('Image post successful!')
            """
    except requests.HTTPError as e:
        print(f'Error: {e}')
        print('Image post failed.')

# Example usage
#image_url = 'https://flashcarwashes.com/wp-content/uploads/2021/12/FlashCarwash-2021.png'
image_url='/Users/haseena/Documents/car-wash.jpeg'
caption = 'Check out this amazing image!'
post_image_on_facebook(image_url, caption)