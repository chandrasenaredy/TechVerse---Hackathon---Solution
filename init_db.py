from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# Database configuration
DATABASE = 'hcl.db'

def get_db_connection():
	"""Create a database connection"""
	conn = sqlite3.connect(DATABASE)
	conn.row_factory = sqlite3.Row
	return conn

def init_db():
	"""Initialize the database with tables"""
	conn = get_db_connection()
	c = conn.cursor()
	
	# Create a sample table
	c.execute('''CREATE TABLE IF NOT EXISTS requests
				 (id INTEGER PRIMARY KEY AUTOINCREMENT,
				  title TEXT NOT NULL,
				  description TEXT,
				  status TEXT DEFAULT 'pending',
				  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
	
	conn.commit()
	conn.close()

@app.route('/api/requests', methods=['GET'])
def fetch_requests():
	"""Fetch all requests from the database"""
	try:
		conn = get_db_connection()
		requests_data = conn.execute('SELECT * FROM requests').fetchall()
		conn.close()
		
		return jsonify([dict(row) for row in requests_data]), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@app.route('/api/requests/<int:request_id>', methods=['GET'])
def fetch_request(request_id):
	"""Fetch a specific request by ID"""
	try:
		conn = get_db_connection()
		req = conn.execute('SELECT * FROM requests WHERE id = ?', (request_id,)).fetchone()
		conn.close()
		
		if req is None:
			return jsonify({'error': 'Request not found'}), 404
		
		return jsonify(dict(req)), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@app.route('/api/requests', methods=['POST'])
def create_request():
	"""Create a new request"""
	try:
		data = request.get_json()
		
		if not data or 'title' not in data:
			return jsonify({'error': 'Title is required'}), 400
		
		conn = get_db_connection()
		conn.execute('INSERT INTO requests (title, description) VALUES (?, ?)',
					 (data['title'], data.get('description', '')))
		conn.commit()
		conn.close()
		
		return jsonify({'message': 'Request created successfully'}), 201
	except Exception as e:
		return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
	init_db()
	app.run(debug=True, port=5000)
