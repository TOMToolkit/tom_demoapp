from django import forms

from tom_dataservices.dataservices import DataService
from tom_dataservices.forms import BaseQueryForm


class DemoServiceForm(BaseQueryForm):
    first_field = forms.CharField(required=False,
                                  label='An Example Field',
                                  help_text='Put important info here.')


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
