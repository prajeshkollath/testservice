from flask import Flask, jsonify
from google.cloud import firestore
from google.oauth2 import service_account
import os

app = Flask(__name__)

# Set up Firestore
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
credentials = service_account.Credentials.from_service_account_file(credentials_path)
db = firestore.Client(credentials=credentials)

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

@app.route('/add')
def add_document():
    doc_ref = db.collection(u'my_collection').document(u'my_document')
    doc_ref.set({
        u'name': u'Test Document',
        u'description': u'This is a test document'
    })
    return jsonify({"message": "Document added"})

@app.route('/read')
def read_document():
    doc_ref = db.collection(u'my_collection').document(u'my_document')
    doc = doc_ref.get()
    if doc.exists:
        return jsonify(doc.to_dict())
    else:
        return jsonify({"message": "No such document"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
