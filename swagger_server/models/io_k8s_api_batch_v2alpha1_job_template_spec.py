# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiBatchV2alpha1JobTemplateSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta=None, spec: IoK8sApiBatchV1JobSpec=None):  # noqa: E501
        """IoK8sApiBatchV2alpha1JobTemplateSpec - a model defined in Swagger

        :param metadata: The metadata of this IoK8sApiBatchV2alpha1JobTemplateSpec.  # noqa: E501
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        :param spec: The spec of this IoK8sApiBatchV2alpha1JobTemplateSpec.  # noqa: E501
        :type spec: IoK8sApiBatchV1JobSpec
        """
        self.swagger_types = {
            'metadata': IoK8sApimachineryPkgApisMetaV1ObjectMeta,
            'spec': IoK8sApiBatchV1JobSpec
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'spec': 'spec'
        }

        self._metadata = metadata
        self._spec = spec

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiBatchV2alpha1JobTemplateSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.batch.v2alpha1.JobTemplateSpec of this IoK8sApiBatchV2alpha1JobTemplateSpec.  # noqa: E501
        :rtype: IoK8sApiBatchV2alpha1JobTemplateSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> IoK8sApimachineryPkgApisMetaV1ObjectMeta:
        """Gets the metadata of this IoK8sApiBatchV2alpha1JobTemplateSpec.

        Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this IoK8sApiBatchV2alpha1JobTemplateSpec.
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta):
        """Sets the metadata of this IoK8sApiBatchV2alpha1JobTemplateSpec.

        Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this IoK8sApiBatchV2alpha1JobTemplateSpec.
        :type metadata: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self) -> IoK8sApiBatchV1JobSpec:
        """Gets the spec of this IoK8sApiBatchV2alpha1JobTemplateSpec.

        Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status  # noqa: E501

        :return: The spec of this IoK8sApiBatchV2alpha1JobTemplateSpec.
        :rtype: IoK8sApiBatchV1JobSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec: IoK8sApiBatchV1JobSpec):
        """Sets the spec of this IoK8sApiBatchV2alpha1JobTemplateSpec.

        Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status  # noqa: E501

        :param spec: The spec of this IoK8sApiBatchV2alpha1JobTemplateSpec.
        :type spec: IoK8sApiBatchV1JobSpec
        """

        self._spec = spec
