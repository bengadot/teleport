import falcon
import json

class Login(object):

    def on_post(self, req, resp):
        body = req.stream.read()
        userdata = json.loads(body)
        username = userdata['username']
        password = userdata['password']
        resp.body = '{{"username": "{:s}pkill", "password": "{:s}"}}'.format(username, password)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
        



        
