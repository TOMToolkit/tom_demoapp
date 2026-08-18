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
