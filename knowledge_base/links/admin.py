from django.contrib import admin

# Register your models here.
from links.models import Articles, Tag, Category, User

admin.site.register(Articles)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(User)


