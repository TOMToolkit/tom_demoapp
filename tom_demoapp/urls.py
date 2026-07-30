from django.urls import path
from django.views.generic.base import TemplateView

from tom_demoapp.views import DemoView, ProfileUpdateView


app_name = 'tom_demoapp'

urlpatterns = [
    path('<int:pk>/demo', DemoView.as_view(), name='demo-page'),
    path('', DemoView.as_view(), name='demo-page'),

    # DemoFacility index page, linked from the navbar "Facilities" menu (see TomDemoappConfig.observation_facilities())
    path('facility/', TemplateView.as_view(template_name='tom_demoapp/facility_index.html'), name='facility-index'),

    path('users/<int:pk>/update/', ProfileUpdateView.as_view(), name='demo-profile-update'),
]
