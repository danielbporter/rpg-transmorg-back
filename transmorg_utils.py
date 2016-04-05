import json, csv


def csv_to_json(csv_filename, json_filename, first_id=0):
    id_counter = first_id
    records = []
    with open(csv_filename, 'r') as csv_fh:
        reader = csv.DictReader(csv_fh, restkey='no_key')
        for record in reader:
            record['id'] = id_counter
            id_counter += 1
            records.append(record)
    with open(json_filename, 'w') as json_fh:
        json.dump(records, json_fh, indent=2)


if __name__ == '__main__':
    csv_to_json('raw_content/items_raw.csv', 'raw_content/items.json')
