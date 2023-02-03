# Imports
import requests
import time


# Globals
BASE = 'http://127.0.0.1:5000'
SWORDS = {
    1: {
        "name": "Half-Moon",
        "style": "Katana",
        "year": 2001
    },
    2: {
        "name": "Liberty",
        "style": "Claymore",
        "year": 2008
    },
    3: {
        "name": "Fire",
        "style": "Hand-and-a-Half",
        "year": 1998
    }
}


# Functions
def test_get(sword_id):
    response = requests.get(BASE + f"/sword/{sword_id}")
    print(response.json())


def test_get_malformed():
    response = requests.get(BASE + f"/sword/fake")
    print(response)


def test_get_fake():
    response = requests.get(BASE + f"/sword/5000")
    print(response.json())


def test_post(sword_id):
    response = requests.post(BASE + f"/sword/{sword_id}", json=SWORDS[sword_id])
    print(response.json())


def test_post_lack_json(sword_id):
    response = requests.post(BASE + f"/sword/{sword_id}")
    print(response)


def test_post_json_field_missing_field(sword_id):
    bad_json = {'name': "fake"}
    response = requests.post(BASE + f"/sword/{sword_id}", json=bad_json)
    print(response.json())


def test_post_json_field_wrong_dtype(sword_id):
    bad_json = {'name': "Fire", "style": 'Hand-and-a-Half', "year": "hello"}
    response = requests.post(BASE + f"/sword/{sword_id}", json=bad_json)
    print(response.json())


def test_delete(sword_id):
    response = requests.delete(BASE + f"/sword/{sword_id}")
    print(response.json())


def test_delete_bad_id():
    response = requests.delete(BASE + f"/sword/4000")
    print(response)


def test_run():
    test_post(1)  # success

    test_get(1)  # success
    # test_get_malformed()  # 404 - not found
    # test_get_fake()  # 409 - could not find id
    #
    # test_post_lack_json(2)  # 400 - not found
    # test_post(1)  # should fail, identical therefore not unique
    # test_post_json_field_missing_field(3)  # 400 - invalid params
    # test_post_json_field_wrong_dtype(3)  # 400 - invalid params
    #
    # test_delete(1)  # success
    # test_delete_bad_id()  # 404 - not found


def test_token():
    # Success
    response = requests.get(BASE + "/login/2")
    token = response.json()['token']
    response = requests.post(BASE + "/login/2", headers={'Authorization': f'Bearer {token}'})
    print(response.json())
    # Fail
    response = requests.get(BASE + "/login/1")
    token = response.json()['token']
    response = requests.post(BASE + "/login/1", headers={'Authorization': f'Bearer {token}'})
    print(response.json())
    # Expiration
    response = requests.get(BASE + "/login/2")
    token = response.json()['token']
    time.sleep(6)
    response = requests.post(BASE + "/login/2", headers={'Authorization': f'Bearer {token}'})
    print(response.json())
