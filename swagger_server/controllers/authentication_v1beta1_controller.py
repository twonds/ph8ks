import connexion
import six

from swagger_server.models.io_k8s_api_authentication_v1beta1_token_review import IoK8sApiAuthenticationV1beta1TokenReview  # noqa: E501
from swagger_server.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList  # noqa: E501
from swagger_server import util


def create_authentication_v1beta1_token_review(body, dryRun=None, fieldManager=None, pretty=None):  # noqa: E501
    """create_authentication_v1beta1_token_review

    create a TokenReview # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :type dryRun: str
    :param fieldManager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
    :type fieldManager: str
    :param pretty: If &#39;true&#39;, then the output is pretty printed.
    :type pretty: str

    :rtype: IoK8sApiAuthenticationV1beta1TokenReview
    """
    if connexion.request.is_json:
        body = IoK8sApiAuthenticationV1beta1TokenReview.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_authentication_v1beta1_api_resources():  # noqa: E501
    """get_authentication_v1beta1_api_resources

    get available resources # noqa: E501


    :rtype: IoK8sApimachineryPkgApisMetaV1APIResourceList
    """
    return 'do some magic!'
