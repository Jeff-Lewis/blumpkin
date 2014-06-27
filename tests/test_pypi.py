from __future__ import unicode_literals

import mock

from . import TestCase

from blumpkin import pypi


class PyPiTestCase(TestCase):

    @mock.patch('os.mkdir')
    @mock.patch('blumpkin.pypi.click.echo')
    def test_write(self, echo, _):
        expected = [
            'wrote /tmp.pip/pip.conf',
            'wrote /tmp/.pypirc',
            'wrote /tmp/.pydistutils.cfg',
            'created pypi setup files'
        ]
        for dry in (True, False):
            echo.reset_mock()
            with mock.patch('blumpkin.pypi.open', create=True) as mock_open:
                mock_open.return_value = mock.MagicMock(spec=file)
                pypi.create_pypi.__dict__['callback'](
                    username='john',
                    password='pass',
                    index='index',
                    base_dir='/tmp',
                    server='server',
                    dry=dry
                )

            if not dry:
                self.assertItemsEqual(
                    [args[0] for args, _ in echo.call_args_list],
                    expected
                )
