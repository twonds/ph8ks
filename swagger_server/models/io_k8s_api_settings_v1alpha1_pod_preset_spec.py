# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiSettingsV1alpha1PodPresetSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, env: List[IoK8sApiCoreV1EnvVar]=None, env_from: List[IoK8sApiCoreV1EnvFromSource]=None, selector: IoK8sApimachineryPkgApisMetaV1LabelSelector=None, volume_mounts: List[IoK8sApiCoreV1VolumeMount]=None, volumes: List[IoK8sApiCoreV1Volume]=None):  # noqa: E501
        """IoK8sApiSettingsV1alpha1PodPresetSpec - a model defined in Swagger

        :param env: The env of this IoK8sApiSettingsV1alpha1PodPresetSpec.  # noqa: E501
        :type env: List[IoK8sApiCoreV1EnvVar]
        :param env_from: The env_from of this IoK8sApiSettingsV1alpha1PodPresetSpec.  # noqa: E501
        :type env_from: List[IoK8sApiCoreV1EnvFromSource]
        :param selector: The selector of this IoK8sApiSettingsV1alpha1PodPresetSpec.  # noqa: E501
        :type selector: IoK8sApimachineryPkgApisMetaV1LabelSelector
        :param volume_mounts: The volume_mounts of this IoK8sApiSettingsV1alpha1PodPresetSpec.  # noqa: E501
        :type volume_mounts: List[IoK8sApiCoreV1VolumeMount]
        :param volumes: The volumes of this IoK8sApiSettingsV1alpha1PodPresetSpec.  # noqa: E501
        :type volumes: List[IoK8sApiCoreV1Volume]
        """
        self.swagger_types = {
            'env': List[IoK8sApiCoreV1EnvVar],
            'env_from': List[IoK8sApiCoreV1EnvFromSource],
            'selector': IoK8sApimachineryPkgApisMetaV1LabelSelector,
            'volume_mounts': List[IoK8sApiCoreV1VolumeMount],
            'volumes': List[IoK8sApiCoreV1Volume]
        }

        self.attribute_map = {
            'env': 'env',
            'env_from': 'envFrom',
            'selector': 'selector',
            'volume_mounts': 'volumeMounts',
            'volumes': 'volumes'
        }

        self._env = env
        self._env_from = env_from
        self._selector = selector
        self._volume_mounts = volume_mounts
        self._volumes = volumes

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiSettingsV1alpha1PodPresetSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.settings.v1alpha1.PodPresetSpec of this IoK8sApiSettingsV1alpha1PodPresetSpec.  # noqa: E501
        :rtype: IoK8sApiSettingsV1alpha1PodPresetSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def env(self) -> List[IoK8sApiCoreV1EnvVar]:
        """Gets the env of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        Env defines the collection of EnvVar to inject into containers.  # noqa: E501

        :return: The env of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :rtype: List[IoK8sApiCoreV1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env: List[IoK8sApiCoreV1EnvVar]):
        """Sets the env of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        Env defines the collection of EnvVar to inject into containers.  # noqa: E501

        :param env: The env of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :type env: List[IoK8sApiCoreV1EnvVar]
        """

        self._env = env

    @property
    def env_from(self) -> List[IoK8sApiCoreV1EnvFromSource]:
        """Gets the env_from of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        EnvFrom defines the collection of EnvFromSource to inject into containers.  # noqa: E501

        :return: The env_from of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :rtype: List[IoK8sApiCoreV1EnvFromSource]
        """
        return self._env_from

    @env_from.setter
    def env_from(self, env_from: List[IoK8sApiCoreV1EnvFromSource]):
        """Sets the env_from of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        EnvFrom defines the collection of EnvFromSource to inject into containers.  # noqa: E501

        :param env_from: The env_from of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :type env_from: List[IoK8sApiCoreV1EnvFromSource]
        """

        self._env_from = env_from

    @property
    def selector(self) -> IoK8sApimachineryPkgApisMetaV1LabelSelector:
        """Gets the selector of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        Selector is a label query over a set of resources, in this case pods. Required.  # noqa: E501

        :return: The selector of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :rtype: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector: IoK8sApimachineryPkgApisMetaV1LabelSelector):
        """Sets the selector of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        Selector is a label query over a set of resources, in this case pods. Required.  # noqa: E501

        :param selector: The selector of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :type selector: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """

        self._selector = selector

    @property
    def volume_mounts(self) -> List[IoK8sApiCoreV1VolumeMount]:
        """Gets the volume_mounts of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        VolumeMounts defines the collection of VolumeMount to inject into containers.  # noqa: E501

        :return: The volume_mounts of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :rtype: List[IoK8sApiCoreV1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts: List[IoK8sApiCoreV1VolumeMount]):
        """Sets the volume_mounts of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        VolumeMounts defines the collection of VolumeMount to inject into containers.  # noqa: E501

        :param volume_mounts: The volume_mounts of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :type volume_mounts: List[IoK8sApiCoreV1VolumeMount]
        """

        self._volume_mounts = volume_mounts

    @property
    def volumes(self) -> List[IoK8sApiCoreV1Volume]:
        """Gets the volumes of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        Volumes defines the collection of Volume to inject into the pod.  # noqa: E501

        :return: The volumes of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :rtype: List[IoK8sApiCoreV1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes: List[IoK8sApiCoreV1Volume]):
        """Sets the volumes of this IoK8sApiSettingsV1alpha1PodPresetSpec.

        Volumes defines the collection of Volume to inject into the pod.  # noqa: E501

        :param volumes: The volumes of this IoK8sApiSettingsV1alpha1PodPresetSpec.
        :type volumes: List[IoK8sApiCoreV1Volume]
        """

        self._volumes = volumes