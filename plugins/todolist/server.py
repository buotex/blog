from tornado import websocket, web, ioloop
import json
import re
import fileinput
import pdb
import os.path


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
                        data[i] = re.sub('\[[^+]?\]','[+]', data[i], count = 1)
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

app = web.Application([
    (r'/api', ApiHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
