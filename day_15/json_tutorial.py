import json

address_book = {
    "tom": {
        "name": "Tom",
        "address": "1 Red street, NY",
        "phone": 98989898
    },
    "bob": {
        "name": "Bob",
        "address": "2 Green street, NY",
        "phone": 89898989
    }
}

json_data = json.dumps(address_book, indent=4)
print("JSON Output:\n", json_data)

parsed_dict = json.loads(json_data)
print("\nParsed Bob's Address:", parsed_dict["bob"]["address"])
