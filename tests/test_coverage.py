from __future__ import unicode_literals

from . import TestCase, fixtures

from blumpkin import coverage


class CoverageTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path_to_fixture = fixtures.get_for_reals_path('coverage.xml')

    def test_coverage_deep(self):
        targets = {
            'precog_service.models.funding_instruments': 94,
            'precog_service.models.funding_instruments.cards': 96
        }
        file_failed, package_failed = coverage.run_coverage(
            self.path_to_fixture, targets, False, False
        )
        self.assertFalse(file_failed)
        self.assertFalse(package_failed)

    def test_coverage_fails(self):
        targets = {
            'precog_service.models.funding_instruments': 95,
        }
        file_failed, package_failed = coverage.run_coverage(
            self.path_to_fixture, targets, False, False
        )
        self.assertTrue(package_failed)
