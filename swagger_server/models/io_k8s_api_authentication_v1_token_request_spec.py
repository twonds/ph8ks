# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiAuthenticationV1TokenRequestSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, audiences: List[str]=None, bound_object_ref: IoK8sApiAuthenticationV1BoundObjectReference=None, expiration_seconds: int=None):  # noqa: E501
        """IoK8sApiAuthenticationV1TokenRequestSpec - a model defined in Swagger

        :param audiences: The audiences of this IoK8sApiAuthenticationV1TokenRequestSpec.  # noqa: E501
        :type audiences: List[str]
        :param bound_object_ref: The bound_object_ref of this IoK8sApiAuthenticationV1TokenRequestSpec.  # noqa: E501
        :type bound_object_ref: IoK8sApiAuthenticationV1BoundObjectReference
        :param expiration_seconds: The expiration_seconds of this IoK8sApiAuthenticationV1TokenRequestSpec.  # noqa: E501
        :type expiration_seconds: int
        """
        self.swagger_types = {
            'audiences': List[str],
            'bound_object_ref': IoK8sApiAuthenticationV1BoundObjectReference,
            'expiration_seconds': int
        }

        self.attribute_map = {
            'audiences': 'audiences',
            'bound_object_ref': 'boundObjectRef',
            'expiration_seconds': 'expirationSeconds'
        }

        self._audiences = audiences
        self._bound_object_ref = bound_object_ref
        self._expiration_seconds = expiration_seconds

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiAuthenticationV1TokenRequestSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.authentication.v1.TokenRequestSpec of this IoK8sApiAuthenticationV1TokenRequestSpec.  # noqa: E501
        :rtype: IoK8sApiAuthenticationV1TokenRequestSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def audiences(self) -> List[str]:
        """Gets the audiences of this IoK8sApiAuthenticationV1TokenRequestSpec.

        Audiences are the intendend audiences of the token. A recipient of a token must identitfy themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.  # noqa: E501

        :return: The audiences of this IoK8sApiAuthenticationV1TokenRequestSpec.
        :rtype: List[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences: List[str]):
        """Sets the audiences of this IoK8sApiAuthenticationV1TokenRequestSpec.

        Audiences are the intendend audiences of the token. A recipient of a token must identitfy themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.  # noqa: E501

        :param audiences: The audiences of this IoK8sApiAuthenticationV1TokenRequestSpec.
        :type audiences: List[str]
        """
        if audiences is None:
            raise ValueError("Invalid value for `audiences`, must not be `None`")  # noqa: E501

        self._audiences = audiences

    @property
    def bound_object_ref(self) -> IoK8sApiAuthenticationV1BoundObjectReference:
        """Gets the bound_object_ref of this IoK8sApiAuthenticationV1TokenRequestSpec.

        BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.  # noqa: E501

        :return: The bound_object_ref of this IoK8sApiAuthenticationV1TokenRequestSpec.
        :rtype: IoK8sApiAuthenticationV1BoundObjectReference
        """
        return self._bound_object_ref

    @bound_object_ref.setter
    def bound_object_ref(self, bound_object_ref: IoK8sApiAuthenticationV1BoundObjectReference):
        """Sets the bound_object_ref of this IoK8sApiAuthenticationV1TokenRequestSpec.

        BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.  # noqa: E501

        :param bound_object_ref: The bound_object_ref of this IoK8sApiAuthenticationV1TokenRequestSpec.
        :type bound_object_ref: IoK8sApiAuthenticationV1BoundObjectReference
        """

        self._bound_object_ref = bound_object_ref

    @property
    def expiration_seconds(self) -> int:
        """Gets the expiration_seconds of this IoK8sApiAuthenticationV1TokenRequestSpec.

        ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.  # noqa: E501

        :return: The expiration_seconds of this IoK8sApiAuthenticationV1TokenRequestSpec.
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds: int):
        """Sets the expiration_seconds of this IoK8sApiAuthenticationV1TokenRequestSpec.

        ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.  # noqa: E501

        :param expiration_seconds: The expiration_seconds of this IoK8sApiAuthenticationV1TokenRequestSpec.
        :type expiration_seconds: int
        """

        self._expiration_seconds = expiration_seconds