from django.urls import path

from tom_demoapp.views import DemoView, ProfileUpdateView


app_name = 'tom_demoapp'

urlpatterns = [
    path('<int:pk>/demo', DemoView.as_view(), name='demo-page'),
    path('', DemoView.as_view(), name='demo-page'),
    path('users/<int:pk>/update/', ProfileUpdateView.as_view(), name='demo-profile-update'),
]
