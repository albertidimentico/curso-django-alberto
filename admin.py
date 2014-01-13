from django.contrib import admin
from models import Post


admin.site.register(Post)

class Media:
    js = (
        '/static/tiny_mce/tiny_mce.js',
        '/static/tiny_mce/textarea.js',
        )
