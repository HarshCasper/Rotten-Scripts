from selenium import webdriver 
from urllib.request import urlretrieve

class InstagramBot:

    # Setting the Basic Constraints in Instagram.
    def __init__(self, path, user_handler):
        self.url = "https://www.instagram.com{}".format(user_handler)
        self.driver = webdriver.Chrome(path)
    
    # Download Function to download the Images.
    def download_image(self):

        try:
            image = None

            # Making the Request to Instagram
            try:
                self.driver.get(self.url)
            except Exception:
                print("Problem with Instagarm Handler. Please enter the valid URL Handler.")

            try:
                image = self.driver.find_element_by_xpath('//img[@class="_6q-tv]')
            except Exception:
                print("Trying for the another Possibility")
            
            try:
                image = self.driver.find_element_by_xpath('//img[@class="be6sR]')
            except Exception:
                print("Something Went Wrong.")
            
            # Getting the Image Link
            image_link = image.get_attribute('src')
            # Setting the Destination Download Folder.
            download_path = "./Downloads/{}.png".format(self.user_handler)

            urlretrieve(image_link, download_path)
            print("Sucessfully Downloaded the Profile Picture.")

            # Closing the Driver Connection
            self.driver.close()
        except Exception:
            print("Something Went Wrong.")
            self.driver.close()

driverPath = input("Enter your driver path properly: ")
instagramURLHandle = input("Enter the URl Handle Properly")
bot = InstagramBot(driverPath, instagramURLHandle)