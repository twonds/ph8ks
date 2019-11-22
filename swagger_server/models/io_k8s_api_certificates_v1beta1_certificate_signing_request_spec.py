# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, extra: Dict[str, List[str]]=None, groups: List[str]=None, request: ByteArray=None, uid: str=None, usages: List[str]=None, username: str=None):  # noqa: E501
        """IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec - a model defined in Swagger

        :param extra: The extra of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.  # noqa: E501
        :type extra: Dict[str, List[str]]
        :param groups: The groups of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.  # noqa: E501
        :type groups: List[str]
        :param request: The request of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.  # noqa: E501
        :type request: ByteArray
        :param uid: The uid of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.  # noqa: E501
        :type uid: str
        :param usages: The usages of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.  # noqa: E501
        :type usages: List[str]
        :param username: The username of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.  # noqa: E501
        :type username: str
        """
        self.swagger_types = {
            'extra': Dict[str, List[str]],
            'groups': List[str],
            'request': ByteArray,
            'uid': str,
            'usages': List[str],
            'username': str
        }

        self.attribute_map = {
            'extra': 'extra',
            'groups': 'groups',
            'request': 'request',
            'uid': 'uid',
            'usages': 'usages',
            'username': 'username'
        }

        self._extra = extra
        self._groups = groups
        self._request = request
        self._uid = uid
        self._usages = usages
        self._username = username

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.certificates.v1beta1.CertificateSigningRequestSpec of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extra(self) -> Dict[str, List[str]]:
        """Gets the extra of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        Extra information about the requesting user. See user.Info interface for details.  # noqa: E501

        :return: The extra of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :rtype: Dict[str, List[str]]
        """
        return self._extra

    @extra.setter
    def extra(self, extra: Dict[str, List[str]]):
        """Sets the extra of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        Extra information about the requesting user. See user.Info interface for details.  # noqa: E501

        :param extra: The extra of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :type extra: Dict[str, List[str]]
        """

        self._extra = extra

    @property
    def groups(self) -> List[str]:
        """Gets the groups of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        Group information about the requesting user. See user.Info interface for details.  # noqa: E501

        :return: The groups of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :rtype: List[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups: List[str]):
        """Sets the groups of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        Group information about the requesting user. See user.Info interface for details.  # noqa: E501

        :param groups: The groups of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :type groups: List[str]
        """

        self._groups = groups

    @property
    def request(self) -> ByteArray:
        """Gets the request of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        Base64-encoded PKCS#10 CSR data  # noqa: E501

        :return: The request of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :rtype: ByteArray
        """
        return self._request

    @request.setter
    def request(self, request: ByteArray):
        """Sets the request of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        Base64-encoded PKCS#10 CSR data  # noqa: E501

        :param request: The request of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :type request: ByteArray
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501
        if request is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', request):  # noqa: E501
            raise ValueError("Invalid value for `request`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._request = request

    @property
    def uid(self) -> str:
        """Gets the uid of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        UID information about the requesting user. See user.Info interface for details.  # noqa: E501

        :return: The uid of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid: str):
        """Sets the uid of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        UID information about the requesting user. See user.Info interface for details.  # noqa: E501

        :param uid: The uid of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :type uid: str
        """

        self._uid = uid

    @property
    def usages(self) -> List[str]:
        """Gets the usages of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        allowedUsages specifies a set of usage contexts the key will be valid for. See: https://tools.ietf.org/html/rfc5280#section-4.2.1.3      https://tools.ietf.org/html/rfc5280#section-4.2.1.12  # noqa: E501

        :return: The usages of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :rtype: List[str]
        """
        return self._usages

    @usages.setter
    def usages(self, usages: List[str]):
        """Sets the usages of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        allowedUsages specifies a set of usage contexts the key will be valid for. See: https://tools.ietf.org/html/rfc5280#section-4.2.1.3      https://tools.ietf.org/html/rfc5280#section-4.2.1.12  # noqa: E501

        :param usages: The usages of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :type usages: List[str]
        """

        self._usages = usages

    @property
    def username(self) -> str:
        """Gets the username of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        Information about the requesting user. See user.Info interface for details.  # noqa: E501

        :return: The username of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.

        Information about the requesting user. See user.Info interface for details.  # noqa: E501

        :param username: The username of this IoK8sApiCertificatesV1beta1CertificateSigningRequestSpec.
        :type username: str
        """

        self._username = username
