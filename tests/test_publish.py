from __future__ import unicode_literals

import mock

from . import TestCase

from blumpkin import publish


class PublishTestCase(TestCase):

    @mock.patch('blumpkin.publish.call')
    @mock.patch('blumpkin.publish.os.environ')
    def test_publish_publish_branch(self, environ, call):
        environ.get.return_value = 'master'
        publish.publish.__dict__['callback']('master', 'index', False)
        self.assertTrue(call.called)

    @mock.patch('blumpkin.publish.call')
    @mock.patch('blumpkin.publish.os.environ')
    def test_publish_non_publish_branch(self, environ, call):
        environ.get.return_value = 'master'
        publish.publish.__dict__['callback']('not_master', 'index', False)
        self.assertFalse(call.called)

    @mock.patch('blumpkin.publish.call')
    @mock.patch('blumpkin.publish.os.environ')
    @mock.patch('blumpkin.publish.check_output')
    def test_publish_tag(self, check_output, environ, call):
        environ.get.return_value = 'v0.0.1'
        check_output.return_value = '0.0.1'
        publish.publish.__dict__['callback']('master', 'index', True)
        self.assertTrue(call.called)

    @mock.patch('blumpkin.publish.call')
    @mock.patch('blumpkin.publish.os.environ')
    @mock.patch('blumpkin.publish.check_output')
    def test_publish_tag_missmatch(self, check_output, environ, call):
        environ.get.return_value = 'v0.0.2'
        check_output.return_value = '0.0.1'
        publish.publish.__dict__['callback']('master', 'index', True)
        self.assertFalse(call.called)
