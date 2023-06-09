import requests
import json


objects_url = 'https://api.restful-api.dev/objects'

headers = {
    "content-type": "application/json"
}

product_payload = json.dumps({
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})

payload_updated = json.dumps({
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 1999,
      "price": 100,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})


# post_a_product = requests.post(create_product_url, headers=headers, data=product_payload)
# print(post_a_product.json())



get_a_product_by_id = requests.get(f'{objects_url}/ff80818188764f13018877d85f51019f', headers=headers)
print(get_a_product_by_id.json())
update_product = requests.put(f'{objects_url}/ff80818188764f13018877d85f51019f', headers=headers, data=payload_updated)
print(update_product.json())
get_a_product_by_id = requests.get(f'{objects_url}/ff80818188764f13018877d85f51019f', headers=headers)
print(get_a_product_by_id.json())

delete_product = requests.delete(f'{objects_url}/ff80818188764f13018877d85f51019f', headers=headers)
get_a_product_by_id = requests.get(f'{objects_url}/ff80818188764f13018877d85f51019f', headers=headers)
print(get_a_product_by_id.json())