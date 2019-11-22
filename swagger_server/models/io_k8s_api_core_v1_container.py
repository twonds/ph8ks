# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1Container(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, args: List[str]=None, command: List[str]=None, env: List[IoK8sApiCoreV1EnvVar]=None, env_from: List[IoK8sApiCoreV1EnvFromSource]=None, image: str=None, image_pull_policy: str=None, lifecycle: IoK8sApiCoreV1Lifecycle=None, liveness_probe: IoK8sApiCoreV1Probe=None, name: str=None, ports: List[IoK8sApiCoreV1ContainerPort]=None, readiness_probe: IoK8sApiCoreV1Probe=None, resources: IoK8sApiCoreV1ResourceRequirements=None, security_context: IoK8sApiCoreV1SecurityContext=None, startup_probe: IoK8sApiCoreV1Probe=None, stdin: bool=None, stdin_once: bool=None, termination_message_path: str=None, termination_message_policy: str=None, tty: bool=None, volume_devices: List[IoK8sApiCoreV1VolumeDevice]=None, volume_mounts: List[IoK8sApiCoreV1VolumeMount]=None, working_dir: str=None):  # noqa: E501
        """IoK8sApiCoreV1Container - a model defined in Swagger

        :param args: The args of this IoK8sApiCoreV1Container.  # noqa: E501
        :type args: List[str]
        :param command: The command of this IoK8sApiCoreV1Container.  # noqa: E501
        :type command: List[str]
        :param env: The env of this IoK8sApiCoreV1Container.  # noqa: E501
        :type env: List[IoK8sApiCoreV1EnvVar]
        :param env_from: The env_from of this IoK8sApiCoreV1Container.  # noqa: E501
        :type env_from: List[IoK8sApiCoreV1EnvFromSource]
        :param image: The image of this IoK8sApiCoreV1Container.  # noqa: E501
        :type image: str
        :param image_pull_policy: The image_pull_policy of this IoK8sApiCoreV1Container.  # noqa: E501
        :type image_pull_policy: str
        :param lifecycle: The lifecycle of this IoK8sApiCoreV1Container.  # noqa: E501
        :type lifecycle: IoK8sApiCoreV1Lifecycle
        :param liveness_probe: The liveness_probe of this IoK8sApiCoreV1Container.  # noqa: E501
        :type liveness_probe: IoK8sApiCoreV1Probe
        :param name: The name of this IoK8sApiCoreV1Container.  # noqa: E501
        :type name: str
        :param ports: The ports of this IoK8sApiCoreV1Container.  # noqa: E501
        :type ports: List[IoK8sApiCoreV1ContainerPort]
        :param readiness_probe: The readiness_probe of this IoK8sApiCoreV1Container.  # noqa: E501
        :type readiness_probe: IoK8sApiCoreV1Probe
        :param resources: The resources of this IoK8sApiCoreV1Container.  # noqa: E501
        :type resources: IoK8sApiCoreV1ResourceRequirements
        :param security_context: The security_context of this IoK8sApiCoreV1Container.  # noqa: E501
        :type security_context: IoK8sApiCoreV1SecurityContext
        :param startup_probe: The startup_probe of this IoK8sApiCoreV1Container.  # noqa: E501
        :type startup_probe: IoK8sApiCoreV1Probe
        :param stdin: The stdin of this IoK8sApiCoreV1Container.  # noqa: E501
        :type stdin: bool
        :param stdin_once: The stdin_once of this IoK8sApiCoreV1Container.  # noqa: E501
        :type stdin_once: bool
        :param termination_message_path: The termination_message_path of this IoK8sApiCoreV1Container.  # noqa: E501
        :type termination_message_path: str
        :param termination_message_policy: The termination_message_policy of this IoK8sApiCoreV1Container.  # noqa: E501
        :type termination_message_policy: str
        :param tty: The tty of this IoK8sApiCoreV1Container.  # noqa: E501
        :type tty: bool
        :param volume_devices: The volume_devices of this IoK8sApiCoreV1Container.  # noqa: E501
        :type volume_devices: List[IoK8sApiCoreV1VolumeDevice]
        :param volume_mounts: The volume_mounts of this IoK8sApiCoreV1Container.  # noqa: E501
        :type volume_mounts: List[IoK8sApiCoreV1VolumeMount]
        :param working_dir: The working_dir of this IoK8sApiCoreV1Container.  # noqa: E501
        :type working_dir: str
        """
        self.swagger_types = {
            'args': List[str],
            'command': List[str],
            'env': List[IoK8sApiCoreV1EnvVar],
            'env_from': List[IoK8sApiCoreV1EnvFromSource],
            'image': str,
            'image_pull_policy': str,
            'lifecycle': IoK8sApiCoreV1Lifecycle,
            'liveness_probe': IoK8sApiCoreV1Probe,
            'name': str,
            'ports': List[IoK8sApiCoreV1ContainerPort],
            'readiness_probe': IoK8sApiCoreV1Probe,
            'resources': IoK8sApiCoreV1ResourceRequirements,
            'security_context': IoK8sApiCoreV1SecurityContext,
            'startup_probe': IoK8sApiCoreV1Probe,
            'stdin': bool,
            'stdin_once': bool,
            'termination_message_path': str,
            'termination_message_policy': str,
            'tty': bool,
            'volume_devices': List[IoK8sApiCoreV1VolumeDevice],
            'volume_mounts': List[IoK8sApiCoreV1VolumeMount],
            'working_dir': str
        }

        self.attribute_map = {
            'args': 'args',
            'command': 'command',
            'env': 'env',
            'env_from': 'envFrom',
            'image': 'image',
            'image_pull_policy': 'imagePullPolicy',
            'lifecycle': 'lifecycle',
            'liveness_probe': 'livenessProbe',
            'name': 'name',
            'ports': 'ports',
            'readiness_probe': 'readinessProbe',
            'resources': 'resources',
            'security_context': 'securityContext',
            'startup_probe': 'startupProbe',
            'stdin': 'stdin',
            'stdin_once': 'stdinOnce',
            'termination_message_path': 'terminationMessagePath',
            'termination_message_policy': 'terminationMessagePolicy',
            'tty': 'tty',
            'volume_devices': 'volumeDevices',
            'volume_mounts': 'volumeMounts',
            'working_dir': 'workingDir'
        }

        self._args = args
        self._command = command
        self._env = env
        self._env_from = env_from
        self._image = image
        self._image_pull_policy = image_pull_policy
        self._lifecycle = lifecycle
        self._liveness_probe = liveness_probe
        self._name = name
        self._ports = ports
        self._readiness_probe = readiness_probe
        self._resources = resources
        self._security_context = security_context
        self._startup_probe = startup_probe
        self._stdin = stdin
        self._stdin_once = stdin_once
        self._termination_message_path = termination_message_path
        self._termination_message_policy = termination_message_policy
        self._tty = tty
        self._volume_devices = volume_devices
        self._volume_mounts = volume_mounts
        self._working_dir = working_dir

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1Container':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.Container of this IoK8sApiCoreV1Container.  # noqa: E501
        :rtype: IoK8sApiCoreV1Container
        """
        return util.deserialize_model(dikt, cls)

    @property
    def args(self) -> List[str]:
        """Gets the args of this IoK8sApiCoreV1Container.

        Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell  # noqa: E501

        :return: The args of this IoK8sApiCoreV1Container.
        :rtype: List[str]
        """
        return self._args

    @args.setter
    def args(self, args: List[str]):
        """Sets the args of this IoK8sApiCoreV1Container.

        Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell  # noqa: E501

        :param args: The args of this IoK8sApiCoreV1Container.
        :type args: List[str]
        """

        self._args = args

    @property
    def command(self) -> List[str]:
        """Gets the command of this IoK8sApiCoreV1Container.

        Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell  # noqa: E501

        :return: The command of this IoK8sApiCoreV1Container.
        :rtype: List[str]
        """
        return self._command

    @command.setter
    def command(self, command: List[str]):
        """Sets the command of this IoK8sApiCoreV1Container.

        Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell  # noqa: E501

        :param command: The command of this IoK8sApiCoreV1Container.
        :type command: List[str]
        """

        self._command = command

    @property
    def env(self) -> List[IoK8sApiCoreV1EnvVar]:
        """Gets the env of this IoK8sApiCoreV1Container.

        List of environment variables to set in the container. Cannot be updated.  # noqa: E501

        :return: The env of this IoK8sApiCoreV1Container.
        :rtype: List[IoK8sApiCoreV1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env: List[IoK8sApiCoreV1EnvVar]):
        """Sets the env of this IoK8sApiCoreV1Container.

        List of environment variables to set in the container. Cannot be updated.  # noqa: E501

        :param env: The env of this IoK8sApiCoreV1Container.
        :type env: List[IoK8sApiCoreV1EnvVar]
        """

        self._env = env

    @property
    def env_from(self) -> List[IoK8sApiCoreV1EnvFromSource]:
        """Gets the env_from of this IoK8sApiCoreV1Container.

        List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.  # noqa: E501

        :return: The env_from of this IoK8sApiCoreV1Container.
        :rtype: List[IoK8sApiCoreV1EnvFromSource]
        """
        return self._env_from

    @env_from.setter
    def env_from(self, env_from: List[IoK8sApiCoreV1EnvFromSource]):
        """Sets the env_from of this IoK8sApiCoreV1Container.

        List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.  # noqa: E501

        :param env_from: The env_from of this IoK8sApiCoreV1Container.
        :type env_from: List[IoK8sApiCoreV1EnvFromSource]
        """

        self._env_from = env_from

    @property
    def image(self) -> str:
        """Gets the image of this IoK8sApiCoreV1Container.

        Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.  # noqa: E501

        :return: The image of this IoK8sApiCoreV1Container.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this IoK8sApiCoreV1Container.

        Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.  # noqa: E501

        :param image: The image of this IoK8sApiCoreV1Container.
        :type image: str
        """

        self._image = image

    @property
    def image_pull_policy(self) -> str:
        """Gets the image_pull_policy of this IoK8sApiCoreV1Container.

        Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images  # noqa: E501

        :return: The image_pull_policy of this IoK8sApiCoreV1Container.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy: str):
        """Sets the image_pull_policy of this IoK8sApiCoreV1Container.

        Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this IoK8sApiCoreV1Container.
        :type image_pull_policy: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def lifecycle(self) -> IoK8sApiCoreV1Lifecycle:
        """Gets the lifecycle of this IoK8sApiCoreV1Container.

        Actions that the management system should take in response to container lifecycle events. Cannot be updated.  # noqa: E501

        :return: The lifecycle of this IoK8sApiCoreV1Container.
        :rtype: IoK8sApiCoreV1Lifecycle
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle: IoK8sApiCoreV1Lifecycle):
        """Sets the lifecycle of this IoK8sApiCoreV1Container.

        Actions that the management system should take in response to container lifecycle events. Cannot be updated.  # noqa: E501

        :param lifecycle: The lifecycle of this IoK8sApiCoreV1Container.
        :type lifecycle: IoK8sApiCoreV1Lifecycle
        """

        self._lifecycle = lifecycle

    @property
    def liveness_probe(self) -> IoK8sApiCoreV1Probe:
        """Gets the liveness_probe of this IoK8sApiCoreV1Container.

        Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :return: The liveness_probe of this IoK8sApiCoreV1Container.
        :rtype: IoK8sApiCoreV1Probe
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe: IoK8sApiCoreV1Probe):
        """Sets the liveness_probe of this IoK8sApiCoreV1Container.

        Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :param liveness_probe: The liveness_probe of this IoK8sApiCoreV1Container.
        :type liveness_probe: IoK8sApiCoreV1Probe
        """

        self._liveness_probe = liveness_probe

    @property
    def name(self) -> str:
        """Gets the name of this IoK8sApiCoreV1Container.

        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.  # noqa: E501

        :return: The name of this IoK8sApiCoreV1Container.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IoK8sApiCoreV1Container.

        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.  # noqa: E501

        :param name: The name of this IoK8sApiCoreV1Container.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ports(self) -> List[IoK8sApiCoreV1ContainerPort]:
        """Gets the ports of this IoK8sApiCoreV1Container.

        List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.  # noqa: E501

        :return: The ports of this IoK8sApiCoreV1Container.
        :rtype: List[IoK8sApiCoreV1ContainerPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports: List[IoK8sApiCoreV1ContainerPort]):
        """Sets the ports of this IoK8sApiCoreV1Container.

        List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.  # noqa: E501

        :param ports: The ports of this IoK8sApiCoreV1Container.
        :type ports: List[IoK8sApiCoreV1ContainerPort]
        """

        self._ports = ports

    @property
    def readiness_probe(self) -> IoK8sApiCoreV1Probe:
        """Gets the readiness_probe of this IoK8sApiCoreV1Container.

        Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :return: The readiness_probe of this IoK8sApiCoreV1Container.
        :rtype: IoK8sApiCoreV1Probe
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe: IoK8sApiCoreV1Probe):
        """Sets the readiness_probe of this IoK8sApiCoreV1Container.

        Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :param readiness_probe: The readiness_probe of this IoK8sApiCoreV1Container.
        :type readiness_probe: IoK8sApiCoreV1Probe
        """

        self._readiness_probe = readiness_probe

    @property
    def resources(self) -> IoK8sApiCoreV1ResourceRequirements:
        """Gets the resources of this IoK8sApiCoreV1Container.

        Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/  # noqa: E501

        :return: The resources of this IoK8sApiCoreV1Container.
        :rtype: IoK8sApiCoreV1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources: IoK8sApiCoreV1ResourceRequirements):
        """Sets the resources of this IoK8sApiCoreV1Container.

        Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/  # noqa: E501

        :param resources: The resources of this IoK8sApiCoreV1Container.
        :type resources: IoK8sApiCoreV1ResourceRequirements
        """

        self._resources = resources

    @property
    def security_context(self) -> IoK8sApiCoreV1SecurityContext:
        """Gets the security_context of this IoK8sApiCoreV1Container.

        Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/  # noqa: E501

        :return: The security_context of this IoK8sApiCoreV1Container.
        :rtype: IoK8sApiCoreV1SecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context: IoK8sApiCoreV1SecurityContext):
        """Sets the security_context of this IoK8sApiCoreV1Container.

        Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/  # noqa: E501

        :param security_context: The security_context of this IoK8sApiCoreV1Container.
        :type security_context: IoK8sApiCoreV1SecurityContext
        """

        self._security_context = security_context

    @property
    def startup_probe(self) -> IoK8sApiCoreV1Probe:
        """Gets the startup_probe of this IoK8sApiCoreV1Container.

        StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is an alpha feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :return: The startup_probe of this IoK8sApiCoreV1Container.
        :rtype: IoK8sApiCoreV1Probe
        """
        return self._startup_probe

    @startup_probe.setter
    def startup_probe(self, startup_probe: IoK8sApiCoreV1Probe):
        """Sets the startup_probe of this IoK8sApiCoreV1Container.

        StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is an alpha feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes  # noqa: E501

        :param startup_probe: The startup_probe of this IoK8sApiCoreV1Container.
        :type startup_probe: IoK8sApiCoreV1Probe
        """

        self._startup_probe = startup_probe

    @property
    def stdin(self) -> bool:
        """Gets the stdin of this IoK8sApiCoreV1Container.

        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.  # noqa: E501

        :return: The stdin of this IoK8sApiCoreV1Container.
        :rtype: bool
        """
        return self._stdin

    @stdin.setter
    def stdin(self, stdin: bool):
        """Sets the stdin of this IoK8sApiCoreV1Container.

        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.  # noqa: E501

        :param stdin: The stdin of this IoK8sApiCoreV1Container.
        :type stdin: bool
        """

        self._stdin = stdin

    @property
    def stdin_once(self) -> bool:
        """Gets the stdin_once of this IoK8sApiCoreV1Container.

        Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false  # noqa: E501

        :return: The stdin_once of this IoK8sApiCoreV1Container.
        :rtype: bool
        """
        return self._stdin_once

    @stdin_once.setter
    def stdin_once(self, stdin_once: bool):
        """Sets the stdin_once of this IoK8sApiCoreV1Container.

        Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false  # noqa: E501

        :param stdin_once: The stdin_once of this IoK8sApiCoreV1Container.
        :type stdin_once: bool
        """

        self._stdin_once = stdin_once

    @property
    def termination_message_path(self) -> str:
        """Gets the termination_message_path of this IoK8sApiCoreV1Container.

        Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.  # noqa: E501

        :return: The termination_message_path of this IoK8sApiCoreV1Container.
        :rtype: str
        """
        return self._termination_message_path

    @termination_message_path.setter
    def termination_message_path(self, termination_message_path: str):
        """Sets the termination_message_path of this IoK8sApiCoreV1Container.

        Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.  # noqa: E501

        :param termination_message_path: The termination_message_path of this IoK8sApiCoreV1Container.
        :type termination_message_path: str
        """

        self._termination_message_path = termination_message_path

    @property
    def termination_message_policy(self) -> str:
        """Gets the termination_message_policy of this IoK8sApiCoreV1Container.

        Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.  # noqa: E501

        :return: The termination_message_policy of this IoK8sApiCoreV1Container.
        :rtype: str
        """
        return self._termination_message_policy

    @termination_message_policy.setter
    def termination_message_policy(self, termination_message_policy: str):
        """Sets the termination_message_policy of this IoK8sApiCoreV1Container.

        Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.  # noqa: E501

        :param termination_message_policy: The termination_message_policy of this IoK8sApiCoreV1Container.
        :type termination_message_policy: str
        """

        self._termination_message_policy = termination_message_policy

    @property
    def tty(self) -> bool:
        """Gets the tty of this IoK8sApiCoreV1Container.

        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.  # noqa: E501

        :return: The tty of this IoK8sApiCoreV1Container.
        :rtype: bool
        """
        return self._tty

    @tty.setter
    def tty(self, tty: bool):
        """Sets the tty of this IoK8sApiCoreV1Container.

        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.  # noqa: E501

        :param tty: The tty of this IoK8sApiCoreV1Container.
        :type tty: bool
        """

        self._tty = tty

    @property
    def volume_devices(self) -> List[IoK8sApiCoreV1VolumeDevice]:
        """Gets the volume_devices of this IoK8sApiCoreV1Container.

        volumeDevices is the list of block devices to be used by the container. This is a beta feature.  # noqa: E501

        :return: The volume_devices of this IoK8sApiCoreV1Container.
        :rtype: List[IoK8sApiCoreV1VolumeDevice]
        """
        return self._volume_devices

    @volume_devices.setter
    def volume_devices(self, volume_devices: List[IoK8sApiCoreV1VolumeDevice]):
        """Sets the volume_devices of this IoK8sApiCoreV1Container.

        volumeDevices is the list of block devices to be used by the container. This is a beta feature.  # noqa: E501

        :param volume_devices: The volume_devices of this IoK8sApiCoreV1Container.
        :type volume_devices: List[IoK8sApiCoreV1VolumeDevice]
        """

        self._volume_devices = volume_devices

    @property
    def volume_mounts(self) -> List[IoK8sApiCoreV1VolumeMount]:
        """Gets the volume_mounts of this IoK8sApiCoreV1Container.

        Pod volumes to mount into the container's filesystem. Cannot be updated.  # noqa: E501

        :return: The volume_mounts of this IoK8sApiCoreV1Container.
        :rtype: List[IoK8sApiCoreV1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts: List[IoK8sApiCoreV1VolumeMount]):
        """Sets the volume_mounts of this IoK8sApiCoreV1Container.

        Pod volumes to mount into the container's filesystem. Cannot be updated.  # noqa: E501

        :param volume_mounts: The volume_mounts of this IoK8sApiCoreV1Container.
        :type volume_mounts: List[IoK8sApiCoreV1VolumeMount]
        """

        self._volume_mounts = volume_mounts

    @property
    def working_dir(self) -> str:
        """Gets the working_dir of this IoK8sApiCoreV1Container.

        Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.  # noqa: E501

        :return: The working_dir of this IoK8sApiCoreV1Container.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir: str):
        """Sets the working_dir of this IoK8sApiCoreV1Container.

        Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.  # noqa: E501

        :param working_dir: The working_dir of this IoK8sApiCoreV1Container.
        :type working_dir: str
        """

        self._working_dir = working_dir
