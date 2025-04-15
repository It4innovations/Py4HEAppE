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


class OpenStackApplicationCredentialsExt(object):
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
        'application_credentials_id': 'str',
        'application_credentials_secret': 'str'
    }

    attribute_map = {
        'application_credentials_id': 'ApplicationCredentialsId',
        'application_credentials_secret': 'ApplicationCredentialsSecret'
    }

    def __init__(self, application_credentials_id=None, application_credentials_secret=None, _configuration=None):  # noqa: E501
        """OpenStackApplicationCredentialsExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_credentials_id = None
        self._application_credentials_secret = None
        self.discriminator = None

        if application_credentials_id is not None:
            self.application_credentials_id = application_credentials_id
        if application_credentials_secret is not None:
            self.application_credentials_secret = application_credentials_secret

    @property
    def application_credentials_id(self):
        """Gets the application_credentials_id of this OpenStackApplicationCredentialsExt.  # noqa: E501

        Application credentials id  # noqa: E501

        :return: The application_credentials_id of this OpenStackApplicationCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._application_credentials_id

    @application_credentials_id.setter
    def application_credentials_id(self, application_credentials_id):
        """Sets the application_credentials_id of this OpenStackApplicationCredentialsExt.

        Application credentials id  # noqa: E501

        :param application_credentials_id: The application_credentials_id of this OpenStackApplicationCredentialsExt.  # noqa: E501
        :type: str
        """

        self._application_credentials_id = application_credentials_id

    @property
    def application_credentials_secret(self):
        """Gets the application_credentials_secret of this OpenStackApplicationCredentialsExt.  # noqa: E501

        Application credentials secret  # noqa: E501

        :return: The application_credentials_secret of this OpenStackApplicationCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._application_credentials_secret

    @application_credentials_secret.setter
    def application_credentials_secret(self, application_credentials_secret):
        """Sets the application_credentials_secret of this OpenStackApplicationCredentialsExt.

        Application credentials secret  # noqa: E501

        :param application_credentials_secret: The application_credentials_secret of this OpenStackApplicationCredentialsExt.  # noqa: E501
        :type: str
        """

        self._application_credentials_secret = application_credentials_secret

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
        if issubclass(OpenStackApplicationCredentialsExt, dict):
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
        if not isinstance(other, OpenStackApplicationCredentialsExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenStackApplicationCredentialsExt):
            return True

        return self.to_dict() != other.to_dict()
