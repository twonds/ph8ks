# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiNodeV1alpha1RuntimeClass(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str=None, kind: str=None, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta=None, spec: IoK8sApiNodeV1alpha1RuntimeClassSpec=None):  # noqa: E501
        """IoK8sApiNodeV1alpha1RuntimeClass - a model defined in Swagger

        :param api_version: The api_version of this IoK8sApiNodeV1alpha1RuntimeClass.  # noqa: E501
        :type api_version: str
        :param kind: The kind of this IoK8sApiNodeV1alpha1RuntimeClass.  # noqa: E501
        :type kind: str
        :param metadata: The metadata of this IoK8sApiNodeV1alpha1RuntimeClass.  # noqa: E501
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        :param spec: The spec of this IoK8sApiNodeV1alpha1RuntimeClass.  # noqa: E501
        :type spec: IoK8sApiNodeV1alpha1RuntimeClassSpec
        """
        self.swagger_types = {
            'api_version': str,
            'kind': str,
            'metadata': IoK8sApimachineryPkgApisMetaV1ObjectMeta,
            'spec': IoK8sApiNodeV1alpha1RuntimeClassSpec
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'metadata': 'metadata',
            'spec': 'spec'
        }

        self._api_version = api_version
        self._kind = kind
        self._metadata = metadata
        self._spec = spec

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiNodeV1alpha1RuntimeClass':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.node.v1alpha1.RuntimeClass of this IoK8sApiNodeV1alpha1RuntimeClass.  # noqa: E501
        :rtype: IoK8sApiNodeV1alpha1RuntimeClass
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApiNodeV1alpha1RuntimeClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiNodeV1alpha1RuntimeClass.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApiNodeV1alpha1RuntimeClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiNodeV1alpha1RuntimeClass.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApiNodeV1alpha1RuntimeClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiNodeV1alpha1RuntimeClass.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApiNodeV1alpha1RuntimeClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiNodeV1alpha1RuntimeClass.
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self) -> IoK8sApimachineryPkgApisMetaV1ObjectMeta:
        """Gets the metadata of this IoK8sApiNodeV1alpha1RuntimeClass.

        More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this IoK8sApiNodeV1alpha1RuntimeClass.
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta):
        """Sets the metadata of this IoK8sApiNodeV1alpha1RuntimeClass.

        More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this IoK8sApiNodeV1alpha1RuntimeClass.
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self) -> IoK8sApiNodeV1alpha1RuntimeClassSpec:
        """Gets the spec of this IoK8sApiNodeV1alpha1RuntimeClass.

        Specification of the RuntimeClass More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status  # noqa: E501

        :return: The spec of this IoK8sApiNodeV1alpha1RuntimeClass.
        :rtype: IoK8sApiNodeV1alpha1RuntimeClassSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec: IoK8sApiNodeV1alpha1RuntimeClassSpec):
        """Sets the spec of this IoK8sApiNodeV1alpha1RuntimeClass.

        Specification of the RuntimeClass More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status  # noqa: E501

        :param spec: The spec of this IoK8sApiNodeV1alpha1RuntimeClass.
        :type spec: IoK8sApiNodeV1alpha1RuntimeClassSpec
        """
        if spec is None:
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec
