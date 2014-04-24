# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop
import json
import re
import fileinput
import pdb
import os.path
import subprocess
import git 
import hashlib


def changeFile(post, number):
    localfile = post[1:]
    endings = [".md", ".markdown"]
    files = [localfile + ending for ending in endings if os.path.isfile(localfile + ending)]
    if len(files) == 0:
        return
    with open(files[0],'r') as file:
        data = file.readlines()
        parse = False
        counter = 1
        for i, line in enumerate(data):
            if '{{#todo_block}}' in line:
                parse = True
                continue
            if parse:
                if re.match('[^[]*\[[^+]?\]', line):
                    if number == counter:
                        data[i] = re.sub('\[[^+]?\]',u'☑'.encode('utf8'), data[i], count = 1)
                        break
                    else:
                        counter = counter + 1


    with open(files[0],'w') as file:
        for l in data:
            file.write(l)



class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        pass

    @web.asynchronous
    def post(self):
        password = self.get_argument('key', '')
        login_response = {'error': True,
                          'msg': 'Wrong key entered!'}

        if  hashlib.md5(password.encode("utf8")).hexdigest() == '455523d86a8a1ab7c7d33208fe0219e7':
            git_dir = "."
            g = git.cmd.Git(git_dir)
            g.pull()
        
            login_response = {'error': True,
                          'msg': 'Pulling from github.'}
        
        self.write(login_response)


app = web.Application([
    (r'/git', ApiHandler),
])

if __name__ == '__main__':
    app.listen(9291)
    ioloop.IOLoop.instance().start()
