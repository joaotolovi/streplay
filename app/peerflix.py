import settings
import requests

def add_torrent(link):
    if settings.PEERFLIX_HOST:
        headers = {'Content-Type': 'application/json;charset=UTF-8',}
        response = requests.request(
            "POST", 
            f"{settings.PEERFLIX_HOST}/torrents", 
            headers=headers, 
            data="{\"link\":\""+link+"\"}")
        if response.status_code == 200:
            return response.json()
        print('responsea',response)
        return False
    else:
        return False

def torrents():
    if settings.PEERFLIX_HOST:
        headers = {'Content-Type': 'application/json;charset=UTF-8',}
        response = requests.request(
            "GET", 
            f"{settings.PEERFLIX_HOST}/torrents", 
            headers=headers)
        if response.status_code == 200:
            response.json()
    else:
        return False

def get_torrent(hash):
    if settings.PEERFLIX_HOST:
        headers = {'Content-Type': 'application/json;charset=UTF-8',}
        response = requests.request(
            "GET", 
            f"{settings.PEERFLIX_HOST}/torrents/{hash}", 
            headers=headers)
        if response.status_code == 200:
            return response.json()
    else:
        return False
