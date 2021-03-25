from django.contrib import admin
from .models import Tag,Problem,Solution,Comment
# Register your models here.
admin.site.register(Problem)
admin.site.register(Tag)
admin.site.register(Solution)
admin.site.register(Comment)