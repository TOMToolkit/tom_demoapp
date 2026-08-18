from __future__ import annotations

from django.apps import AppConfig
from django.urls import path, include


class TomDemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # App names for internal use. `name` and `verbose_name` are used by Django, `short_name` is used by the TOMToolkit
    name = 'tom_demoapp'  # required by Django, the Python path to the app's package; from django-admin startapp
    verbose_name = 'A Demo App for the TOM Toolkit'  # optional, Django human-readable name for the application
    short_name = 'demoapp'  # Optional: This is most often used to remove the "tom" from self.name's "tom_****"

    route_prefix = 'short_name'  # useful to prefix the urlpatterns in urls.py. So, pages live at HOST:PORT/demoapp/...

    def target_detail_buttons(self):
        """Integration point for adding buttons to the target detail view.

        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        profile partial. The `context` key is optional and should point to the dot separated string path to the
        templatetag that will return a dictionary containing new context for the accompanying partial.
        Typically, this partial will be a button or link referencing the current target.
        """
        return [{'partial': f'{self.name}/partials/demo_button.html',
                 'context': f'{self.name}.templatetags.demo_extras.demo_button'}]

    def nav_items(self):
        """Integration point for adding items to the navbar.

        This method should return a list of dictionaries that include a `partial` key pointing to the html templates to
        be included in the navbar. An optional `context` key may be included that should point to the dot separated
        string path to the templatetag that will return a dictionary containing new context for the accompanying
        partial. The `position` key, if included, should be either "left" or "right" to specify which
        side of the navbar the partial should be included on. If not included, a left side nav item is assumed.  We
        provide examples of both here.
        """
        return [
            {'partial': f'{self.name}/partials/navbar_demo.html',
             'position': 'right'
             # 'context': f'{self.name}.templatetags.demo_extras.nav_context'
             },
            {'partial': f'{self.name}/partials/navbar_list_demo.html'}
        ]

    def include_url_paths(self):
        """Integration point for adding URL patterns to the Tom Common URL configuration.

        This method should return a list of URL patterns to be included in the main URL configuration.
        The implementation below uses ``include()`` to gather urlpatterns from ``urls.py``.

        Refer to your URLs in your templates as '<namespace>:<name>', like this:
        ```html
        {% url 'tom_demoapp:<name>' %}
        ```
        The ``<namespace>`` half of the URL name above comes from ``app_name`` in ``urls.py``
        and the ``<name>`` half is the ``name=`` argument passed to ``path()`` in your
        ``urls.py`` urlpatterns.
        """
        urlpatterns = [
            path(f'{self.route_prefix}/', include(f'{self.name}.urls'))
        ]
        return urlpatterns

    def profile_details(self):
        """Integration point for adding items to the user profile page.

        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        profile partial. The `context` key should point to the dot separated string path to the templatetag that will
        return a dictionary containing new context for the accompanying partial.
        Typically, this partial will be a bootstrap card displaying some app specific user data.
        """
        # TODO: see if 'demo' couldn't be removed from these filenames
        return [{'partial': f'{self.name}/partials/profile_demo.html',
                 'context': f'{self.name}.templatetags.demo_extras.demo_profile_data'}]

    def user_lists(self):
        """Integration point for adding items to the user list page.

        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        user_list partial. The `context` key should point to the dot separated string path to the templatetag that will
        return a dictionary containing new context for the accompanying partial.
        Typically, this partial will be a bootstrap table displaying some app specific user list or similar.

        """
        # TODO: see if 'demo' couldn't be removed from these filenames
        return [{'partial': f'{self.name}/partials/demo_user_list.html',
                 'context': f'{self.name}.templatetags.demo_extras.demo_user_list'}]

    def target_detail_tabs(self):
        """Integration point for adding tabs to the target detail page.

        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        target_detail_tab partial.
        The `context` key should point to the dot separated string path to the templatetag that will return a
        dictionary containing new context for the accompanying partial.
        The `label` key will represent the label string to put in the tab and use as a tab reference id.

        This partial will be displayed within the tab on the target detail page.

        """
        return [{'partial': f'{self.name}/partials/demo_partial.html',
                 'label': 'Demo Tab',
                 # 'context': f'{self.name}.templatetags.demo_extras.tab_context'
                 }]

    def data_services(self):
        """Integration point for including data services in the TOM.

        This method should return a list of dictionaries containing dot separated DataService classes
        """
        return [{'class': f'{self.name}.demo_dataservice.DemoDataService'}]

    def observation_facilities(self) -> list[dict[str, str]]:
        """Integration point for including this app's observation facilities in the TOM.

        Returns a list of ``{'class': <dot separated path to a Facility class>}`` dicts, consumed by
        ``tom_observations.facility.get_service_classes()``. Whether or not a facility gets a navbar
        menu item is declared on the facility class -- see ``demo_facility.py``.
        """
        return [{'class': f'{self.name}.demo_facility.DemoFacility'}]
