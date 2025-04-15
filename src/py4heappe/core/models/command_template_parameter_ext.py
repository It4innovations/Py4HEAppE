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


class CommandTemplateParameterExt(object):
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
        'identifier': 'str',
        'description': 'str'
    }

    attribute_map = {
        'identifier': 'Identifier',
        'description': 'Description'
    }

    def __init__(self, identifier=None, description=None, _configuration=None):  # noqa: E501
        """CommandTemplateParameterExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identifier = None
        self._description = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if description is not None:
            self.description = description

    @property
    def identifier(self):
        """Gets the identifier of this CommandTemplateParameterExt.  # noqa: E501

        Identifier  # noqa: E501

        :return: The identifier of this CommandTemplateParameterExt.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this CommandTemplateParameterExt.

        Identifier  # noqa: E501

        :param identifier: The identifier of this CommandTemplateParameterExt.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def description(self):
        """Gets the description of this CommandTemplateParameterExt.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this CommandTemplateParameterExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommandTemplateParameterExt.

        Description  # noqa: E501

        :param description: The description of this CommandTemplateParameterExt.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(CommandTemplateParameterExt, dict):
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
        if not isinstance(other, CommandTemplateParameterExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommandTemplateParameterExt):
            return True

        return self.to_dict() != other.to_dict()
