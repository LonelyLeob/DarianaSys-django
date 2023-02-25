from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/toys/', include('toys.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/purchase/', include('purchase.urls'))
]
