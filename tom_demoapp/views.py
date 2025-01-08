from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from tom_demoapp.models import DemoProfile


# Create your views here.


class DemoView(TemplateView):
    """
    Generic demo view
    """
    template_name = "tom_demoapp/demo_page.html"


class ProfileUpdateView(UpdateView):
    """
    View that handles updating of a user's ``DemoProfile``.
    """
    model = DemoProfile
    fields = ['demo_secret', 'demo_field']
    template_name = 'tom_demoapp/update_profile.html'

    def get_success_url(self):
        return reverse_lazy('user-profile')
