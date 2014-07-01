from __future__ import unicode_literals

import mock

from . import TestCase

from blumpkin import test


class TestTestCase(TestCase):

    @mock.patch('blumpkin.test.pytest')
    def test_write(self, pytest):
        result = test.run(
            'blumpkin', ('xml', 'term-missing'), 'tests/'
        )
        self.assertEqual(result, pytest.main.return_value)
