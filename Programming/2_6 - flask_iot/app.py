# imports
import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template
from get_kitchen_dht11_data import get_kitchen_data

app = Flask(__name__)

# data and graph funtions, plot functions imported from Matplotlib
def kitchen_temp():
    timestamps, temp, hum = get_kitchen_data(10)

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.plot(timestamps, temp, linestyle = 'dashed', linewidth='1.0', marker='o')
    ax.set_xlabel("timestamps")
    ax.set_ylabel("temperature C")
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def kitchen_hum():
    timestamps, temp, hum = get_kitchen_data(10)

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.plot(timestamps, hum, linestyle='dashed', linewidth='1.0', marker='o')
    ax.set_xlabel("timestamps")
    ax.set_ylabel("humidity %")
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

# app routing and run
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kitchen')
def kitchen():
    kitchen_temperature = kitchen_temp()
    kitchen_humidity = kitchen_hum()
    return render_template('kitchen.html', kitchen_temperature = kitchen_temperature, kitchen_humidity = kitchen_humidity)

@app.route('/livingroom')
def livingroom():
    return render_template('livingroom.html')

@app.route('/bedroom')
def bedroom():
    return render_template('bedroom.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)
