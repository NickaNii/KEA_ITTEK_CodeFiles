import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template
from get_kitchen_dht11_data import get_kitchen_data

app = Flask(__name__)

def kitchen_temp():
    timestamps, temp, hum = get_kitchen_data(10)

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    
    ax.plot(timestamps, temp)
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
    ax.plot(timestamps, hum)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kitchen')
def stue():
    kitchen_temperature = kitchen_temp()
    kitchen_humidity = kitchen_hum()
    return render_template('kitchen.html', kitchen_temperature = kitchen_temperature, kitchen_humidity = kitchen_humidity)

app.run(debug=True)
