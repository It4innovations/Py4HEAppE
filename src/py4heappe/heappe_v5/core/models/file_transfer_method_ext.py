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


class FileTransferMethodExt(object):
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
        'id': 'int',
        'server_hostname': 'str',
        'shared_basepath': 'str',
        'protocol': 'FileTransferProtocolExt',
        'port': 'int',
        'proxy_connection': 'ClusterProxyConnectionExt',
        'credentials': 'FileTransferKeyCredentialsExt'
    }

    attribute_map = {
        'id': 'Id',
        'server_hostname': 'ServerHostname',
        'shared_basepath': 'SharedBasepath',
        'protocol': 'Protocol',
        'port': 'Port',
        'proxy_connection': 'ProxyConnection',
        'credentials': 'Credentials'
    }

    def __init__(self, id=None, server_hostname=None, shared_basepath=None, protocol=None, port=None, proxy_connection=None, credentials=None, _configuration=None):  # noqa: E501
        """FileTransferMethodExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._server_hostname = None
        self._shared_basepath = None
        self._protocol = None
        self._port = None
        self._proxy_connection = None
        self._credentials = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if server_hostname is not None:
            self.server_hostname = server_hostname
        if shared_basepath is not None:
            self.shared_basepath = shared_basepath
        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if proxy_connection is not None:
            self.proxy_connection = proxy_connection
        if credentials is not None:
            self.credentials = credentials

    @property
    def id(self):
        """Gets the id of this FileTransferMethodExt.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this FileTransferMethodExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileTransferMethodExt.

        Id  # noqa: E501

        :param id: The id of this FileTransferMethodExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def server_hostname(self):
        """Gets the server_hostname of this FileTransferMethodExt.  # noqa: E501

        Server host name  # noqa: E501

        :return: The server_hostname of this FileTransferMethodExt.  # noqa: E501
        :rtype: str
        """
        return self._server_hostname

    @server_hostname.setter
    def server_hostname(self, server_hostname):
        """Sets the server_hostname of this FileTransferMethodExt.

        Server host name  # noqa: E501

        :param server_hostname: The server_hostname of this FileTransferMethodExt.  # noqa: E501
        :type: str
        """

        self._server_hostname = server_hostname

    @property
    def shared_basepath(self):
        """Gets the shared_basepath of this FileTransferMethodExt.  # noqa: E501

        Shared base path  # noqa: E501

        :return: The shared_basepath of this FileTransferMethodExt.  # noqa: E501
        :rtype: str
        """
        return self._shared_basepath

    @shared_basepath.setter
    def shared_basepath(self, shared_basepath):
        """Sets the shared_basepath of this FileTransferMethodExt.

        Shared base path  # noqa: E501

        :param shared_basepath: The shared_basepath of this FileTransferMethodExt.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                shared_basepath is not None and len(shared_basepath) > 200):
            raise ValueError("Invalid value for `shared_basepath`, length must be less than or equal to `200`")  # noqa: E501
        if (self._configuration.client_side_validation and
                shared_basepath is not None and len(shared_basepath) < 0):
            raise ValueError("Invalid value for `shared_basepath`, length must be greater than or equal to `0`")  # noqa: E501

        self._shared_basepath = shared_basepath

    @property
    def protocol(self):
        """Gets the protocol of this FileTransferMethodExt.  # noqa: E501


        :return: The protocol of this FileTransferMethodExt.  # noqa: E501
        :rtype: FileTransferProtocolExt
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FileTransferMethodExt.


        :param protocol: The protocol of this FileTransferMethodExt.  # noqa: E501
        :type: FileTransferProtocolExt
        """

        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this FileTransferMethodExt.  # noqa: E501

        Port  # noqa: E501

        :return: The port of this FileTransferMethodExt.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this FileTransferMethodExt.

        Port  # noqa: E501

        :param port: The port of this FileTransferMethodExt.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def proxy_connection(self):
        """Gets the proxy_connection of this FileTransferMethodExt.  # noqa: E501


        :return: The proxy_connection of this FileTransferMethodExt.  # noqa: E501
        :rtype: ClusterProxyConnectionExt
        """
        return self._proxy_connection

    @proxy_connection.setter
    def proxy_connection(self, proxy_connection):
        """Sets the proxy_connection of this FileTransferMethodExt.


        :param proxy_connection: The proxy_connection of this FileTransferMethodExt.  # noqa: E501
        :type: ClusterProxyConnectionExt
        """

        self._proxy_connection = proxy_connection

    @property
    def credentials(self):
        """Gets the credentials of this FileTransferMethodExt.  # noqa: E501


        :return: The credentials of this FileTransferMethodExt.  # noqa: E501
        :rtype: FileTransferKeyCredentialsExt
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this FileTransferMethodExt.


        :param credentials: The credentials of this FileTransferMethodExt.  # noqa: E501
        :type: FileTransferKeyCredentialsExt
        """

        self._credentials = credentials

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
        if issubclass(FileTransferMethodExt, dict):
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
        if not isinstance(other, FileTransferMethodExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileTransferMethodExt):
            return True

        return self.to_dict() != other.to_dict()
