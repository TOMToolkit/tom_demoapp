from django.test import tag, TestCase
from django.urls import reverse

from tom_observations.facility import get_service_classes
from tom_observations.templatetags.observation_extras import observation_facilities_list

from tom_demoapp.demo_facility import DemoFacility


class TestDummy(TestCase):
    """
    This is just a dummy test to make sure the testing infrastructure is working.
    """

    def test_dummy(self):
        assert True


@tag('canary')
class TestDummyCanary(TestCase):
    """
    This is just a dummy test to make sure the testing infrastructure is working.
    """

    def test_dummy_canary(self):
        assert True


class TestObservationFacilitiesIntegrationPoint(TestCase):
    """The observation_facilities() AppConfig integration point (see apps.py)."""

    def test_demo_facility_auto_registers(self):
        # installing the app is enough: no TOM_FACILITY_CLASSES settings entry needed
        self.assertIn('DemoFacility', get_service_classes())

    def test_navbar_facilities_menu_lists_demo_facility(self):
        context = observation_facilities_list({})
        facility_names = [facility['name'] for facility in context['observation_facilities']]
        self.assertIn('DemoFacility', facility_names)

    def test_facility_detail_page_renders(self):
        response = self.client.get(reverse('tom_demoapp:facility-detail'))
        self.assertContains(response, 'DemoFacility')

    def test_detail_url_name_resolves(self):
        """DemoFacility.detail_url_name must reverse to the mounted detail page --
        its namespace half is urls.py's app_name, derived from the AppConfig's name."""
        self.assertEqual(reverse(DemoFacility.detail_url_name), '/demoapp/facility/')
