# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiStorageV1beta1VolumeAttachmentSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, attacher: str=None, node_name: str=None, source: IoK8sApiStorageV1beta1VolumeAttachmentSource=None):  # noqa: E501
        """IoK8sApiStorageV1beta1VolumeAttachmentSpec - a model defined in Swagger

        :param attacher: The attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :type attacher: str
        :param node_name: The node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :type node_name: str
        :param source: The source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :type source: IoK8sApiStorageV1beta1VolumeAttachmentSource
        """
        self.swagger_types = {
            'attacher': str,
            'node_name': str,
            'source': IoK8sApiStorageV1beta1VolumeAttachmentSource
        }

        self.attribute_map = {
            'attacher': 'attacher',
            'node_name': 'nodeName',
            'source': 'source'
        }

        self._attacher = attacher
        self._node_name = node_name
        self._source = source

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiStorageV1beta1VolumeAttachmentSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.storage.v1beta1.VolumeAttachmentSpec of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :rtype: IoK8sApiStorageV1beta1VolumeAttachmentSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attacher(self) -> str:
        """Gets the attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().  # noqa: E501

        :return: The attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.
        :rtype: str
        """
        return self._attacher

    @attacher.setter
    def attacher(self, attacher: str):
        """Sets the attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().  # noqa: E501

        :param attacher: The attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.
        :type attacher: str
        """
        if attacher is None:
            raise ValueError("Invalid value for `attacher`, must not be `None`")  # noqa: E501

        self._attacher = attacher

    @property
    def node_name(self) -> str:
        """Gets the node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        The node that the volume should be attached to.  # noqa: E501

        :return: The node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name: str):
        """Sets the node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        The node that the volume should be attached to.  # noqa: E501

        :param node_name: The node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.
        :type node_name: str
        """
        if node_name is None:
            raise ValueError("Invalid value for `node_name`, must not be `None`")  # noqa: E501

        self._node_name = node_name

    @property
    def source(self) -> IoK8sApiStorageV1beta1VolumeAttachmentSource:
        """Gets the source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        Source represents the volume that should be attached.  # noqa: E501

        :return: The source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.
        :rtype: IoK8sApiStorageV1beta1VolumeAttachmentSource
        """
        return self._source

    @source.setter
    def source(self, source: IoK8sApiStorageV1beta1VolumeAttachmentSource):
        """Sets the source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        Source represents the volume that should be attached.  # noqa: E501

        :param source: The source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.
        :type source: IoK8sApiStorageV1beta1VolumeAttachmentSource
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source
