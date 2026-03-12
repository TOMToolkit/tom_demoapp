from django import forms

from tom_dataservices.dataservices import DataService
from tom_dataservices.forms import BaseQueryForm


class DemoServiceForm(BaseQueryForm):
    first_field = forms.CharField(required=False,
                                  label='An Example Field',
                                  help_text='Put important info here.')
    ra = forms.FloatField(required=False, min_value=0., max_value=360.,
                            label='R.A.',
                            help_text='Right ascension in degrees')
    dec = forms.FloatField(required=False, min_value=-90., max_value=90.,
                        label='Dec.',
                        help_text='Declination in degrees')
    radius = forms.FloatField(required=False, min_value=0.,
                        label='Cone Radius')

    def simple_fields(self):
        """Return List of fields to be included in the simple form."""
        return ['first_field']


class DemoDataService(DataService):
    """
    This is an Example Data Service with the minimum required
    functionality.
    """
    name = 'DemoDataService'

    @classmethod
    def get_form_class(cls):
        """
        Points to the form class discussed below.
        """
        return DemoServiceForm

    def build_query_parameters(self, parameters, **kwargs):
        """
        Use this function to convert the form results into the query parameters understood
        by the Data Service.
        """
        return self.query_parameters

    def query_service(self, data, **kwargs):
        """
        This is where you actually make the call to the Data Service.
        Return the results.
        """
        return self.query_results
