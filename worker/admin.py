from django.contrib import admin
from .models import Worker
from .models import Comment
from .models import Resume

admin.site.register(Worker)
admin.site.register(Comment)
admin.site.register(Resume)
