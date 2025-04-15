# coding: utf-8

"""
    py4heappe API

    Merged API documentation for py4heappe client  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from py4heappe.core.configuration import Configuration


class HttpGetToJobNodeModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'session_code': 'str',
        'submitted_job_info_id': 'int',
        'http_request': 'str',
        'http_headers': 'list[HTTPHeaderExt]',
        'node_ip_address': 'str',
        'node_port': 'int'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'submitted_job_info_id': 'SubmittedJobInfoId',
        'http_request': 'HttpRequest',
        'http_headers': 'HttpHeaders',
        'node_ip_address': 'NodeIPAddress',
        'node_port': 'NodePort'
    }

    def __init__(self, session_code=None, submitted_job_info_id=None, http_request=None, http_headers=None, node_ip_address=None, node_port=None, _configuration=None):  # noqa: E501
        """HttpGetToJobNodeModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_code = None
        self._submitted_job_info_id = None
        self._http_request = None
        self._http_headers = None
        self._node_ip_address = None
        self._node_port = None
        self.discriminator = None

        if session_code is not None:
            self.session_code = session_code
        if submitted_job_info_id is not None:
            self.submitted_job_info_id = submitted_job_info_id
        if http_request is not None:
            self.http_request = http_request
        if http_headers is not None:
            self.http_headers = http_headers
        if node_ip_address is not None:
            self.node_ip_address = node_ip_address
        self.node_port = node_port

    @property
    def session_code(self):
        """Gets the session_code of this HttpGetToJobNodeModel.  # noqa: E501

        Session code  # noqa: E501

        :return: The session_code of this HttpGetToJobNodeModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this HttpGetToJobNodeModel.

        Session code  # noqa: E501

        :param session_code: The session_code of this HttpGetToJobNodeModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                session_code is not None and len(session_code) > 50):
            raise ValueError("Invalid value for `session_code`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                session_code is not None and len(session_code) < 0):
            raise ValueError("Invalid value for `session_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._session_code = session_code

    @property
    def submitted_job_info_id(self):
        """Gets the submitted_job_info_id of this HttpGetToJobNodeModel.  # noqa: E501

        Subbmited job info id  # noqa: E501

        :return: The submitted_job_info_id of this HttpGetToJobNodeModel.  # noqa: E501
        :rtype: int
        """
        return self._submitted_job_info_id

    @submitted_job_info_id.setter
    def submitted_job_info_id(self, submitted_job_info_id):
        """Sets the submitted_job_info_id of this HttpGetToJobNodeModel.

        Subbmited job info id  # noqa: E501

        :param submitted_job_info_id: The submitted_job_info_id of this HttpGetToJobNodeModel.  # noqa: E501
        :type: int
        """

        self._submitted_job_info_id = submitted_job_info_id

    @property
    def http_request(self):
        """Gets the http_request of this HttpGetToJobNodeModel.  # noqa: E501

        Http request  # noqa: E501

        :return: The http_request of this HttpGetToJobNodeModel.  # noqa: E501
        :rtype: str
        """
        return self._http_request

    @http_request.setter
    def http_request(self, http_request):
        """Sets the http_request of this HttpGetToJobNodeModel.

        Http request  # noqa: E501

        :param http_request: The http_request of this HttpGetToJobNodeModel.  # noqa: E501
        :type: str
        """

        self._http_request = http_request

    @property
    def http_headers(self):
        """Gets the http_headers of this HttpGetToJobNodeModel.  # noqa: E501

        Http headers  # noqa: E501

        :return: The http_headers of this HttpGetToJobNodeModel.  # noqa: E501
        :rtype: list[HTTPHeaderExt]
        """
        return self._http_headers

    @http_headers.setter
    def http_headers(self, http_headers):
        """Sets the http_headers of this HttpGetToJobNodeModel.

        Http headers  # noqa: E501

        :param http_headers: The http_headers of this HttpGetToJobNodeModel.  # noqa: E501
        :type: list[HTTPHeaderExt]
        """

        self._http_headers = http_headers

    @property
    def node_ip_address(self):
        """Gets the node_ip_address of this HttpGetToJobNodeModel.  # noqa: E501

        Node ip address  # noqa: E501

        :return: The node_ip_address of this HttpGetToJobNodeModel.  # noqa: E501
        :rtype: str
        """
        return self._node_ip_address

    @node_ip_address.setter
    def node_ip_address(self, node_ip_address):
        """Sets the node_ip_address of this HttpGetToJobNodeModel.

        Node ip address  # noqa: E501

        :param node_ip_address: The node_ip_address of this HttpGetToJobNodeModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                node_ip_address is not None and len(node_ip_address) > 50):
            raise ValueError("Invalid value for `node_ip_address`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                node_ip_address is not None and len(node_ip_address) < 0):
            raise ValueError("Invalid value for `node_ip_address`, length must be greater than or equal to `0`")  # noqa: E501

        self._node_ip_address = node_ip_address

    @property
    def node_port(self):
        """Gets the node_port of this HttpGetToJobNodeModel.  # noqa: E501

        Node port  # noqa: E501

        :return: The node_port of this HttpGetToJobNodeModel.  # noqa: E501
        :rtype: int
        """
        return self._node_port

    @node_port.setter
    def node_port(self, node_port):
        """Sets the node_port of this HttpGetToJobNodeModel.

        Node port  # noqa: E501

        :param node_port: The node_port of this HttpGetToJobNodeModel.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and node_port is None:
            raise ValueError("Invalid value for `node_port`, must not be `None`")  # noqa: E501

        self._node_port = node_port

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(HttpGetToJobNodeModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HttpGetToJobNodeModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HttpGetToJobNodeModel):
            return True

        return self.to_dict() != other.to_dict()
