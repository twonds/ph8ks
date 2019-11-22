import connexion
import six

from swagger_server.models.io_k8s_api_authorization_v1beta1_local_subject_access_review import IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview  # noqa: E501
from swagger_server.models.io_k8s_api_authorization_v1beta1_self_subject_access_review import IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview  # noqa: E501
from swagger_server.models.io_k8s_api_authorization_v1beta1_self_subject_rules_review import IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview  # noqa: E501
from swagger_server.models.io_k8s_api_authorization_v1beta1_subject_access_review import IoK8sApiAuthorizationV1beta1SubjectAccessReview  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server import util


def create_authorization_v1beta1_namespaced_local_subject_access_review(namespace, body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_authorization_v1beta1_namespaced_local_subject_access_review

    create a LocalSubjectAccessReview # noqa: E501

    :param namespace: object name and auth scope, such as for teams and projects
    :type namespace: str
    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview
    """
    if connexion.request.is_json:
        body = IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_authorization_v1beta1_self_subject_access_review(body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_authorization_v1beta1_self_subject_access_review

    create a SelfSubjectAccessReview # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview
    """
    if connexion.request.is_json:
        body = IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_authorization_v1beta1_self_subject_rules_review(body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_authorization_v1beta1_self_subject_rules_review

    create a SelfSubjectRulesReview # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview
    """
    if connexion.request.is_json:
        body = IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_authorization_v1beta1_subject_access_review(body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_authorization_v1beta1_subject_access_review

    create a SubjectAccessReview # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAuthorizationV1beta1SubjectAccessReview
    """
    if connexion.request.is_json:
        body = IoK8sApiAuthorizationV1beta1SubjectAccessReview.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_authorization_v1beta1_api_resources():  # noqa: E501
    """get_authorization_v1beta1_api_resources

    get available resources # noqa: E501


    :rtype: IoK8sApimachineryPkgApisMetaV1APIResourceList
    """
    return 'do some magic!'
