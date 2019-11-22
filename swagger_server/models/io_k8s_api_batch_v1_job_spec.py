# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiBatchV1JobSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, active_deadline_seconds: int=None, backoff_limit: int=None, completions: int=None, manual_selector: bool=None, parallelism: int=None, selector: IoK8sApimachineryPkgApisMetaV1LabelSelector=None, template: IoK8sApiCoreV1PodTemplateSpec=None, ttl_seconds_after_finished: int=None):  # noqa: E501
        """IoK8sApiBatchV1JobSpec - a model defined in Swagger

        :param active_deadline_seconds: The active_deadline_seconds of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :type active_deadline_seconds: int
        :param backoff_limit: The backoff_limit of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :type backoff_limit: int
        :param completions: The completions of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :type completions: int
        :param manual_selector: The manual_selector of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :type manual_selector: bool
        :param parallelism: The parallelism of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :type parallelism: int
        :param selector: The selector of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :type selector: IoK8sApimachineryPkgApisMetaV1LabelSelector
        :param template: The template of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :type template: IoK8sApiCoreV1PodTemplateSpec
        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :type ttl_seconds_after_finished: int
        """
        self.swagger_types = {
            'active_deadline_seconds': int,
            'backoff_limit': int,
            'completions': int,
            'manual_selector': bool,
            'parallelism': int,
            'selector': IoK8sApimachineryPkgApisMetaV1LabelSelector,
            'template': IoK8sApiCoreV1PodTemplateSpec,
            'ttl_seconds_after_finished': int
        }

        self.attribute_map = {
            'active_deadline_seconds': 'activeDeadlineSeconds',
            'backoff_limit': 'backoffLimit',
            'completions': 'completions',
            'manual_selector': 'manualSelector',
            'parallelism': 'parallelism',
            'selector': 'selector',
            'template': 'template',
            'ttl_seconds_after_finished': 'ttlSecondsAfterFinished'
        }

        self._active_deadline_seconds = active_deadline_seconds
        self._backoff_limit = backoff_limit
        self._completions = completions
        self._manual_selector = manual_selector
        self._parallelism = parallelism
        self._selector = selector
        self._template = template
        self._ttl_seconds_after_finished = ttl_seconds_after_finished

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiBatchV1JobSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.batch.v1.JobSpec of this IoK8sApiBatchV1JobSpec.  # noqa: E501
        :rtype: IoK8sApiBatchV1JobSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active_deadline_seconds(self) -> int:
        """Gets the active_deadline_seconds of this IoK8sApiBatchV1JobSpec.

        Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer  # noqa: E501

        :return: The active_deadline_seconds of this IoK8sApiBatchV1JobSpec.
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds: int):
        """Sets the active_deadline_seconds of this IoK8sApiBatchV1JobSpec.

        Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer  # noqa: E501

        :param active_deadline_seconds: The active_deadline_seconds of this IoK8sApiBatchV1JobSpec.
        :type active_deadline_seconds: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def backoff_limit(self) -> int:
        """Gets the backoff_limit of this IoK8sApiBatchV1JobSpec.

        Specifies the number of retries before marking this job failed. Defaults to 6  # noqa: E501

        :return: The backoff_limit of this IoK8sApiBatchV1JobSpec.
        :rtype: int
        """
        return self._backoff_limit

    @backoff_limit.setter
    def backoff_limit(self, backoff_limit: int):
        """Sets the backoff_limit of this IoK8sApiBatchV1JobSpec.

        Specifies the number of retries before marking this job failed. Defaults to 6  # noqa: E501

        :param backoff_limit: The backoff_limit of this IoK8sApiBatchV1JobSpec.
        :type backoff_limit: int
        """

        self._backoff_limit = backoff_limit

    @property
    def completions(self) -> int:
        """Gets the completions of this IoK8sApiBatchV1JobSpec.

        Specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The completions of this IoK8sApiBatchV1JobSpec.
        :rtype: int
        """
        return self._completions

    @completions.setter
    def completions(self, completions: int):
        """Sets the completions of this IoK8sApiBatchV1JobSpec.

        Specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param completions: The completions of this IoK8sApiBatchV1JobSpec.
        :type completions: int
        """

        self._completions = completions

    @property
    def manual_selector(self) -> bool:
        """Gets the manual_selector of this IoK8sApiBatchV1JobSpec.

        manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector  # noqa: E501

        :return: The manual_selector of this IoK8sApiBatchV1JobSpec.
        :rtype: bool
        """
        return self._manual_selector

    @manual_selector.setter
    def manual_selector(self, manual_selector: bool):
        """Sets the manual_selector of this IoK8sApiBatchV1JobSpec.

        manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector  # noqa: E501

        :param manual_selector: The manual_selector of this IoK8sApiBatchV1JobSpec.
        :type manual_selector: bool
        """

        self._manual_selector = manual_selector

    @property
    def parallelism(self) -> int:
        """Gets the parallelism of this IoK8sApiBatchV1JobSpec.

        Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The parallelism of this IoK8sApiBatchV1JobSpec.
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism: int):
        """Sets the parallelism of this IoK8sApiBatchV1JobSpec.

        Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param parallelism: The parallelism of this IoK8sApiBatchV1JobSpec.
        :type parallelism: int
        """

        self._parallelism = parallelism

    @property
    def selector(self) -> IoK8sApimachineryPkgApisMetaV1LabelSelector:
        """Gets the selector of this IoK8sApiBatchV1JobSpec.

        A label query over pods that should match the pod count. Normally, the system sets this field for you. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :return: The selector of this IoK8sApiBatchV1JobSpec.
        :rtype: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector: IoK8sApimachineryPkgApisMetaV1LabelSelector):
        """Sets the selector of this IoK8sApiBatchV1JobSpec.

        A label query over pods that should match the pod count. Normally, the system sets this field for you. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :param selector: The selector of this IoK8sApiBatchV1JobSpec.
        :type selector: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """

        self._selector = selector

    @property
    def template(self) -> IoK8sApiCoreV1PodTemplateSpec:
        """Gets the template of this IoK8sApiBatchV1JobSpec.

        Describes the pod that will be created when executing a job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The template of this IoK8sApiBatchV1JobSpec.
        :rtype: IoK8sApiCoreV1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template: IoK8sApiCoreV1PodTemplateSpec):
        """Sets the template of this IoK8sApiBatchV1JobSpec.

        Describes the pod that will be created when executing a job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param template: The template of this IoK8sApiBatchV1JobSpec.
        :type template: IoK8sApiCoreV1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def ttl_seconds_after_finished(self) -> int:
        """Gets the ttl_seconds_after_finished of this IoK8sApiBatchV1JobSpec.

        ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the TTLAfterFinished feature.  # noqa: E501

        :return: The ttl_seconds_after_finished of this IoK8sApiBatchV1JobSpec.
        :rtype: int
        """
        return self._ttl_seconds_after_finished

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished: int):
        """Sets the ttl_seconds_after_finished of this IoK8sApiBatchV1JobSpec.

        ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the TTLAfterFinished feature.  # noqa: E501

        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this IoK8sApiBatchV1JobSpec.
        :type ttl_seconds_after_finished: int
        """

        self._ttl_seconds_after_finished = ttl_seconds_after_finished