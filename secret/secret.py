import json

SECRET_PATH = 'secret/client_secret.json'
_WEB = 'web'
_CLIENT_ID = 'client_id'


def load_credentials_from_path(path):
    f = open(path, 'r')
    data = f.read()
    cred_json = json.loads(data)
    client_id = cred_json[_WEB][_CLIENT_ID]
    f.close()

    return client_id

web_client_id = load_credentials_from_path(SECRET_PATH)
