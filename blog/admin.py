from django.contrib import admin

from .models import Blog
from .models import Author
from .models import Entry

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
