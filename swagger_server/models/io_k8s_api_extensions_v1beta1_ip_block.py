# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiExtensionsV1beta1IPBlock(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, cidr: str=None, _except: List[str]=None):  # noqa: E501
        """IoK8sApiExtensionsV1beta1IPBlock - a model defined in Swagger

        :param cidr: The cidr of this IoK8sApiExtensionsV1beta1IPBlock.  # noqa: E501
        :type cidr: str
        :param _except: The _except of this IoK8sApiExtensionsV1beta1IPBlock.  # noqa: E501
        :type _except: List[str]
        """
        self.swagger_types = {
            'cidr': str,
            '_except': List[str]
        }

        self.attribute_map = {
            'cidr': 'cidr',
            '_except': 'except'
        }

        self._cidr = cidr
        self.__except = _except

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiExtensionsV1beta1IPBlock':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.extensions.v1beta1.IPBlock of this IoK8sApiExtensionsV1beta1IPBlock.  # noqa: E501
        :rtype: IoK8sApiExtensionsV1beta1IPBlock
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cidr(self) -> str:
        """Gets the cidr of this IoK8sApiExtensionsV1beta1IPBlock.

        CIDR is a string representing the IP Block Valid examples are \"192.168.1.1/24\"  # noqa: E501

        :return: The cidr of this IoK8sApiExtensionsV1beta1IPBlock.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr: str):
        """Sets the cidr of this IoK8sApiExtensionsV1beta1IPBlock.

        CIDR is a string representing the IP Block Valid examples are \"192.168.1.1/24\"  # noqa: E501

        :param cidr: The cidr of this IoK8sApiExtensionsV1beta1IPBlock.
        :type cidr: str
        """
        if cidr is None:
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501

        self._cidr = cidr

    @property
    def _except(self) -> List[str]:
        """Gets the _except of this IoK8sApiExtensionsV1beta1IPBlock.

        Except is a slice of CIDRs that should not be included within an IP Block Valid examples are \"192.168.1.1/24\" Except values will be rejected if they are outside the CIDR range  # noqa: E501

        :return: The _except of this IoK8sApiExtensionsV1beta1IPBlock.
        :rtype: List[str]
        """
        return self.__except

    @_except.setter
    def _except(self, _except: List[str]):
        """Sets the _except of this IoK8sApiExtensionsV1beta1IPBlock.

        Except is a slice of CIDRs that should not be included within an IP Block Valid examples are \"192.168.1.1/24\" Except values will be rejected if they are outside the CIDR range  # noqa: E501

        :param _except: The _except of this IoK8sApiExtensionsV1beta1IPBlock.
        :type _except: List[str]
        """

        self.__except = _except