from django.urls import path

from tom_demoapp.views import DemoView


app_name = 'tom_demoapp'

urlpatterns = [
    path('<int:pk>/demo', DemoView.as_view(), name='demo-page'),
]
