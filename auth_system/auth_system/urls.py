from django.contrib import admin
from django.urls import path, include  # Add include import
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include app's URLs
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

