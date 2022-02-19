#@auto-fold regex \.\
import requests as r,os, json,base64,python_helper as ph
creds = json.load(open(ph.root_fp+'/creds/creds.json')).get('img_gur')
baseurl = 'https://api.imgur.com/3/'
headers = {'Authorization': 'Client-ID {}'.format(creds.get('img_ur_client_id'))}
    # NOTE: DOCS https://apidocs.imgur.com/#2078c7e0-c2b8-4bc8-a646-6e544b087d0f

def upload_path(path):
    """Upload load files from path"""
    with open(path, 'rb') as fd:
        contents = fd.read()
        b64 = base64.b64encode(contents)
        data = {'image': b64,
            'type': 'base64',}
        resp = r.post(baseurl+'image',headers=headers, data = data )
    return resp.json().get('data')
