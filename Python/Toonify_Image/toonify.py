# shutil is used to save image locally
import requests
import sys 
import shutil 
from decouple import config

imagePath=sys.argv[1]
api_key=config("API_KEY")
r = requests.post(
    "https://api.deepai.org/api/toonify",
    files={
        'image': open(imagePath, 'rb'),
    },
    headers={'api-key': api_key}
)
y=r.json()
image_url=y['output_url']
filename = image_url.split("/")[-1]
# Open the url image
r1 = requests.get(image_url, stream = True)
# Check if the image was retrieved successfully
if r1.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r1.raw.decode_content = True
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r1.raw, f)
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')
