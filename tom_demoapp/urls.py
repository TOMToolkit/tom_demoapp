from django.urls import path
from django.views.generic.base import TemplateView

from tom_demoapp.apps import TomDemoappConfig
from tom_demoapp.views import DemoView, ProfileUpdateView


# app_name supplies the '<namespace>:' half of this app's URL names, e.g. {% url 'tom_demoapp:<name>' %}.
# Deriving app_name from the AppConfig.name means the namespace and the package name can never disagree.
app_name = TomDemoappConfig.name

urlpatterns = [
    path('<int:pk>/demo', DemoView.as_view(), name='demo-page'),
    path('', DemoView.as_view(), name='demo-page'),
    path('facility/', TemplateView.as_view(template_name='tom_demoapp/demo_page.html'), name='facility-detail'),
    path('users/<int:pk>/update/', ProfileUpdateView.as_view(), name='demo-profile-update'),
]
