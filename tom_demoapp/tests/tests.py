from django.test import tag, TestCase


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
        from tom_observations.facility import get_service_classes
        self.assertIn('DemoFacility', get_service_classes())

    def test_navbar_facilities_menu_lists_demo_facility(self):
        from tom_observations.templatetags.observation_extras import observation_facilities_list
        context = observation_facilities_list({})
        facility_names = [facility['name'] for facility in context['observation_facilities']]
        self.assertIn('DemoFacility', facility_names)

    def test_facility_landing_page_renders(self):
        from django.urls import reverse
        response = self.client.get(reverse('demoapp:facility-index'))
        self.assertContains(response, 'DemoFacility')
