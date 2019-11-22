# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1FlockerVolumeSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, dataset_name: str=None, dataset_uuid: str=None):  # noqa: E501
        """IoK8sApiCoreV1FlockerVolumeSource - a model defined in Swagger

        :param dataset_name: The dataset_name of this IoK8sApiCoreV1FlockerVolumeSource.  # noqa: E501
        :type dataset_name: str
        :param dataset_uuid: The dataset_uuid of this IoK8sApiCoreV1FlockerVolumeSource.  # noqa: E501
        :type dataset_uuid: str
        """
        self.swagger_types = {
            'dataset_name': str,
            'dataset_uuid': str
        }

        self.attribute_map = {
            'dataset_name': 'datasetName',
            'dataset_uuid': 'datasetUUID'
        }

        self._dataset_name = dataset_name
        self._dataset_uuid = dataset_uuid

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1FlockerVolumeSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.FlockerVolumeSource of this IoK8sApiCoreV1FlockerVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1FlockerVolumeSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dataset_name(self) -> str:
        """Gets the dataset_name of this IoK8sApiCoreV1FlockerVolumeSource.

        Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated  # noqa: E501

        :return: The dataset_name of this IoK8sApiCoreV1FlockerVolumeSource.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name: str):
        """Sets the dataset_name of this IoK8sApiCoreV1FlockerVolumeSource.

        Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated  # noqa: E501

        :param dataset_name: The dataset_name of this IoK8sApiCoreV1FlockerVolumeSource.
        :type dataset_name: str
        """

        self._dataset_name = dataset_name

    @property
    def dataset_uuid(self) -> str:
        """Gets the dataset_uuid of this IoK8sApiCoreV1FlockerVolumeSource.

        UUID of the dataset. This is unique identifier of a Flocker dataset  # noqa: E501

        :return: The dataset_uuid of this IoK8sApiCoreV1FlockerVolumeSource.
        :rtype: str
        """
        return self._dataset_uuid

    @dataset_uuid.setter
    def dataset_uuid(self, dataset_uuid: str):
        """Sets the dataset_uuid of this IoK8sApiCoreV1FlockerVolumeSource.

        UUID of the dataset. This is unique identifier of a Flocker dataset  # noqa: E501

        :param dataset_uuid: The dataset_uuid of this IoK8sApiCoreV1FlockerVolumeSource.
        :type dataset_uuid: str
        """

        self._dataset_uuid = dataset_uuid