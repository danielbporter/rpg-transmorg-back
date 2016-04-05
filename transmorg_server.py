from flask import abort, Flask, jsonify, request
import json

SOURCE = 'raw_content/items.json'
TARGET = 'contents/items.json'

records = read_raw_records()
id_counter = records[0]['id']
objects = load_objects()

app = Flask(__name__)


@app.route('/record', methods=['GET'])
def get_next_record():
    """Respond with the next record to be x-morged."""
    next_record = records[id_counter]
    id_counter += 1
    return jsonify(next_record)


@app.route('/record/<int:record_id>', method=['GET'])
def get_specific_record(record_id):
    specific_record = records.get(record_id, None)
    if specific_record is None:
        abort(404)
    else:
        return jsonify(specific_record)


@app.route('/record', methods=['POST'])
def save_new_object():
    """Save a x-morged object."""
    new_object = request.json()
    objects.append(new_object)
    json.dump(objects, open(TARGET, 'w'))


def read_raw_records():
    return json.load(open(SOURCE, 'r'))


def load_objects():
    return json.load(open(TARGET, 'r'))


if __name__ == '__main__':
    app.run()
