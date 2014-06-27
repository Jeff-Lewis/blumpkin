from __future__ import unicode_literals

import mock

from . import TestCase

from blumpkin import publish


class PublishTestCase(TestCase):

    @mock.patch('blumpkin.publish.call')
    @mock.patch('blumpkin.publish.os.environ')
    def test_publish_publish_branch(self, environ, call):
        environ.get.return_value = 'master'
        publish.publish.__dict__['callback']('master', 'index')
        self.assertTrue(call.called)

    @mock.patch('blumpkin.publish.call')
    @mock.patch('blumpkin.publish.os.environ')
    def test_publish_non_publish_branch(self, environ, call):
        environ.get.return_value = 'master'
        publish.publish.__dict__['callback']('not_master', 'index')
        self.assertFalse(call.called)

