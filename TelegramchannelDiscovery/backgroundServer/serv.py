from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import cgi
from Channel import Channel

class Serv(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            print('get request on /')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("{'success':'success'}", 'utf-8'))
    def do_POST(self):
        print(self.path)
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        if self.path == '/channel/approve':
            print("here")
            form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
            print(form.list)
            username = form.getvalue('username')
            channel = Channel('@'+username) 
            print(channel.valid)
            # content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            # print(content_length)
            # post_data = self.rfile.read(content_length) # <--- Gets the data itself
            # print(post_data.decode())
            # self.send_response(200)
            if channel.valid == 'valid':
                print("if")
                newchannel = {
                    'cat_id': form.getvalue('category'),
                    'title': channel.title,
                    'description': channel.description,
                    'members': channel.subscribers_count,
                    'contact_name': form.getvalue('ownername'),
                    'contact_phone': form.getvalue('ownerphone'),
                    'contact_address': form.getvalue('owneraddress'),
                    'user_id': form.getvalue('userid'),
                    'username': form.getvalue('username')
                }
                imgs = {'img': channel.image}
                print("sending request")
                resp = requests.post('http://127.0.0.1:8000/api/channel',  files=imgs, data=newchannel )
                print(resp.text)
                self.end_headers()
                self.wfile.write(bytes(channel.valid, 'utf-8'))
            else:
                print("else")
                self.end_headers()
                self.wfile.write(bytes(channel.valid, 'utf-8'))
            # exit()
print("server running on port 5000")
httpd = HTTPServer(('localhost', 5000), Serv)
httpd.serve_forever()