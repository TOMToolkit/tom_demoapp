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
                'title': 'Demo Target Button',
                'class': 'btn  btn-danger',
                'text': 'Demo',
                }

    def nav_items(self):
        """
        Integration point for adding items to the navbar.
        This method should return a list of dictionaries that include a `partial` key pointing to the html templates to
        be included in the navbar. The `position` key, if included, should be either "left" or "right" to specify which
        side of the navbar the partial should be included on. If not included, a right side nav item is assumed.
        """
        return [{'partial': 'tom_demoapp/partials/navbar_demo.html', 'position': 'right'},
                {'partial': 'tom_demoapp/partials/navbar_list_demo.html'}]

    def include_url_paths(self):
        """
        Integration point for adding URL patterns to the Tom Common URL configuration.
        This method should return a list of URL patterns to be included in the main URL configuration.
        """
        urlpatterns = [
            path('demoapp/', include('tom_demoapp.urls', namespace='demoapp'))
        ]
        return urlpatterns

    def profile_details(self):
        """
        Integration point for adding items to the user profile page.

        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        profile partial. The `context` key should point to the dot separated string path to the templatetag that will
        return a dictionary containing new context for the accompanying partial.
        Typically, this partial will be a bootstrap card displaying some app specific user data.
        """
        return [{'partial': 'tom_demoapp/partials/profile_demo.html',
                 'context': 'tom_demoapp.templatetags.demo_extras.demo_profile_data'}]

    def user_lists(self):
        """
        Integration point for adding items to the user list page.

        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        user_list partial. The `context` key should point to the dot separated string path to the templatetag that will
        return a dictionary containing new context for the accompanying partial.
        Typically, this partial will be a bootstrap table displaying some app specific user list or similar.

        """
        return [{'partial': 'tom_demoapp/partials/demo_user_list.html',
                 'context': 'tom_demoapp.templatetags.demo_extras.demo_user_list'}]
