"""A minimal example of a TOM Toolkit observation facility.

This module demonstrates the smallest example of a facility plugin:
  * a Form class defining the facility-specific observation parameters, and
  * a Facility class that the toolkit discovers via the ``observation_facilities()``
    AppConfig integration point (see ``apps.py``).

For a real-world example (credentials via user profiles, an external API,
target synchronization, etc), see ``tom_cfht``, ``tom_lt``, ``tom_swift`` plugins et al.
"""
from __future__ import annotations

from crispy_forms.layout import Layout
from django import forms

from tom_observations.facility import BaseRoboticObservationFacility, BaseRoboticObservationForm


class DemoFacilityForm(BaseRoboticObservationForm):
    """The observation-request form for the DemoFacility.

    Add one form field per parameter your facility's observation request needs.
    The base class contributes the common hidden fields (facility, target_id,
    observation_type) and the submit buttons.
    """
    exposure_time = forms.IntegerField(min_value=1, help_text='Exposure time in seconds.')
    exposure_count = forms.IntegerField(min_value=1, initial=1, help_text='Number of exposures.')

    def layout(self) -> Layout:
        """Return the crispy-forms Layout for the facility-specific fields."""
        return Layout(
            'exposure_time',
            'exposure_count',
        )


class DemoFacility(BaseRoboticObservationFacility):
    """A do-nothing observation facility demonstrating the required interface.

    Every method below is required by the base class; a real facility would talk
    to the observatory's API in ``submit_observation()`` / ``validate_observation()``
    and report real state in ``get_observation_status()``.
    """
    name = 'DemoFacility'
    template_name = 'tom_demoapp/observation_form.html'  # override default with simple, stub
    observation_types: list[tuple[str, str]] = [
        ('OBSERVATION', 'Demo Observation'),
    ]
    observation_forms: dict[str, type[BaseRoboticObservationForm]] = {
        'OBSERVATION': DemoFacilityForm,
    }

    def get_form(self, observation_type: str | None) -> type[BaseRoboticObservationForm]:
        """Return the observation form class for ``observation_type``."""
        if observation_type is None:
            return DemoFacilityForm
        return self.observation_forms.get(observation_type, DemoFacilityForm)

    def submit_observation(self, observation_payload) -> list:
        """Submit the observation to the facility; return a list of observation ids.

        A real facility POSTs ``observation_payload`` to the observatory API here.
        """
        return []

    def validate_observation(self, observation_payload) -> list:
        """Dry-run counterpart of submit_observation(); return a list of errors."""
        return []

    def get_observation_status(self, observation_id: str) -> dict:
        """Return {'state': ..., 'scheduled_start': ..., 'scheduled_end': ...}."""
        return {'state': 'PENDING', 'scheduled_start': None, 'scheduled_end': None}

    def get_terminal_observing_states(self) -> list[str]:
        """States from which an observation can no longer change."""
        return ['COMPLETED', 'CANCELED']

    def get_observing_sites(self) -> dict[str, dict]:
        """Site(s) for the visibility planner: sitecode, latitude, longitude, elevation."""
        return {
            'Demo Site': {
                'sitecode': 'demo',
                'latitude': 0.0,
                'longitude': 0.0,
                'elevation': 0,
            }
        }

    def get_observation_url(self, observation_id: str) -> str:
        """URL of this observation's page at the facility, if it has one."""
        return ''

    def data_products(self, observation_id: str, product_id: str | None = None) -> list:
        """Data products the facility has for this observation (none, for the demo)."""
        return []
