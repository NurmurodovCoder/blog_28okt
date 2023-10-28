from django.contrib import admin
from .models import Post, Person, Tag, Contact, Comments, Category

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Comments)
admin.site.register(Category)
