from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

import polls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls'))
]
