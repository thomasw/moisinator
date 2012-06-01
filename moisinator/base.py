import os

import web

from settings import SITE_ROOT

render = web.template.render(os.path.join(SITE_ROOT, 'templates'))

class Index:
    def GET(self):
        return render.index()