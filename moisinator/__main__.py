import web

from urls import urls
from base import Index

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()