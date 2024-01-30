import psutil
from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def index():
    cpu_metric = psutil.cpu_percent(interval=1)
    mem_metric = psutil.virtual_memory().percent
    message = None  
    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or memory detected. Please Scale up!!"
    return render_template("index.html", cpu_var = cpu_metric, mem_var = mem_metric, message = message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    