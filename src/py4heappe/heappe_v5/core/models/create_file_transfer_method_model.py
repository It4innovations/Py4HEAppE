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

from py4heappe.heappe_v5.core.configuration import Configuration


class CreateFileTransferMethodModel(object):
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
        'server_hostname': 'str',
        'protocol': 'FileTransferProtocol',
        'cluster_id': 'int',
        'port': 'int'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'server_hostname': 'ServerHostname',
        'protocol': 'Protocol',
        'cluster_id': 'ClusterId',
        'port': 'Port'
    }

    def __init__(self, session_code=None, server_hostname=None, protocol=None, cluster_id=None, port=None, _configuration=None):  # noqa: E501
        """CreateFileTransferMethodModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_code = None
        self._server_hostname = None
        self._protocol = None
        self._cluster_id = None
        self._port = None
        self.discriminator = None

        if session_code is not None:
            self.session_code = session_code
        if server_hostname is not None:
            self.server_hostname = server_hostname
        if protocol is not None:
            self.protocol = protocol
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if port is not None:
            self.port = port

    @property
    def session_code(self):
        """Gets the session_code of this CreateFileTransferMethodModel.  # noqa: E501

        Session code  # noqa: E501

        :return: The session_code of this CreateFileTransferMethodModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this CreateFileTransferMethodModel.

        Session code  # noqa: E501

        :param session_code: The session_code of this CreateFileTransferMethodModel.  # noqa: E501
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
    def server_hostname(self):
        """Gets the server_hostname of this CreateFileTransferMethodModel.  # noqa: E501

        Server host name  # noqa: E501

        :return: The server_hostname of this CreateFileTransferMethodModel.  # noqa: E501
        :rtype: str
        """
        return self._server_hostname

    @server_hostname.setter
    def server_hostname(self, server_hostname):
        """Sets the server_hostname of this CreateFileTransferMethodModel.

        Server host name  # noqa: E501

        :param server_hostname: The server_hostname of this CreateFileTransferMethodModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                server_hostname is not None and len(server_hostname) > 50):
            raise ValueError("Invalid value for `server_hostname`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                server_hostname is not None and len(server_hostname) < 0):
            raise ValueError("Invalid value for `server_hostname`, length must be greater than or equal to `0`")  # noqa: E501

        self._server_hostname = server_hostname

    @property
    def protocol(self):
        """Gets the protocol of this CreateFileTransferMethodModel.  # noqa: E501


        :return: The protocol of this CreateFileTransferMethodModel.  # noqa: E501
        :rtype: FileTransferProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateFileTransferMethodModel.


        :param protocol: The protocol of this CreateFileTransferMethodModel.  # noqa: E501
        :type: FileTransferProtocol
        """

        self._protocol = protocol

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateFileTransferMethodModel.  # noqa: E501

        Cluster id  # noqa: E501

        :return: The cluster_id of this CreateFileTransferMethodModel.  # noqa: E501
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateFileTransferMethodModel.

        Cluster id  # noqa: E501

        :param cluster_id: The cluster_id of this CreateFileTransferMethodModel.  # noqa: E501
        :type: int
        """

        self._cluster_id = cluster_id

    @property
    def port(self):
        """Gets the port of this CreateFileTransferMethodModel.  # noqa: E501

        Port  # noqa: E501

        :return: The port of this CreateFileTransferMethodModel.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateFileTransferMethodModel.

        Port  # noqa: E501

        :param port: The port of this CreateFileTransferMethodModel.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if issubclass(CreateFileTransferMethodModel, dict):
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
        if not isinstance(other, CreateFileTransferMethodModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFileTransferMethodModel):
            return True

        return self.to_dict() != other.to_dict()
