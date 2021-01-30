from flask import Flask, render_template
from flask import escape


app = Flask(__name__)
    
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/StudyNotes/tkwant/<name>/')
def StudyNotes_section(name):
    return render_template('/StudyNotes/tkwant/%s'% escape(name))
    
@app.route('/其他/建站经历/<name>/')
def other_section(name):
    return render_template('/其他/建站经历/%s'% escape(name))
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
