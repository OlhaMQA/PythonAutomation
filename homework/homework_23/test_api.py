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
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
})

payload_patched = json.dumps({
   "name": "Apple MacBook Pro 16 (Patched Name)"
})


# Tests status code for POST request
def test_post_request_status_code():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    assert post_a_product.status_code == 200


# Tests response for POST request
def test_post_request_response():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    assert post_a_product.json()['name'] == 'Apple MacBook Pro 16'
    assert post_a_product.json()['data']['year'] == 2019
    assert post_a_product.json()['data']['price'] == 1849.99
    assert post_a_product.json()['data']['CPU model'] == 'Intel Core i9'
    assert post_a_product.json()['data']['Hard disk size'] == '1 TB'
    assert post_a_product.json()['id'] is not None
    assert post_a_product.json()['createdAt'] is not None


# Tests status code for GET by id request
def test_get_product_by_id_status_code():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    get_a_product_by_id = requests.get(f'{objects_url}/{id}', headers=headers)
    assert get_a_product_by_id.status_code == 200


# Tests response for GET by id request
def test_get_product_by_id_response():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    get_a_product_by_id = requests.get(f'{objects_url}/{id}', headers=headers)
    assert get_a_product_by_id.json()['name'] == 'Apple MacBook Pro 16'
    assert get_a_product_by_id.json()['data']['year'] == 2019
    assert get_a_product_by_id.json()['data']['price'] == 1849.99
    assert get_a_product_by_id.json()['data']['CPU model'] == 'Intel Core i9'
    assert get_a_product_by_id.json()['data']['Hard disk size'] == '1 TB'
    assert get_a_product_by_id.json()['id'] == id


# Tests status code for PUT product by id request
def test_put_product_by_id_status_code():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    update_product = requests.put(f'{objects_url}/{id}', headers=headers, data=payload_updated)
    assert update_product.status_code == 200


# Tests response for PUT product by id request
def test_put_product_by_id_response():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    update_product = requests.put(f'{objects_url}/{id}', headers=headers, data=payload_updated)
    assert update_product.json()['name'] == 'Apple MacBook Pro 16'
    assert update_product.json()['data']['year'] == 2019
    assert update_product.json()['data']['price'] == 2049.99
    assert update_product.json()['data']['CPU model'] == 'Intel Core i9'
    assert update_product.json()['data']['Hard disk size'] == '1 TB'
    assert update_product.json()['data']['color'] == 'silver'


# Tests status code for PATCH product by id request
def test_patch_product_by_id_status_code():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    update_product = requests.patch(f'{objects_url}/{id}', headers=headers, data=payload_patched)
    assert update_product.status_code == 200


# Tests response for PATCH product by id request
def test_patch_product_by_id_response():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    patch_product = requests.patch(f'{objects_url}/{id}', headers=headers, data=payload_patched)
    assert patch_product.json()['name'] == 'Apple MacBook Pro 16 (Patched Name)'
    assert patch_product.json()['data']['year'] == 2019
    assert patch_product.json()['data']['price'] == 1849.99
    assert patch_product.json()['data']['CPU model'] == 'Intel Core i9'
    assert patch_product.json()['data']['Hard disk size'] == '1 TB'


# Tests status code for DELETE product by id request
def test_delete_product_by_id_status_code():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    delete_product = requests.delete(f'{objects_url}/{id}', headers=headers)
    assert delete_product.status_code == 200


# Tests response for DELETE product by id request
def test_delete_product_by_id_response():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    delete_product = requests.delete(f'{objects_url}/{id}', headers=headers)
    assert delete_product.json()['message'] == f"Object with id = {id} has been deleted."


# Test if product was deleted after sending the DELETE request
def test_product_is_deleted():
    post_a_product = requests.post(objects_url, headers=headers, data=product_payload)
    id = post_a_product.json()['id']
    delete_product = requests.delete(f'{objects_url}/{id}', headers=headers)
    get_a_product_by_id = requests.get(f'{objects_url}/{id}', headers=headers)
    assert get_a_product_by_id.status_code == 404
