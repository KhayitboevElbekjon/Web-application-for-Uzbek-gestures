from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('adminn/', admin.site.urls),
    path('', Home.as_view()),
    path('sozlar/<int:pk>', SozlarView.as_view()),
    path('OneSoz/<int:pk>', OneSozView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
