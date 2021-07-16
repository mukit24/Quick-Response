from django.contrib import admin
from .models import Tag,Problem,Solution,Comment,Voter
# Register your models here.
admin.site.register(Problem)
admin.site.register(Tag)
admin.site.register(Solution)
admin.site.register(Comment)
admin.site.register(Voter)