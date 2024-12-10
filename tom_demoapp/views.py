from django.views.generic.base import TemplateView


# Create your views here.


class DemoView(TemplateView):
    template_name = "tom_demoapp/demo_page.html"
