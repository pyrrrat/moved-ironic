# Copyright 2013 Hewlett-Packard Development Company, L.P.
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

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class ImageService(object):
    """Provides storage and retrieval of disk image objects within Glance."""

    @abc.abstractmethod
    def __init__(self):
        """Constructor."""

    @abc.abstractmethod
    def detail(self):
        """Calls out to Glance for a list of detailed image information."""

    @abc.abstractmethod
    def show(self, image_id):
        """Returns a dict with image data for the given opaque image id.

        :param image_id: The opaque image identifier.
        :returns: A dict containing image metadata.

        :raises: ImageNotFound
        """

    @abc.abstractmethod
    def download(self, image_id, data=None):
        """Calls out to Glance for data and writes data.

        :param image_id: The opaque image identifier.
        :param data: (Optional) File object to write data to.
        """

    @abc.abstractmethod
    def create(self, image_meta, data=None):
        """Store the image data and return the new image object.

        :param image_meta: A dict containing image metadata
        :param data: (Optional) File object to create image from.
        :returns: dict -- New created image metadata
        """

    @abc.abstractmethod
    def update(self, image_id,
               image_meta, data=None, purge_props=False):
        """Modify the given image with the new data.

        :param image_id: The opaque image identifier.
        :param data: (Optional) File object to update data from.
        :param purge_props: (Optional=True) Purge existing properties.
        :returns: dict -- New created image metadata
        """

    @abc.abstractmethod
    def delete(self, image_id):
        """Delete the given image.

        :param image_id: The opaque image identifier.

        :raises: ImageNotFound if the image does not exist.
        :raises: NotAuthorized if the user is not an owner.
        :raises: ImageNotAuthorized if the user is not authorized.

        """
