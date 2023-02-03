# Imports
import requests

# Globals
BASE = 'http://127.0.0.1:5000/'


# Functions
def test_helloworld_get():
    response = requests.get(BASE + 'helloworld')
    print(response.json())


def test_helloworld_post():
    response = requests.post(BASE + 'helloworld')
    print(response.json())


def test_helloworld_get_args():
    response = requests.get(BASE + 'helloworld/dan/30')
    print(response.json())


def test_helloworld_get_args_1():
    response = requests.get(BASE + 'helloworld/bob')
    print(response.json())


def test_video_put_fail():
    response = requests.put(BASE + 'video/12', json={"likes": 10})
    print(response.json())


def test_video_put_pass():
    response = requests.put(BASE + 'video/12', json={"likes": 10, 'name': 'The Last Samurai', 'views': 800})
    print(response.json())


def test_video_not_found_abort():
    response = requests.get(BASE + 'videos/20')
    print(response)


def test_video_delete():
    response = requests.post(BASE + 'video/100', json={"likes": 10, 'name': 'The Matrix', 'views': 800})
    print(response.json())
    response = requests.delete(BASE + 'video/100')
    print(response)


def test_put_post():
    response = requests.post(BASE + 'video/100', json={"likes": 10, 'name': 'The Matrix', 'views': 800})
    print(response.json())
    response = requests.put(BASE + 'video/100', json={"likes": 10, 'name': 'The Matrix 2', 'views': 800})
    print(response.json())
    response = requests.post(BASE + 'video/100', json={"likes": 10, 'name': 'The Matrix 2', 'views': 800})
    print(response)


def test_db():
    response = requests.get(BASE + 'video/1')
    print(response.json())
    response = requests.post(BASE + 'video/1', json={"likes": 10, 'name': 'The Matrix', 'views': 800})
    print(response.json())
    response = requests.get(BASE + 'video/1')
    print(response.json())
    response = requests.delete(BASE + 'video/1')
    print(response)
    response = requests.get(BASE + 'video/1')
    print(response.json())
    response = requests.post(BASE + 'video/1', json={"likes": 10, 'name': 'The Matrix', 'views': 800})
    print(response.json())
    response = requests.patch(BASE + 'video/1', json={"likes": 100, 'name': 'The Matrix 2', 'views': 900})
    print(response.json())


def test_restx():
    response = requests.get(BASE + 'video/1')
    print(response.json())
    response = requests.post(BASE + 'video/2', json={"likes": 10, 'name': 'The Matrix 3', 'views': 800})
    print(response.json())
    response = requests.get(BASE + 'video/2')
    print(response.json())
    response = requests.patch(BASE + 'video/2', json={"likes": 100, 'name': 'The Matrix 3', 'views': 800})
    print(response.json())
    response = requests.get(BASE + 'video/2')
    print(response.json())
    response = requests.delete(BASE + 'video/1')
    print(response)
    response = requests.delete(BASE + 'video/2')
    print(response)


if __name__ == '__main__':
    # test_helloworld_get()
    # test_helloworld_post()
    # test_helloworld_get_args()
    # test_helloworld_get_args_1()
    # test_video_put()
    # test_video_put_pass()
    # test_video_not_found_abort()
    # test_video_delete()
    # test_put_post()
    test_restx()
