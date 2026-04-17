from flask import Flask

service_center = Flask(__name__)
@service_center.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    service_center.run(debug=True)
