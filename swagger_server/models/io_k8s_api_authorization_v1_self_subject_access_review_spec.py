# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, non_resource_attributes: IoK8sApiAuthorizationV1NonResourceAttributes=None, resource_attributes: IoK8sApiAuthorizationV1ResourceAttributes=None):  # noqa: E501
        """IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec - a model defined in Swagger

        :param non_resource_attributes: The non_resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.  # noqa: E501
        :type non_resource_attributes: IoK8sApiAuthorizationV1NonResourceAttributes
        :param resource_attributes: The resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.  # noqa: E501
        :type resource_attributes: IoK8sApiAuthorizationV1ResourceAttributes
        """
        self.swagger_types = {
            'non_resource_attributes': IoK8sApiAuthorizationV1NonResourceAttributes,
            'resource_attributes': IoK8sApiAuthorizationV1ResourceAttributes
        }

        self.attribute_map = {
            'non_resource_attributes': 'nonResourceAttributes',
            'resource_attributes': 'resourceAttributes'
        }

        self._non_resource_attributes = non_resource_attributes
        self._resource_attributes = resource_attributes

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.authorization.v1.SelfSubjectAccessReviewSpec of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.  # noqa: E501
        :rtype: IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def non_resource_attributes(self) -> IoK8sApiAuthorizationV1NonResourceAttributes:
        """Gets the non_resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.

        NonResourceAttributes describes information for a non-resource access request  # noqa: E501

        :return: The non_resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.
        :rtype: IoK8sApiAuthorizationV1NonResourceAttributes
        """
        return self._non_resource_attributes

    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes: IoK8sApiAuthorizationV1NonResourceAttributes):
        """Sets the non_resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.

        NonResourceAttributes describes information for a non-resource access request  # noqa: E501

        :param non_resource_attributes: The non_resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.
        :type non_resource_attributes: IoK8sApiAuthorizationV1NonResourceAttributes
        """

        self._non_resource_attributes = non_resource_attributes

    @property
    def resource_attributes(self) -> IoK8sApiAuthorizationV1ResourceAttributes:
        """Gets the resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.

        ResourceAuthorizationAttributes describes information for a resource access request  # noqa: E501

        :return: The resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.
        :rtype: IoK8sApiAuthorizationV1ResourceAttributes
        """
        return self._resource_attributes

    @resource_attributes.setter
    def resource_attributes(self, resource_attributes: IoK8sApiAuthorizationV1ResourceAttributes):
        """Sets the resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.

        ResourceAuthorizationAttributes describes information for a resource access request  # noqa: E501

        :param resource_attributes: The resource_attributes of this IoK8sApiAuthorizationV1SelfSubjectAccessReviewSpec.
        :type resource_attributes: IoK8sApiAuthorizationV1ResourceAttributes
        """

        self._resource_attributes = resource_attributes