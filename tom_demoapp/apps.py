from django.apps import AppConfig
from django.urls import path, include


class TomDemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tom_demoapp'  # Full Python path to the application, e.g. 'django.contrib.admin'
    short_name = 'demoapp'  # Short name for the application, e.g. 'admin'
    verbose_name = 'A Demo App for the TOM Toolkit'  # Human-readable name for the application, e.g. “Administration”.

    def target_detail_buttons(self):
        """
        Integration point for adding buttons to the target detail view.
        This method should return a list of dictionaries that include a `partial` key pointing to the path of the html
        profile partial. The `context` key is optional and should point to the dot separated string path to the
        templatetag that will return a dictionary containing new context for the accompanying partial.
        Typically, this partial will be a button or link referencing the current target.
        """
        return [{'partial': f'{self.name}/partials/demo_button.html',
                 'context': f'{self.name}.templatetags.demo_extras.demo_button'}]

    def nav_items(self):
        """
        Integration point for adding items to the navbar.
        This method should return a list of dictionaries that include a `partial` key pointing to the html templates to
        be included in the navbar. An optional `context` key may be included that should point to the dot separated
        string path to the templatetag that will return a dictionary containing new context for the accompanying
        partial. The `position` key, if included, should be either "left" or "right" to specify which
        side of the navbar the partial should be included on. If not included, a left side nav item is assumed.  We
        provide examples of both here.
        """
        # TODO: These filenames probably don't need 'demo' in them b/c they're namespaced in the app folder
        return [{'partial': f'{self.name}/partials/navbar_demo.html',
                 'position': 'right'
                 # 'context': f'{self.name}.templatetags.demo_extras.nav_context'
                 },
                {'partial': f'{self.name}/partials/navbar_list_demo.html'}]

    def include_url_paths(self):
        """
        Integration point for adding URL patterns to the Tom Common URL configuration.
        This method should return a list of URL patterns to be included in the main URL configuration.
        """
        urlpatterns = [
            path(f'{self.short_name}/', include(f'{self.name}.urls', namespace=f'{self.short_name}'))
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

    def target_detail_tabs(self):
        """
        Integration point for adding tabs to the target detail page.

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
        """
        integration point for including data services in the TOM
        This method should return a list of dictionaries containing dot separated DataService classes
        """
        return [{'class': f'{self.name}.demo_dataservice.DemoDataService'}]

    def observation_facilities(self):
        """
        Integration point for including observation facilities in the TOM.

        This method should return a list of dictionaries, one per facility.
        The keys and values of the configuration dictionary:
         - `class` (required): dot separated path to a Facility class (an extension of
           BaseRoboticObservationFacility or BaseManualObservationFacility).
         - `url` (optional): the namespaced Django URL name of the facility's landing page,
           used as its menu item in the navbar "Facilities" dropdown. Omit `url` for a facility
           with no landing page. It is still registered so there will be an observe button
           on the TargetDetail page and an ObservationCreateView with observation forms).
           However, without a `url` key:value, this facility gets no navbar menu item.

        Facilities listed here are combined with settings.TOM_FACILITY_CLASSES by
        ``tom_observations.facility.get_service_classes()``, so installing the app is all a
        TOM needs to do -- no settings changes required.
        """
        return [{'class': f'{self.name}.demo_facility.DemoFacility',
                 'url': f'{self.short_name}:facility-index'}]
