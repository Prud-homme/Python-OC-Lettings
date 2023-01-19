from django.contrib import admin
from django.urls import include, path

from views import index, trigger_error

urlpatterns = [
    path('', index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error, name='sentry-debug'),
]
