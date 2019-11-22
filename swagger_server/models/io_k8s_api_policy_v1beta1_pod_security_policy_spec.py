# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiPolicyV1beta1PodSecurityPolicySpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, allow_privilege_escalation: bool=None, allowed_csi_drivers: List[IoK8sApiPolicyV1beta1AllowedCSIDriver]=None, allowed_capabilities: List[str]=None, allowed_flex_volumes: List[IoK8sApiPolicyV1beta1AllowedFlexVolume]=None, allowed_host_paths: List[IoK8sApiPolicyV1beta1AllowedHostPath]=None, allowed_proc_mount_types: List[str]=None, allowed_unsafe_sysctls: List[str]=None, default_add_capabilities: List[str]=None, default_allow_privilege_escalation: bool=None, forbidden_sysctls: List[str]=None, fs_group: IoK8sApiPolicyV1beta1FSGroupStrategyOptions=None, host_ipc: bool=None, host_network: bool=None, host_pid: bool=None, host_ports: List[IoK8sApiPolicyV1beta1HostPortRange]=None, privileged: bool=None, read_only_root_filesystem: bool=None, required_drop_capabilities: List[str]=None, run_as_group: IoK8sApiPolicyV1beta1RunAsGroupStrategyOptions=None, run_as_user: IoK8sApiPolicyV1beta1RunAsUserStrategyOptions=None, runtime_class: IoK8sApiPolicyV1beta1RuntimeClassStrategyOptions=None, se_linux: IoK8sApiPolicyV1beta1SELinuxStrategyOptions=None, supplemental_groups: IoK8sApiPolicyV1beta1SupplementalGroupsStrategyOptions=None, volumes: List[str]=None):  # noqa: E501
        """IoK8sApiPolicyV1beta1PodSecurityPolicySpec - a model defined in Swagger

        :param allow_privilege_escalation: The allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type allow_privilege_escalation: bool
        :param allowed_csi_drivers: The allowed_csi_drivers of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type allowed_csi_drivers: List[IoK8sApiPolicyV1beta1AllowedCSIDriver]
        :param allowed_capabilities: The allowed_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type allowed_capabilities: List[str]
        :param allowed_flex_volumes: The allowed_flex_volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type allowed_flex_volumes: List[IoK8sApiPolicyV1beta1AllowedFlexVolume]
        :param allowed_host_paths: The allowed_host_paths of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type allowed_host_paths: List[IoK8sApiPolicyV1beta1AllowedHostPath]
        :param allowed_proc_mount_types: The allowed_proc_mount_types of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type allowed_proc_mount_types: List[str]
        :param allowed_unsafe_sysctls: The allowed_unsafe_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type allowed_unsafe_sysctls: List[str]
        :param default_add_capabilities: The default_add_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type default_add_capabilities: List[str]
        :param default_allow_privilege_escalation: The default_allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type default_allow_privilege_escalation: bool
        :param forbidden_sysctls: The forbidden_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type forbidden_sysctls: List[str]
        :param fs_group: The fs_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type fs_group: IoK8sApiPolicyV1beta1FSGroupStrategyOptions
        :param host_ipc: The host_ipc of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type host_ipc: bool
        :param host_network: The host_network of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type host_network: bool
        :param host_pid: The host_pid of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type host_pid: bool
        :param host_ports: The host_ports of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type host_ports: List[IoK8sApiPolicyV1beta1HostPortRange]
        :param privileged: The privileged of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type privileged: bool
        :param read_only_root_filesystem: The read_only_root_filesystem of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type read_only_root_filesystem: bool
        :param required_drop_capabilities: The required_drop_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type required_drop_capabilities: List[str]
        :param run_as_group: The run_as_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type run_as_group: IoK8sApiPolicyV1beta1RunAsGroupStrategyOptions
        :param run_as_user: The run_as_user of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type run_as_user: IoK8sApiPolicyV1beta1RunAsUserStrategyOptions
        :param runtime_class: The runtime_class of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type runtime_class: IoK8sApiPolicyV1beta1RuntimeClassStrategyOptions
        :param se_linux: The se_linux of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type se_linux: IoK8sApiPolicyV1beta1SELinuxStrategyOptions
        :param supplemental_groups: The supplemental_groups of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type supplemental_groups: IoK8sApiPolicyV1beta1SupplementalGroupsStrategyOptions
        :param volumes: The volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :type volumes: List[str]
        """
        self.swagger_types = {
            'allow_privilege_escalation': bool,
            'allowed_csi_drivers': List[IoK8sApiPolicyV1beta1AllowedCSIDriver],
            'allowed_capabilities': List[str],
            'allowed_flex_volumes': List[IoK8sApiPolicyV1beta1AllowedFlexVolume],
            'allowed_host_paths': List[IoK8sApiPolicyV1beta1AllowedHostPath],
            'allowed_proc_mount_types': List[str],
            'allowed_unsafe_sysctls': List[str],
            'default_add_capabilities': List[str],
            'default_allow_privilege_escalation': bool,
            'forbidden_sysctls': List[str],
            'fs_group': IoK8sApiPolicyV1beta1FSGroupStrategyOptions,
            'host_ipc': bool,
            'host_network': bool,
            'host_pid': bool,
            'host_ports': List[IoK8sApiPolicyV1beta1HostPortRange],
            'privileged': bool,
            'read_only_root_filesystem': bool,
            'required_drop_capabilities': List[str],
            'run_as_group': IoK8sApiPolicyV1beta1RunAsGroupStrategyOptions,
            'run_as_user': IoK8sApiPolicyV1beta1RunAsUserStrategyOptions,
            'runtime_class': IoK8sApiPolicyV1beta1RuntimeClassStrategyOptions,
            'se_linux': IoK8sApiPolicyV1beta1SELinuxStrategyOptions,
            'supplemental_groups': IoK8sApiPolicyV1beta1SupplementalGroupsStrategyOptions,
            'volumes': List[str]
        }

        self.attribute_map = {
            'allow_privilege_escalation': 'allowPrivilegeEscalation',
            'allowed_csi_drivers': 'allowedCSIDrivers',
            'allowed_capabilities': 'allowedCapabilities',
            'allowed_flex_volumes': 'allowedFlexVolumes',
            'allowed_host_paths': 'allowedHostPaths',
            'allowed_proc_mount_types': 'allowedProcMountTypes',
            'allowed_unsafe_sysctls': 'allowedUnsafeSysctls',
            'default_add_capabilities': 'defaultAddCapabilities',
            'default_allow_privilege_escalation': 'defaultAllowPrivilegeEscalation',
            'forbidden_sysctls': 'forbiddenSysctls',
            'fs_group': 'fsGroup',
            'host_ipc': 'hostIPC',
            'host_network': 'hostNetwork',
            'host_pid': 'hostPID',
            'host_ports': 'hostPorts',
            'privileged': 'privileged',
            'read_only_root_filesystem': 'readOnlyRootFilesystem',
            'required_drop_capabilities': 'requiredDropCapabilities',
            'run_as_group': 'runAsGroup',
            'run_as_user': 'runAsUser',
            'runtime_class': 'runtimeClass',
            'se_linux': 'seLinux',
            'supplemental_groups': 'supplementalGroups',
            'volumes': 'volumes'
        }

        self._allow_privilege_escalation = allow_privilege_escalation
        self._allowed_csi_drivers = allowed_csi_drivers
        self._allowed_capabilities = allowed_capabilities
        self._allowed_flex_volumes = allowed_flex_volumes
        self._allowed_host_paths = allowed_host_paths
        self._allowed_proc_mount_types = allowed_proc_mount_types
        self._allowed_unsafe_sysctls = allowed_unsafe_sysctls
        self._default_add_capabilities = default_add_capabilities
        self._default_allow_privilege_escalation = default_allow_privilege_escalation
        self._forbidden_sysctls = forbidden_sysctls
        self._fs_group = fs_group
        self._host_ipc = host_ipc
        self._host_network = host_network
        self._host_pid = host_pid
        self._host_ports = host_ports
        self._privileged = privileged
        self._read_only_root_filesystem = read_only_root_filesystem
        self._required_drop_capabilities = required_drop_capabilities
        self._run_as_group = run_as_group
        self._run_as_user = run_as_user
        self._runtime_class = runtime_class
        self._se_linux = se_linux
        self._supplemental_groups = supplemental_groups
        self._volumes = volumes

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiPolicyV1beta1PodSecurityPolicySpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.policy.v1beta1.PodSecurityPolicySpec of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.  # noqa: E501
        :rtype: IoK8sApiPolicyV1beta1PodSecurityPolicySpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allow_privilege_escalation(self) -> bool:
        """Gets the allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.  # noqa: E501

        :return: The allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._allow_privilege_escalation

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, allow_privilege_escalation: bool):
        """Sets the allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.  # noqa: E501

        :param allow_privilege_escalation: The allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type allow_privilege_escalation: bool
        """

        self._allow_privilege_escalation = allow_privilege_escalation

    @property
    def allowed_csi_drivers(self) -> List[IoK8sApiPolicyV1beta1AllowedCSIDriver]:
        """Gets the allowed_csi_drivers of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        AllowedCSIDrivers is a whitelist of inline CSI drivers that must be explicitly set to be embedded within a pod spec. An empty value indicates that any CSI driver can be used for inline ephemeral volumes. This is an alpha field, and is only honored if the API server enables the CSIInlineVolume feature gate.  # noqa: E501

        :return: The allowed_csi_drivers of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[IoK8sApiPolicyV1beta1AllowedCSIDriver]
        """
        return self._allowed_csi_drivers

    @allowed_csi_drivers.setter
    def allowed_csi_drivers(self, allowed_csi_drivers: List[IoK8sApiPolicyV1beta1AllowedCSIDriver]):
        """Sets the allowed_csi_drivers of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        AllowedCSIDrivers is a whitelist of inline CSI drivers that must be explicitly set to be embedded within a pod spec. An empty value indicates that any CSI driver can be used for inline ephemeral volumes. This is an alpha field, and is only honored if the API server enables the CSIInlineVolume feature gate.  # noqa: E501

        :param allowed_csi_drivers: The allowed_csi_drivers of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type allowed_csi_drivers: List[IoK8sApiPolicyV1beta1AllowedCSIDriver]
        """

        self._allowed_csi_drivers = allowed_csi_drivers

    @property
    def allowed_capabilities(self) -> List[str]:
        """Gets the allowed_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.  # noqa: E501

        :return: The allowed_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[str]
        """
        return self._allowed_capabilities

    @allowed_capabilities.setter
    def allowed_capabilities(self, allowed_capabilities: List[str]):
        """Sets the allowed_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.  # noqa: E501

        :param allowed_capabilities: The allowed_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type allowed_capabilities: List[str]
        """

        self._allowed_capabilities = allowed_capabilities

    @property
    def allowed_flex_volumes(self) -> List[IoK8sApiPolicyV1beta1AllowedFlexVolume]:
        """Gets the allowed_flex_volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the \"volumes\" field.  # noqa: E501

        :return: The allowed_flex_volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[IoK8sApiPolicyV1beta1AllowedFlexVolume]
        """
        return self._allowed_flex_volumes

    @allowed_flex_volumes.setter
    def allowed_flex_volumes(self, allowed_flex_volumes: List[IoK8sApiPolicyV1beta1AllowedFlexVolume]):
        """Sets the allowed_flex_volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the \"volumes\" field.  # noqa: E501

        :param allowed_flex_volumes: The allowed_flex_volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type allowed_flex_volumes: List[IoK8sApiPolicyV1beta1AllowedFlexVolume]
        """

        self._allowed_flex_volumes = allowed_flex_volumes

    @property
    def allowed_host_paths(self) -> List[IoK8sApiPolicyV1beta1AllowedHostPath]:
        """Gets the allowed_host_paths of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths may be used.  # noqa: E501

        :return: The allowed_host_paths of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[IoK8sApiPolicyV1beta1AllowedHostPath]
        """
        return self._allowed_host_paths

    @allowed_host_paths.setter
    def allowed_host_paths(self, allowed_host_paths: List[IoK8sApiPolicyV1beta1AllowedHostPath]):
        """Sets the allowed_host_paths of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths may be used.  # noqa: E501

        :param allowed_host_paths: The allowed_host_paths of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type allowed_host_paths: List[IoK8sApiPolicyV1beta1AllowedHostPath]
        """

        self._allowed_host_paths = allowed_host_paths

    @property
    def allowed_proc_mount_types(self) -> List[str]:
        """Gets the allowed_proc_mount_types of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.  # noqa: E501

        :return: The allowed_proc_mount_types of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[str]
        """
        return self._allowed_proc_mount_types

    @allowed_proc_mount_types.setter
    def allowed_proc_mount_types(self, allowed_proc_mount_types: List[str]):
        """Sets the allowed_proc_mount_types of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.  # noqa: E501

        :param allowed_proc_mount_types: The allowed_proc_mount_types of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type allowed_proc_mount_types: List[str]
        """

        self._allowed_proc_mount_types = allowed_proc_mount_types

    @property
    def allowed_unsafe_sysctls(self) -> List[str]:
        """Gets the allowed_unsafe_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.  Examples: e.g. \"foo/*\" allows \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" allows \"foo.bar\", \"foo.baz\", etc.  # noqa: E501

        :return: The allowed_unsafe_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[str]
        """
        return self._allowed_unsafe_sysctls

    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(self, allowed_unsafe_sysctls: List[str]):
        """Sets the allowed_unsafe_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.  Examples: e.g. \"foo/*\" allows \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" allows \"foo.bar\", \"foo.baz\", etc.  # noqa: E501

        :param allowed_unsafe_sysctls: The allowed_unsafe_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type allowed_unsafe_sysctls: List[str]
        """

        self._allowed_unsafe_sysctls = allowed_unsafe_sysctls

    @property
    def default_add_capabilities(self) -> List[str]:
        """Gets the default_add_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.  # noqa: E501

        :return: The default_add_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[str]
        """
        return self._default_add_capabilities

    @default_add_capabilities.setter
    def default_add_capabilities(self, default_add_capabilities: List[str]):
        """Sets the default_add_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.  # noqa: E501

        :param default_add_capabilities: The default_add_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type default_add_capabilities: List[str]
        """

        self._default_add_capabilities = default_add_capabilities

    @property
    def default_allow_privilege_escalation(self) -> bool:
        """Gets the default_allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.  # noqa: E501

        :return: The default_allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._default_allow_privilege_escalation

    @default_allow_privilege_escalation.setter
    def default_allow_privilege_escalation(self, default_allow_privilege_escalation: bool):
        """Sets the default_allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.  # noqa: E501

        :param default_allow_privilege_escalation: The default_allow_privilege_escalation of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type default_allow_privilege_escalation: bool
        """

        self._default_allow_privilege_escalation = default_allow_privilege_escalation

    @property
    def forbidden_sysctls(self) -> List[str]:
        """Gets the forbidden_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.  Examples: e.g. \"foo/*\" forbids \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" forbids \"foo.bar\", \"foo.baz\", etc.  # noqa: E501

        :return: The forbidden_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[str]
        """
        return self._forbidden_sysctls

    @forbidden_sysctls.setter
    def forbidden_sysctls(self, forbidden_sysctls: List[str]):
        """Sets the forbidden_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.  Examples: e.g. \"foo/*\" forbids \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" forbids \"foo.bar\", \"foo.baz\", etc.  # noqa: E501

        :param forbidden_sysctls: The forbidden_sysctls of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type forbidden_sysctls: List[str]
        """

        self._forbidden_sysctls = forbidden_sysctls

    @property
    def fs_group(self) -> IoK8sApiPolicyV1beta1FSGroupStrategyOptions:
        """Gets the fs_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.  # noqa: E501

        :return: The fs_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: IoK8sApiPolicyV1beta1FSGroupStrategyOptions
        """
        return self._fs_group

    @fs_group.setter
    def fs_group(self, fs_group: IoK8sApiPolicyV1beta1FSGroupStrategyOptions):
        """Sets the fs_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.  # noqa: E501

        :param fs_group: The fs_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type fs_group: IoK8sApiPolicyV1beta1FSGroupStrategyOptions
        """
        if fs_group is None:
            raise ValueError("Invalid value for `fs_group`, must not be `None`")  # noqa: E501

        self._fs_group = fs_group

    @property
    def host_ipc(self) -> bool:
        """Gets the host_ipc of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        hostIPC determines if the policy allows the use of HostIPC in the pod spec.  # noqa: E501

        :return: The host_ipc of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc: bool):
        """Sets the host_ipc of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        hostIPC determines if the policy allows the use of HostIPC in the pod spec.  # noqa: E501

        :param host_ipc: The host_ipc of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type host_ipc: bool
        """

        self._host_ipc = host_ipc

    @property
    def host_network(self) -> bool:
        """Gets the host_network of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.  # noqa: E501

        :return: The host_network of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network: bool):
        """Sets the host_network of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.  # noqa: E501

        :param host_network: The host_network of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type host_network: bool
        """

        self._host_network = host_network

    @property
    def host_pid(self) -> bool:
        """Gets the host_pid of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        hostPID determines if the policy allows the use of HostPID in the pod spec.  # noqa: E501

        :return: The host_pid of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._host_pid

    @host_pid.setter
    def host_pid(self, host_pid: bool):
        """Sets the host_pid of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        hostPID determines if the policy allows the use of HostPID in the pod spec.  # noqa: E501

        :param host_pid: The host_pid of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type host_pid: bool
        """

        self._host_pid = host_pid

    @property
    def host_ports(self) -> List[IoK8sApiPolicyV1beta1HostPortRange]:
        """Gets the host_ports of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        hostPorts determines which host port ranges are allowed to be exposed.  # noqa: E501

        :return: The host_ports of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[IoK8sApiPolicyV1beta1HostPortRange]
        """
        return self._host_ports

    @host_ports.setter
    def host_ports(self, host_ports: List[IoK8sApiPolicyV1beta1HostPortRange]):
        """Sets the host_ports of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        hostPorts determines which host port ranges are allowed to be exposed.  # noqa: E501

        :param host_ports: The host_ports of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type host_ports: List[IoK8sApiPolicyV1beta1HostPortRange]
        """

        self._host_ports = host_ports

    @property
    def privileged(self) -> bool:
        """Gets the privileged of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        privileged determines if a pod can request to be run as privileged.  # noqa: E501

        :return: The privileged of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged: bool):
        """Sets the privileged of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        privileged determines if a pod can request to be run as privileged.  # noqa: E501

        :param privileged: The privileged of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type privileged: bool
        """

        self._privileged = privileged

    @property
    def read_only_root_filesystem(self) -> bool:
        """Gets the read_only_root_filesystem of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.  # noqa: E501

        :return: The read_only_root_filesystem of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem: bool):
        """Sets the read_only_root_filesystem of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.  # noqa: E501

        :param read_only_root_filesystem: The read_only_root_filesystem of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type read_only_root_filesystem: bool
        """

        self._read_only_root_filesystem = read_only_root_filesystem

    @property
    def required_drop_capabilities(self) -> List[str]:
        """Gets the required_drop_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.  # noqa: E501

        :return: The required_drop_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[str]
        """
        return self._required_drop_capabilities

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, required_drop_capabilities: List[str]):
        """Sets the required_drop_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.  # noqa: E501

        :param required_drop_capabilities: The required_drop_capabilities of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type required_drop_capabilities: List[str]
        """

        self._required_drop_capabilities = required_drop_capabilities

    @property
    def run_as_group(self) -> IoK8sApiPolicyV1beta1RunAsGroupStrategyOptions:
        """Gets the run_as_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        RunAsGroup is the strategy that will dictate the allowable RunAsGroup values that may be set. If this field is omitted, the pod's RunAsGroup can take any value. This field requires the RunAsGroup feature gate to be enabled.  # noqa: E501

        :return: The run_as_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: IoK8sApiPolicyV1beta1RunAsGroupStrategyOptions
        """
        return self._run_as_group

    @run_as_group.setter
    def run_as_group(self, run_as_group: IoK8sApiPolicyV1beta1RunAsGroupStrategyOptions):
        """Sets the run_as_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        RunAsGroup is the strategy that will dictate the allowable RunAsGroup values that may be set. If this field is omitted, the pod's RunAsGroup can take any value. This field requires the RunAsGroup feature gate to be enabled.  # noqa: E501

        :param run_as_group: The run_as_group of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type run_as_group: IoK8sApiPolicyV1beta1RunAsGroupStrategyOptions
        """

        self._run_as_group = run_as_group

    @property
    def run_as_user(self) -> IoK8sApiPolicyV1beta1RunAsUserStrategyOptions:
        """Gets the run_as_user of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.  # noqa: E501

        :return: The run_as_user of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: IoK8sApiPolicyV1beta1RunAsUserStrategyOptions
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user: IoK8sApiPolicyV1beta1RunAsUserStrategyOptions):
        """Sets the run_as_user of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.  # noqa: E501

        :param run_as_user: The run_as_user of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type run_as_user: IoK8sApiPolicyV1beta1RunAsUserStrategyOptions
        """
        if run_as_user is None:
            raise ValueError("Invalid value for `run_as_user`, must not be `None`")  # noqa: E501

        self._run_as_user = run_as_user

    @property
    def runtime_class(self) -> IoK8sApiPolicyV1beta1RuntimeClassStrategyOptions:
        """Gets the runtime_class of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        runtimeClass is the strategy that will dictate the allowable RuntimeClasses for a pod. If this field is omitted, the pod's runtimeClassName field is unrestricted. Enforcement of this field depends on the RuntimeClass feature gate being enabled.  # noqa: E501

        :return: The runtime_class of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: IoK8sApiPolicyV1beta1RuntimeClassStrategyOptions
        """
        return self._runtime_class

    @runtime_class.setter
    def runtime_class(self, runtime_class: IoK8sApiPolicyV1beta1RuntimeClassStrategyOptions):
        """Sets the runtime_class of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        runtimeClass is the strategy that will dictate the allowable RuntimeClasses for a pod. If this field is omitted, the pod's runtimeClassName field is unrestricted. Enforcement of this field depends on the RuntimeClass feature gate being enabled.  # noqa: E501

        :param runtime_class: The runtime_class of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type runtime_class: IoK8sApiPolicyV1beta1RuntimeClassStrategyOptions
        """

        self._runtime_class = runtime_class

    @property
    def se_linux(self) -> IoK8sApiPolicyV1beta1SELinuxStrategyOptions:
        """Gets the se_linux of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        seLinux is the strategy that will dictate the allowable labels that may be set.  # noqa: E501

        :return: The se_linux of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: IoK8sApiPolicyV1beta1SELinuxStrategyOptions
        """
        return self._se_linux

    @se_linux.setter
    def se_linux(self, se_linux: IoK8sApiPolicyV1beta1SELinuxStrategyOptions):
        """Sets the se_linux of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        seLinux is the strategy that will dictate the allowable labels that may be set.  # noqa: E501

        :param se_linux: The se_linux of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type se_linux: IoK8sApiPolicyV1beta1SELinuxStrategyOptions
        """
        if se_linux is None:
            raise ValueError("Invalid value for `se_linux`, must not be `None`")  # noqa: E501

        self._se_linux = se_linux

    @property
    def supplemental_groups(self) -> IoK8sApiPolicyV1beta1SupplementalGroupsStrategyOptions:
        """Gets the supplemental_groups of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        supplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.  # noqa: E501

        :return: The supplemental_groups of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: IoK8sApiPolicyV1beta1SupplementalGroupsStrategyOptions
        """
        return self._supplemental_groups

    @supplemental_groups.setter
    def supplemental_groups(self, supplemental_groups: IoK8sApiPolicyV1beta1SupplementalGroupsStrategyOptions):
        """Sets the supplemental_groups of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        supplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.  # noqa: E501

        :param supplemental_groups: The supplemental_groups of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type supplemental_groups: IoK8sApiPolicyV1beta1SupplementalGroupsStrategyOptions
        """
        if supplemental_groups is None:
            raise ValueError("Invalid value for `supplemental_groups`, must not be `None`")  # noqa: E501

        self._supplemental_groups = supplemental_groups

    @property
    def volumes(self) -> List[str]:
        """Gets the volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'.  # noqa: E501

        :return: The volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :rtype: List[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes: List[str]):
        """Sets the volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.

        volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'.  # noqa: E501

        :param volumes: The volumes of this IoK8sApiPolicyV1beta1PodSecurityPolicySpec.
        :type volumes: List[str]
        """

        self._volumes = volumes
