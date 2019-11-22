# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApimachineryPkgApisMetaV1APIResource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, categories: List[str]=None, group: str=None, kind: str=None, name: str=None, namespaced: bool=None, short_names: List[str]=None, singular_name: str=None, storage_version_hash: str=None, verbs: List[str]=None, version: str=None):  # noqa: E501
        """IoK8sApimachineryPkgApisMetaV1APIResource - a model defined in Swagger

        :param categories: The categories of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type categories: List[str]
        :param group: The group of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type group: str
        :param kind: The kind of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type kind: str
        :param name: The name of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type name: str
        :param namespaced: The namespaced of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type namespaced: bool
        :param short_names: The short_names of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type short_names: List[str]
        :param singular_name: The singular_name of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type singular_name: str
        :param storage_version_hash: The storage_version_hash of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type storage_version_hash: str
        :param verbs: The verbs of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type verbs: List[str]
        :param version: The version of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'categories': List[str],
            'group': str,
            'kind': str,
            'name': str,
            'namespaced': bool,
            'short_names': List[str],
            'singular_name': str,
            'storage_version_hash': str,
            'verbs': List[str],
            'version': str
        }

        self.attribute_map = {
            'categories': 'categories',
            'group': 'group',
            'kind': 'kind',
            'name': 'name',
            'namespaced': 'namespaced',
            'short_names': 'shortNames',
            'singular_name': 'singularName',
            'storage_version_hash': 'storageVersionHash',
            'verbs': 'verbs',
            'version': 'version'
        }

        self._categories = categories
        self._group = group
        self._kind = kind
        self._name = name
        self._namespaced = namespaced
        self._short_names = short_names
        self._singular_name = singular_name
        self._storage_version_hash = storage_version_hash
        self._verbs = verbs
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApimachineryPkgApisMetaV1APIResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.apimachinery.pkg.apis.meta.v1.APIResource of this IoK8sApimachineryPkgApisMetaV1APIResource.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1APIResource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def categories(self) -> List[str]:
        """Gets the categories of this IoK8sApimachineryPkgApisMetaV1APIResource.

        categories is a list of the grouped resources this resource belongs to (e.g. 'all')  # noqa: E501

        :return: The categories of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[str]):
        """Sets the categories of this IoK8sApimachineryPkgApisMetaV1APIResource.

        categories is a list of the grouped resources this resource belongs to (e.g. 'all')  # noqa: E501

        :param categories: The categories of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type categories: List[str]
        """

        self._categories = categories

    @property
    def group(self) -> str:
        """Gets the group of this IoK8sApimachineryPkgApisMetaV1APIResource.

        group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\".  # noqa: E501

        :return: The group of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group: str):
        """Sets the group of this IoK8sApimachineryPkgApisMetaV1APIResource.

        group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\".  # noqa: E501

        :param group: The group of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type group: str
        """

        self._group = group

    @property
    def kind(self) -> str:
        """Gets the kind of this IoK8sApimachineryPkgApisMetaV1APIResource.

        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')  # noqa: E501

        :return: The kind of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this IoK8sApimachineryPkgApisMetaV1APIResource.

        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')  # noqa: E501

        :param kind: The kind of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type kind: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self) -> str:
        """Gets the name of this IoK8sApimachineryPkgApisMetaV1APIResource.

        name is the plural name of the resource.  # noqa: E501

        :return: The name of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IoK8sApimachineryPkgApisMetaV1APIResource.

        name is the plural name of the resource.  # noqa: E501

        :param name: The name of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespaced(self) -> bool:
        """Gets the namespaced of this IoK8sApimachineryPkgApisMetaV1APIResource.

        namespaced indicates if a resource is namespaced or not.  # noqa: E501

        :return: The namespaced of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: bool
        """
        return self._namespaced

    @namespaced.setter
    def namespaced(self, namespaced: bool):
        """Sets the namespaced of this IoK8sApimachineryPkgApisMetaV1APIResource.

        namespaced indicates if a resource is namespaced or not.  # noqa: E501

        :param namespaced: The namespaced of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type namespaced: bool
        """
        if namespaced is None:
            raise ValueError("Invalid value for `namespaced`, must not be `None`")  # noqa: E501

        self._namespaced = namespaced

    @property
    def short_names(self) -> List[str]:
        """Gets the short_names of this IoK8sApimachineryPkgApisMetaV1APIResource.

        shortNames is a list of suggested short names of the resource.  # noqa: E501

        :return: The short_names of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: List[str]
        """
        return self._short_names

    @short_names.setter
    def short_names(self, short_names: List[str]):
        """Sets the short_names of this IoK8sApimachineryPkgApisMetaV1APIResource.

        shortNames is a list of suggested short names of the resource.  # noqa: E501

        :param short_names: The short_names of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type short_names: List[str]
        """

        self._short_names = short_names

    @property
    def singular_name(self) -> str:
        """Gets the singular_name of this IoK8sApimachineryPkgApisMetaV1APIResource.

        singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.  # noqa: E501

        :return: The singular_name of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: str
        """
        return self._singular_name

    @singular_name.setter
    def singular_name(self, singular_name: str):
        """Sets the singular_name of this IoK8sApimachineryPkgApisMetaV1APIResource.

        singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.  # noqa: E501

        :param singular_name: The singular_name of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type singular_name: str
        """
        if singular_name is None:
            raise ValueError("Invalid value for `singular_name`, must not be `None`")  # noqa: E501

        self._singular_name = singular_name

    @property
    def storage_version_hash(self) -> str:
        """Gets the storage_version_hash of this IoK8sApimachineryPkgApisMetaV1APIResource.

        The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates.  # noqa: E501

        :return: The storage_version_hash of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: str
        """
        return self._storage_version_hash

    @storage_version_hash.setter
    def storage_version_hash(self, storage_version_hash: str):
        """Sets the storage_version_hash of this IoK8sApimachineryPkgApisMetaV1APIResource.

        The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates.  # noqa: E501

        :param storage_version_hash: The storage_version_hash of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type storage_version_hash: str
        """

        self._storage_version_hash = storage_version_hash

    @property
    def verbs(self) -> List[str]:
        """Gets the verbs of this IoK8sApimachineryPkgApisMetaV1APIResource.

        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)  # noqa: E501

        :return: The verbs of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: List[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs: List[str]):
        """Sets the verbs of this IoK8sApimachineryPkgApisMetaV1APIResource.

        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)  # noqa: E501

        :param verbs: The verbs of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type verbs: List[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")  # noqa: E501

        self._verbs = verbs

    @property
    def version(self) -> str:
        """Gets the version of this IoK8sApimachineryPkgApisMetaV1APIResource.

        version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)\".  # noqa: E501

        :return: The version of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this IoK8sApimachineryPkgApisMetaV1APIResource.

        version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)\".  # noqa: E501

        :param version: The version of this IoK8sApimachineryPkgApisMetaV1APIResource.
        :type version: str
        """

        self._version = version