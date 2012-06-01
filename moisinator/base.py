import os

import requests
import web

from settings import SITE_ROOT, DROPBOX_BASE_URL

render = web.template.render(os.path.join(SITE_ROOT, 'templates'))

class Index:
    def GET(self, image):
        if not image:
            return render.index()
        
        return self.render_image("%s%s" % (DROPBOX_BASE_URL, image))
    
    def render_image(self, image):
        image = requests.get(image)
        image.is_image = image.headers['content-type'].startswith('image')
        
        if image.status_code != 200 and not image.is_image:
            raise web.notfound()
        
        return image.content
