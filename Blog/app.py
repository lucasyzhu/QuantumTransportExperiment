from flask import Flask, render_template, request
from flask import escape
from flask import render_template_string
import os
import time

#查看所有的静态html文件，并存为html_files list
html_files = []
for root, dirs, files in os.walk("templates"):
  for name in files:
    html_files.append(os.path.join(root, name).replace('templates',''))
    
#----------------------------------------------
app = Flask(__name__)
    
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/<path:dummy>')
def all_subpage(dummy):
    #有时浏览器会在url末尾自动添加'/'，所以需要检查
    url_str = request.path
    if url_str.endswith('/'): url_str = url_str[:-1]

    #判断是否有网页文件
    #如果有，则返回相应静态网页，并记录时间，ip，以及网页
    #如果没有，则返回404页面
    if (url_str in html_files):
        record(url_str,  request.remote_addr)
        return render_template(url_str)
    return render_template_string('<center><h1> 欧欧 </h1><h2>啥也没有</h2>')
    
    
def record(url_str, ip):
  localtime = time.asctime( time.localtime(time.time()) )
  data_str = "%s | %s | %s\n"%(localtime, ip, url_str)
  with open("record.txt", "a") as file:
    file.write(data_str) 
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)#80, debug=True )
