from django.apps import AppConfig
from django.urls import path, include


class TomDemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tom_demoapp'  # Full Python path to the application, e.g. 'django.contrib.admin'
    label = 'demoapp'  # Short name for the application, e.g. 'admin' WARNING: used in database tables and migrations
    verbose_name = 'A Demo App for the TOM Toolkit'  # Human-readable name for the application, e.g. “Administration”.

    def target_detail_buttons(self):
        """
        Integration point for adding buttons to the target detail view.
        This method should return a list of dictionaries, each containing the keys:
        - 'namespace': The namespace of the app that provides the button's view
        - 'title': The title of the button
        - 'class': The CSS class of the button
        - 'text': The text of the button
        """
        return {'namespace': f'{self.label}:demo-page',
                'title': f'{self.label} Target Button',
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
        # TODO: These filenames probably don't need 'demo' in them b/c they're namespaced in the app folder
        return [{'partial': f'{self.name}/partials/navbar_demo.html', 'position': 'right'},
                {'partial': f'{self.name}/partials/navbar_list_demo.html'}]

    def include_url_paths(self):
        """
        Integration point for adding URL patterns to the Tom Common URL configuration.
        This method should return a list of URL patterns to be included in the main URL configuration.
        """
        urlpatterns = [
            path(f'{self.label}/', include(f'{self.name}.urls', namespace=f'{self.label}'))
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
        # TODO: see if 'demo' couldn't be removed from these filenames
        return [{'partial': f'{self.name}/partials/profile_demo.html',
                 'context': f'{self.name}.templatetags.demo_extras.demo_profile_data'}]

    def user_lists(self):
        """
        Integration point for adding items to the user list page.

        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        user_list partial. The `context` key should point to the dot separated string path to the templatetag that will
        return a dictionary containing new context for the accompanying partial.
        Typically, this partial will be a bootstrap table displaying some app specific user list or similar.

        """
        # TODO: see if 'demo' couldn't be removed from these filenames
        return [{'partial': f'{self.name}/partials/demo_user_list.html',
                 'context': f'{self.name}.templatetags.demo_extras.demo_user_list'}]
