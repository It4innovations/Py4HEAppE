# coding: utf-8

"""
    HEAppE Web API

    HEAppE middleware API v4.2.1  # noqa: E501

    OpenAPI spec version: v4.2.1
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LexisCredentialsExt(object):
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
        'username': 'str',
        'open_id_access_token': 'str'
    }

    attribute_map = {
        'username': 'Username',
        'open_id_access_token': 'OpenIdAccessToken'
    }

    def __init__(self, username=None, open_id_access_token=None):  # noqa: E501
        """LexisCredentialsExt - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._open_id_access_token = None
        self.discriminator = None
        if username is not None:
            self.username = username
        self.open_id_access_token = open_id_access_token

    @property
    def username(self):
        """Gets the username of this LexisCredentialsExt.  # noqa: E501


        :return: The username of this LexisCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LexisCredentialsExt.


        :param username: The username of this LexisCredentialsExt.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def open_id_access_token(self):
        """Gets the open_id_access_token of this LexisCredentialsExt.  # noqa: E501


        :return: The open_id_access_token of this LexisCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._open_id_access_token

    @open_id_access_token.setter
    def open_id_access_token(self, open_id_access_token):
        """Sets the open_id_access_token of this LexisCredentialsExt.


        :param open_id_access_token: The open_id_access_token of this LexisCredentialsExt.  # noqa: E501
        :type: str
        """
        if open_id_access_token is None:
            raise ValueError("Invalid value for `open_id_access_token`, must not be `None`")  # noqa: E501

        self._open_id_access_token = open_id_access_token

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
        if issubclass(LexisCredentialsExt, dict):
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
        if not isinstance(other, LexisCredentialsExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
