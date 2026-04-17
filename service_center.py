from flask import Flask, render_template, request, redirect, url_for, jsonify

service_center = Flask(__name__)

@service_center.route('/')
def home():
    return render_template('index.html')

@service_center.route('/services')
def services():
    return render_template('services.html')

@service_center.route('/about')
def about():
    return render_template('about.html')

@service_center.route('/contacts')
def contacts():
    return render_template('contacts.html')

@service_center.route('/submit_request', methods=['POST'])
def submit_request():
    name = request.form.get('name')
    phone = request.form.get('phone')
    device = request.form.get('device')
    problem = request.form.get('problem')

    print(f"Новая заявка от {name}, телефон: {phone}, устройство: {device}")
    return redirect(url_for('home'))


if __name__ == '__main__':
    service_center.run(debug=True)