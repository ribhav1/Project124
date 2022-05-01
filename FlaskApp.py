from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': 'Somone',
        'Contact': '1234567890',
        'done': False
    },
    {
        'id': 2,
        'title': 'Someone 2',
        'description': '0987654321',
        'done': False 
    }
]

@app.route('/add-data', methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'Please provide the data'
        }, 400)
    contact = {
        'id': contact[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ''),
        'done': False
    }

    contacts.append(contact)

    return jsonify({
        'status': 'success',
        'message': 'Contact added successfully'
    })
    
if (__name__ == '__main__'):
    app.run(debug = True)