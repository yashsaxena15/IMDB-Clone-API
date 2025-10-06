from django.contrib import admin
# from .models import movie
from .models import StreamPlatform, WatchList,Review
# Register your models here.

# admin.site.register(movie)
admin.site.register(StreamPlatform)
admin.site.register(WatchList)
admin.site.register(Review)

