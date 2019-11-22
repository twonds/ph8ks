# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IoK8sApiCoreV1GitRepoVolumeSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, directory: str=None, repository: str=None, revision: str=None):  # noqa: E501
        """IoK8sApiCoreV1GitRepoVolumeSource - a model defined in Swagger

        :param directory: The directory of this IoK8sApiCoreV1GitRepoVolumeSource.  # noqa: E501
        :type directory: str
        :param repository: The repository of this IoK8sApiCoreV1GitRepoVolumeSource.  # noqa: E501
        :type repository: str
        :param revision: The revision of this IoK8sApiCoreV1GitRepoVolumeSource.  # noqa: E501
        :type revision: str
        """
        self.swagger_types = {
            'directory': str,
            'repository': str,
            'revision': str
        }

        self.attribute_map = {
            'directory': 'directory',
            'repository': 'repository',
            'revision': 'revision'
        }

        self._directory = directory
        self._repository = repository
        self._revision = revision

    @classmethod
    def from_dict(cls, dikt) -> 'IoK8sApiCoreV1GitRepoVolumeSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The io.k8s.api.core.v1.GitRepoVolumeSource of this IoK8sApiCoreV1GitRepoVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1GitRepoVolumeSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def directory(self) -> str:
        """Gets the directory of this IoK8sApiCoreV1GitRepoVolumeSource.

        Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.  # noqa: E501

        :return: The directory of this IoK8sApiCoreV1GitRepoVolumeSource.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory: str):
        """Sets the directory of this IoK8sApiCoreV1GitRepoVolumeSource.

        Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.  # noqa: E501

        :param directory: The directory of this IoK8sApiCoreV1GitRepoVolumeSource.
        :type directory: str
        """

        self._directory = directory

    @property
    def repository(self) -> str:
        """Gets the repository of this IoK8sApiCoreV1GitRepoVolumeSource.

        Repository URL  # noqa: E501

        :return: The repository of this IoK8sApiCoreV1GitRepoVolumeSource.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository: str):
        """Sets the repository of this IoK8sApiCoreV1GitRepoVolumeSource.

        Repository URL  # noqa: E501

        :param repository: The repository of this IoK8sApiCoreV1GitRepoVolumeSource.
        :type repository: str
        """
        if repository is None:
            raise ValueError("Invalid value for `repository`, must not be `None`")  # noqa: E501

        self._repository = repository

    @property
    def revision(self) -> str:
        """Gets the revision of this IoK8sApiCoreV1GitRepoVolumeSource.

        Commit hash for the specified revision.  # noqa: E501

        :return: The revision of this IoK8sApiCoreV1GitRepoVolumeSource.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision: str):
        """Sets the revision of this IoK8sApiCoreV1GitRepoVolumeSource.

        Commit hash for the specified revision.  # noqa: E501

        :param revision: The revision of this IoK8sApiCoreV1GitRepoVolumeSource.
        :type revision: str
        """

        self._revision = revision