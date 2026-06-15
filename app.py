""" from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():  
    return 'Application is running successfully!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  """

from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'successfully deployed python application through jenkins!!!!!!!!!, added webhook'
@app.route('/hi')
def hell():
    return '<h1>Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii from Flask & Docker</h1>'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)