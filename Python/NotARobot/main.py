from captcha.image import ImageCaptcha
import random
from flask import Flask, request, redirect, url_for, jsonify
import time

app = Flask(__name__)

def captcha():
  num = random.randint(1000,9999)
  image = ImageCaptcha()
  tstr = time.strftime("%Y%m%d-%H%M%S")
  image.write(str(num), f'./static/{tstr}.png')
  return num,tstr

@app.route("/", methods=["GET","POST"])
def index():
  global num1
  if request.method=="GET":
    num1,tstr = captcha()
    return f'''
    <form method="POST">
    <img src="./static/{tstr}.png"><br>
    <input type="text" name="ip">
    <button type"submit">submit</button>
    '''
  elif request.method=="POST":
    ip = request.form["ip"]
    try:
      if int(ip)==int(num1):
        return jsonify({'status':'success'}) 
      else:
        return redirect(url_for(".index"))
    except:
      return redirect(url_for(".index"))

@app.route("/api", methods=["GET","POST"])
def api():
  req = request.args.get("req")
  num = request.args.get("num")
  global num1
  if req=="get":
    num1,tstr = captcha()
    return jsonify({"number": num1, "image_url":f"http://notarobot.virajman3.repl.co/static/{tstr}.png"})
  elif req=="post":
    if int(num)==int(num1):
        return jsonify({'status':'success'}) 
    else:
        return jsonify({'status':'fail'})
        
if __name__=="__main__":
  app.debug=True
  app.run(host="0.0.0.0",threaded=True,use_reloader=True)
