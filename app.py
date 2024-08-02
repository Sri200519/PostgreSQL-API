from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    conn = psycopg2.connect(
        dbname='beacon',
        user='***',
        password='***',
        host="localhost",
        port='5432'
    )
    return conn

# General function to fetch data from a table
def fetch_data_from_table(table_name):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f'SELECT * FROM {table_name};')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# Define endpoints for each table
@app.route('/autism_services_resource_directory', methods=['GET'])
def get_autism_services_resource_directory():
    data = fetch_data_from_table('autism_services_resource_directory')
    return jsonify(data)

@app.route('/autism_spectrum_disorder', methods=['GET'])
def get_autism_spectrum_disorder():
    data = fetch_data_from_table('autism_spectrum_disorder')
    return jsonify(data)

@app.route('/birth_to_3_programs', methods=['GET'])
def get_birth_to_3_programs():
    data = fetch_data_from_table('birth_to_3_programs')
    return jsonify(data)

@app.route('/connecticut_food_banks_mobile_pantry_schedule', methods=['GET'])
def get_connecticut_food_banks_mobile_pantry_schedule():
    data = fetch_data_from_table('connecticut_food_banks_mobile_pantry_schedule')
    return jsonify(data)

@app.route('/connecticut_resource_directory', methods=['GET'])
def get_connecticut_resource_directory():
    data = fetch_data_from_table('connecticut_resource_directory')
    return jsonify(data)

@app.route('/diaper_connections', methods=['GET'])
def get_diaper_connections():
    data = fetch_data_from_table('diaper_connections')
    return jsonify(data)

@app.route('/family_support_and_services', methods=['GET'])
def get_family_support_and_services():
    data = fetch_data_from_table('family_support_and_services')
    return jsonify(data)

@app.route('/state_education_resource_center', methods=['GET'])
def get_state_education_resource_center():
    data = fetch_data_from_table('state_education_resource_center')
    return jsonify(data)

@app.route('/temporary_family_assistance', methods=['GET'])
def get_temporary_family_assistance():
    data = fetch_data_from_table('temporary_family_assistance')
    return jsonify(data)

@app.route('/women_infants_children', methods=['GET'])
def get_women_infants_children():
    data = fetch_data_from_table('women_infants_children')
    return jsonify(data)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
