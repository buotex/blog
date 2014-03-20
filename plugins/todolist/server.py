# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop
import json
import re
import fileinput
import pdb
import os.path
import subprocess


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
        post = self.get_argument("post")
        number = self.get_argument("number")
        url = self.request.full_url()
        m = re.match(r"[^:]+:[^:]+", url)
        n = re.match(r"[^.]+", post)
        result = m.group(0) + ":9292" + n.group(0)
        changeFile(post, int(number))

        self.write('<html xmlns="http://www.w3.org/1999/xhtml">'+
                    '<head>' +
                    '<meta http-equiv="refresh" content="0.5;URL=\'{}\'" />'.format(result) +
                    '</head><body>Ticking...</body></html>')
        #self.redirect(result)
        self.finish()

    @web.asynchronous
    def post(self):
        pass

class TodoHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        cache = self.get_argument("cache")
        context = self.get_argument("context")
        project = self.get_argument("project")
        url = self.request.full_url()
        m = re.match(r"[^:]+:[^:]+", url)
        #n = re.match(r"[^.]+", post)
        #result = m.group(0) + ":9292" + n.group(0)
        #changeFile(post, int(number))

        #self.write('<html xmlns="http://www.w3.org/1999/xhtml">'+
        #            '<head>' +
        #            '<meta http-equiv="refresh" content="0.5;URL=\'{}\'" />'.format(result) +
        #            '</head><body>Ticking...</body></html>')
        #self.redirect(result)        

        p = subprocess.Popen(["/home/bxu/.todo/todo.sh", "-p", "ls", project, context],  stdout=subprocess.PIPE)
        out, err = p.communicate()
        with open("todo/todo" + cache + ".md", "w") as f:
            for l in out.split("\n"):
                words = l.split()
                try:
                    #go.db
                    int(words[0])
                    lowerlim = 1
                    prefix = ''
                    suffix = ''
                    if '(' in words[1]:
                        lowerlim = lowerlim + 1
                        prefix = '**'
                        suffix = '**'

                    f.write('- ')

                    if 'x' in words[1]:
                        lowerlim = lowerlim + 2
                        f.write(u'\u2611 '.encode("utf8"))
                    else:
                        f.write(u'\u2610 '.encode("utf8"))

                    f.write(prefix)
                    f.write(" ".join(words[lowerlim:]))
                    f.write(suffix)
                    f.write("\n")
                except:
                    pass

        #self.write('<html xmlns="http://www.w3.org/1999/xhtml">'+
        #            '<head>' +
        #            '<meta http-equiv="refresh" content="0.5;URL=\'{}\'" />'.format(result) +
        #            '</head><body>Ticking...</body></html>')
        result = m.group(0) + ":9292/todo/todo" + cache
        self.write('<html xmlns="http://www.w3.org/1999/xhtml">'+
                    '<head>' +
                    '<meta http-equiv="refresh" content="0.5;URL=\'{}\'" />'.format(result) +
                    '</head><body>Ticking...</body></html>')
        #self.redirect(result)        
        #self.write('<html xmlns="http://www.w3.org/1999/xhtml">'+
        #            '<head>' +
        #            '</head><body>{}</body></html>'.format(out))
        
        
        self.finish()

    @web.asynchronous
    def post(self):
        pass

app = web.Application([
    (r'/api', ApiHandler),
])
app2 = web.Application([
    (r'/todo', TodoHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    app2.listen(8889)
    ioloop.IOLoop.instance().start()
