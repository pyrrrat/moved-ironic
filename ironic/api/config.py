# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# Server Specific Configurations
# See https://pecan.readthedocs.org/en/latest/configuration.html#server-configuration # noqa
server = {
    'port': '6385',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
# See https://pecan.readthedocs.org/en/latest/configuration.html#application-configuration # noqa
app = {
    'root': 'ironic.api.controllers.root.RootController',
    'modules': ['ironic.api'],
    'static_root': '%(confdir)s/public',
    'debug': False,
    'enable_acl': True,
    'acl_public_routes': [
        '/',
        '/v1',
        # IPA ramdisk methods
        '/v1/drivers/[a-z0-9_]*/vendor_passthru/lookup',
        '/v1/nodes/[a-z0-9\-]+/vendor_passthru/heartbeat',
        # DIB ramdisk methods
        # NOTE(yuriyz): support URL without 'v1' for backward compatibility
        # with old DIB ramdisks.
        '(?:/v1)?/nodes/[a-z0-9\-]+/vendor_passthru/pass_(?:deploy|'
        'bootloader_install)_info',
    ],
}

# WSME Configurations
# See https://wsme.readthedocs.org/en/latest/integrate.html#configuration
wsme = {
    'debug': False,
}
