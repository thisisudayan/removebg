# modules for remove background and request
from rembg import remove
import requests
from PIL import Image

#module for create server
import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        imageurl = self.get_argument("image")
        color = self.get_argument("color")
        outputPath = 'output.png'
        input = Image.open(requests.get(imageurl, stream=True).raw)
        output = remove(input)
        output.save(outputPath)
        with open('output.png', 'rb') as file: 
            self.write(file.read())
        self.set_header("Content-type",  "image/png")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

    app.listen()
    tornado.ioloop.IOLoop.current().start()