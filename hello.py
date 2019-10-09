from flask import Flask, render_template

app = Flask(__name__)

# Method directing users to specific url is called routing

@app.route('/')

def index():
    return render_template('index.html')


# Decorator modififes the func defined. Route tells app to start at root
@app.route('/Greetings/<int:planet>') 
# Will now create function that returns hello back to browser
def hello(planet):

    return render_template('hello.html', t_planet=planet)


