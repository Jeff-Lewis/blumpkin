from __future__ import unicode_literals

from . import TestCase, fixtures

from blumpkin import coverage


class CoverageTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path_to_fixture = fixtures.get_for_reals_path('coverage.xml')

    def test_coverage_deep(self):
        targets = {
            'precog_service.models.funding_instruments': 93,
            'precog_service.models.funding_instruments.cards': 93
        }
        package_failed = coverage.run_coverage(
            self.path_to_fixture, targets
        )
        self.assertFalse(package_failed)

    def test_coverage_fails(self):
        targets = {
            'precog_service.models.funding_instruments': 95,
            'missing_package': 95,
        }
        package_failed = coverage.run_coverage(
            self.path_to_fixture, targets
        )
        self.assertTrue(package_failed)

    def test_command(self):
        targets = (
            'precog_service:10',
        )
        coverage.handle_coverage(self.path_to_fixture, targets)
