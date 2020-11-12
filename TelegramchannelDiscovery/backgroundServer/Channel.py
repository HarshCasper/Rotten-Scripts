import requests, os, errno
    
class Channel:
    def __init__(self, handler):
        try:
            get_chat_URL = 'https://api.telegram.org/bot1071915503:AAG6OVmjh_NfNIz21aSFmBv85d3sEBhfxns/getChat'
            get_chat_members_count_URL = 'https://api.telegram.org/bot1071915503:AAG6OVmjh_NfNIz21aSFmBv85d3sEBhfxns/getChatMembersCount'
            get_user_profile_photos_URL = 'https://api.telegram.org/bot1071915503:AAG6OVmjh_NfNIz21aSFmBv85d3sEBhfxns/getUserProfilePhotos'
            get_profile_picture_path_URL  = 'https://api.telegram.org/bot1071915503:AAG6OVmjh_NfNIz21aSFmBv85d3sEBhfxns/getFile'
            get_profile_picture_URL  = 'https://api.telegram.org/file/bot1071915503:AAG6OVmjh_NfNIz21aSFmBv85d3sEBhfxns/'
            PARAMS = {'chat_id':handler}

            r = requests.get(url = get_chat_URL, params = PARAMS)

            data = r.json()

            r2 = requests.get (url = get_chat_members_count_URL, params = {'chat_id':handler})

            r3 = requests.get (url = get_profile_picture_path_URL, params = {'file_id':data['result']['photo']['big_file_id']})

            r4 = requests.get (url = get_profile_picture_URL+ r3.json()['result']['file_path'])
            
                            
            self.handler = handler
            self.title = data['result']['title']
            self.id = data['result']['id']
            self.username = data['result']['username']
            self.description = data['result']['description']
            self.subscribers_count = r2.json()['result'] if r2.json()['ok'] else 0
            # self.profile_pic_path = 'http://localhost:8000/images/'+str(self.id)+'.jpg'
            self.image = r4.content
            self.valid = 'valid'
        except:
            self.valid = 'invalid'
            self.title = None
            self.id = None
            self.username = None
            self.description = None
            self.subscribers_count = None
            self.profile_pic_path = None
            self.image = None
            return
        
        # if not os.path.exists(os.path.dirname(self.profile_pic_path)):
        #     try:
        #         os.makedirs(os.path.dirname(self.profile_pic_path))
        #     except OSError as exc:
        #         if exc.errno != errno.EEXIST:
        #             raise
        # with open(self.profile_pic_path, 'wb') as f:
        #     f.write(r4.content)
