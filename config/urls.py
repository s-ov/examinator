from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('examinator.urls')),
    path('scoreboard/', include('scoreboard.urls')),
    path('workflow/', include('workflow.urls')),
]
