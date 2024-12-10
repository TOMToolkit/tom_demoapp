from django.apps import AppConfig
from django.urls import path, include


class TomDemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tom_demoapp'
    label = 'demoapp'

    def target_detail_buttons(self):
        """
        Integration point for adding buttons to the target detail view.
        This method should return a list of dictionaries, each containing the keys:
        - 'namespace': The namespace of the app that provides the button's view
        - 'title': The title of the button
        - 'class': The CSS class of the button
        - 'text': The text of the button
        """
        return {'namespace': 'demoapp:demo-page',
                'title': 'Demo Page',
                'class': 'btn  btn-danger',
                'text': 'Demo',
                }

    def include_url_paths(self):
        """
        Integration point for adding URL patterns to the Tom Common URL configuration.
        This method should return a list of URL patterns to be included in the main URL configuration.
        """
        urlpatterns = [
            path('demoapp/', include('tom_demoapp.urls', namespace='demoapp'))
        ]
        return urlpatterns
