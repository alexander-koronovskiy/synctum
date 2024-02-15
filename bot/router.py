import requests


def parse_to_add(message):
    user, route = message.text.split('/')
    user = user.strip()
    route = int(route.strip())
    print(user, route)
    data = {'user_id': user, 'route': route}
    requests.post('http://127.0.0.1:8000/add_route/', json=data)
