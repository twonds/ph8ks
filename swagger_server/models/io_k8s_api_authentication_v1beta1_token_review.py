# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuthenticationV1beta1TokenReview(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str=None, kind: str=None, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta=None, spec: IoK8sApiAuthenticationV1beta1TokenReviewSpec=None, status: IoK8sApiAuthenticationV1beta1TokenReviewStatus=None):  # noqa: E501
        """IoK8sApiAuthenticationV1beta1TokenReview - a model defined in Swagger

        :param api_version: The api_version of this IoK8sApiAuthenticationV1beta1TokenReview.  # noqa: E501
        :type api_version: str
        :param kind: The kind of this IoK8sApiAuthenticationV1beta1TokenReview.  # noqa: E501
        :type kind: str
        :param metadata: The metadata of this IoK8sApiAuthenticationV1beta1TokenReview.  # noqa: E501
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        :param spec: The spec of this IoK8sApiAuthenticationV1beta1TokenReview.  # noqa: E501
        :type spec: IoK8sApiAuthenticationV1beta1TokenReviewSpec
        :param status: The status of this IoK8sApiAuthenticationV1beta1TokenReview.  # noqa: E501
        :type status: IoK8sApiAuthenticationV1beta1TokenReviewStatus
        """
        self.swagger_types = {
            'api_version': str,
            'kind': str,
            'metadata': IoK8sApimachineryPkgApisMetaV1ObjectMeta,
            'spec': IoK8sApiAuthenticationV1beta1TokenReviewSpec,
            'status': IoK8sApiAuthenticationV1beta1TokenReviewStatus
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'metadata': 'metadata',
            'spec': 'spec',
            'status': 'status'
        }

        self._api_version = api_version
        self._kind = kind
        self._metadata = metadata
        self._spec = spec
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuthenticationV1beta1TokenReview':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.authentication.v1beta1.TokenReview of this IoK8sApiAuthenticationV1beta1TokenReview.  # noqa: E501
        :rtype: IoK8sApiAuthenticationV1beta1TokenReview
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this IoK8sApiAuthenticationV1beta1TokenReview.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiAuthenticationV1beta1TokenReview.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this IoK8sApiAuthenticationV1beta1TokenReview.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiAuthenticationV1beta1TokenReview.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApiAuthenticationV1beta1TokenReview.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiAuthenticationV1beta1TokenReview.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApiAuthenticationV1beta1TokenReview.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiAuthenticationV1beta1TokenReview.
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self) -> IoK8sApimachineryPkgApisMetaV1ObjectMeta:
        """Gets the metadata of this IoK8sApiAuthenticationV1beta1TokenReview.


        :return: The metadata of this IoK8sApiAuthenticationV1beta1TokenReview.
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta):
        """Sets the metadata of this IoK8sApiAuthenticationV1beta1TokenReview.


        :param metadata: The metadata of this IoK8sApiAuthenticationV1beta1TokenReview.
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self) -> IoK8sApiAuthenticationV1beta1TokenReviewSpec:
        """Gets the spec of this IoK8sApiAuthenticationV1beta1TokenReview.

        Spec holds information about the request being evaluated  # noqa: E501

        :return: The spec of this IoK8sApiAuthenticationV1beta1TokenReview.
        :rtype: IoK8sApiAuthenticationV1beta1TokenReviewSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec: IoK8sApiAuthenticationV1beta1TokenReviewSpec):
        """Sets the spec of this IoK8sApiAuthenticationV1beta1TokenReview.

        Spec holds information about the request being evaluated  # noqa: E501

        :param spec: The spec of this IoK8sApiAuthenticationV1beta1TokenReview.
        :type spec: IoK8sApiAuthenticationV1beta1TokenReviewSpec
        """
        if spec is None:
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    @property
    def status(self) -> IoK8sApiAuthenticationV1beta1TokenReviewStatus:
        """Gets the status of this IoK8sApiAuthenticationV1beta1TokenReview.

        Status is filled in by the server and indicates whether the request can be authenticated.  # noqa: E501

        :return: The status of this IoK8sApiAuthenticationV1beta1TokenReview.
        :rtype: IoK8sApiAuthenticationV1beta1TokenReviewStatus
        """
        return self._status

    @status.setter
    def status(self, status: IoK8sApiAuthenticationV1beta1TokenReviewStatus):
        """Sets the status of this IoK8sApiAuthenticationV1beta1TokenReview.

        Status is filled in by the server and indicates whether the request can be authenticated.  # noqa: E501

        :param status: The status of this IoK8sApiAuthenticationV1beta1TokenReview.
        :type status: IoK8sApiAuthenticationV1beta1TokenReviewStatus
        """

        self._status = status