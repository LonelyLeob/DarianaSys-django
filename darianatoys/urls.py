from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/toys/', include('toys.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/purchase/', include('purchase.urls')),
    path('api/v1/user/', include('user.urls')),
    # path('api/v1/token/', TokenObtainPairView.as_view()),
    # path('api/v1/refresh/', TokenRefreshView.as_view()),
    # path('api/v1/verify/', TokenVerifyView.as_view()),
]