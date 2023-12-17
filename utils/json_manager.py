import os
import json

data_structure = {
    'trabajadores': [],
    'areas': [{
        'id': 1,
        'nombre': 'Administración',
        'activo': True
    }],
}


def read_data():
    if not os.path.isfile('data.json'):
        with open('data.json', 'w') as doc:
            json.dump(data_structure, doc)
    
    with open('data.json', 'r') as doc:
        data = json.load(doc)

    return data

def write_json(data):
    with open('data.json', 'w') as doc:
        json.dump(data, doc)

def trabajadores():
    return list(filter(lambda x: x['activo'] == True, read_data()['trabajadores']))

