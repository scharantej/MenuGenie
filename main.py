
# main.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    requirements = request.form
    # Process the form data and query the database to find matching services
    services = get_matching_services(requirements)
    return render_template('results.html', services=services)

@app.route('/request-service/<service_id>')
def request_service(service_id):
    service_details = get_service_details(service_id)
    return render_template('request_service.html', service=service_details)

@app.route('/submit-request', methods=['POST'])
def submit_request():
    request_data = request.form
    # Save the request in the database or forward it to the appropriate specialist
    save_request(request_data)
    return render_template('confirmation.html')

def get_matching_services(requirements):
    # Connect to the database and perform the query to find matching services
    connection = sqlite3.connect('services.db')
    cursor = connection.cursor()
    query = "SELECT * FROM services WHERE "
    for requirement in requirements:
        query += f"{requirement} = '{requirements[requirement]}' AND "
    query = query[:-4]  # Remove the trailing "AND "
    cursor.execute(query)
    services = cursor.fetchall()
    connection.close()
    return services

def get_service_details(service_id):
    # Connect to the database and fetch the details of the service with the given ID
    connection = sqlite3.connect('services.db')
    cursor = connection.cursor()
    query = "SELECT * FROM services WHERE service_id = ?"
    cursor.execute(query, (service_id,))
    service_details = cursor.fetchone()
    connection.close()
    return service_details

def save_request(request_data):
    # Connect to the database and save the request
    connection = sqlite3.connect('requests.db')
    cursor = connection.cursor()
    query = "INSERT INTO requests (service_id, sales_partner_name, company_name, budget, requirements) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (request_data['service_id'], request_data['sales_partner_name'],
               request_data['company_name'], request_data['budget'], request_data['requirements']))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    app.run(debug=True)
