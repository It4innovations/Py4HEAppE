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


class CommandTemplateExt(object):
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
        'name': 'str',
        'description': 'str',
        'extended_allocation_command': 'str',
        'is_generic': 'bool',
        'is_enabled': 'bool',
        'created_from_generic_template_id': 'int',
        'template_parameters': 'list[CommandTemplateParameterExt]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'extended_allocation_command': 'ExtendedAllocationCommand',
        'is_generic': 'IsGeneric',
        'is_enabled': 'IsEnabled',
        'created_from_generic_template_id': 'CreatedFromGenericTemplateId',
        'template_parameters': 'TemplateParameters'
    }

    def __init__(self, id=None, name=None, description=None, extended_allocation_command=None, is_generic=None, is_enabled=None, created_from_generic_template_id=None, template_parameters=None, _configuration=None):  # noqa: E501
        """CommandTemplateExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._extended_allocation_command = None
        self._is_generic = None
        self._is_enabled = None
        self._created_from_generic_template_id = None
        self._template_parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if extended_allocation_command is not None:
            self.extended_allocation_command = extended_allocation_command
        if is_generic is not None:
            self.is_generic = is_generic
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if created_from_generic_template_id is not None:
            self.created_from_generic_template_id = created_from_generic_template_id
        if template_parameters is not None:
            self.template_parameters = template_parameters

    @property
    def id(self):
        """Gets the id of this CommandTemplateExt.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this CommandTemplateExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommandTemplateExt.

        Id  # noqa: E501

        :param id: The id of this CommandTemplateExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CommandTemplateExt.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this CommandTemplateExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommandTemplateExt.

        Name  # noqa: E501

        :param name: The name of this CommandTemplateExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CommandTemplateExt.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this CommandTemplateExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommandTemplateExt.

        Description  # noqa: E501

        :param description: The description of this CommandTemplateExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extended_allocation_command(self):
        """Gets the extended_allocation_command of this CommandTemplateExt.  # noqa: E501

        Extended allocation command  # noqa: E501

        :return: The extended_allocation_command of this CommandTemplateExt.  # noqa: E501
        :rtype: str
        """
        return self._extended_allocation_command

    @extended_allocation_command.setter
    def extended_allocation_command(self, extended_allocation_command):
        """Sets the extended_allocation_command of this CommandTemplateExt.

        Extended allocation command  # noqa: E501

        :param extended_allocation_command: The extended_allocation_command of this CommandTemplateExt.  # noqa: E501
        :type: str
        """

        self._extended_allocation_command = extended_allocation_command

    @property
    def is_generic(self):
        """Gets the is_generic of this CommandTemplateExt.  # noqa: E501

        Is generic  # noqa: E501

        :return: The is_generic of this CommandTemplateExt.  # noqa: E501
        :rtype: bool
        """
        return self._is_generic

    @is_generic.setter
    def is_generic(self, is_generic):
        """Sets the is_generic of this CommandTemplateExt.

        Is generic  # noqa: E501

        :param is_generic: The is_generic of this CommandTemplateExt.  # noqa: E501
        :type: bool
        """

        self._is_generic = is_generic

    @property
    def is_enabled(self):
        """Gets the is_enabled of this CommandTemplateExt.  # noqa: E501

        Is enabled  # noqa: E501

        :return: The is_enabled of this CommandTemplateExt.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this CommandTemplateExt.

        Is enabled  # noqa: E501

        :param is_enabled: The is_enabled of this CommandTemplateExt.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def created_from_generic_template_id(self):
        """Gets the created_from_generic_template_id of this CommandTemplateExt.  # noqa: E501

        Created from generic template id  # noqa: E501

        :return: The created_from_generic_template_id of this CommandTemplateExt.  # noqa: E501
        :rtype: int
        """
        return self._created_from_generic_template_id

    @created_from_generic_template_id.setter
    def created_from_generic_template_id(self, created_from_generic_template_id):
        """Sets the created_from_generic_template_id of this CommandTemplateExt.

        Created from generic template id  # noqa: E501

        :param created_from_generic_template_id: The created_from_generic_template_id of this CommandTemplateExt.  # noqa: E501
        :type: int
        """

        self._created_from_generic_template_id = created_from_generic_template_id

    @property
    def template_parameters(self):
        """Gets the template_parameters of this CommandTemplateExt.  # noqa: E501

        Array of command template parameters  # noqa: E501

        :return: The template_parameters of this CommandTemplateExt.  # noqa: E501
        :rtype: list[CommandTemplateParameterExt]
        """
        return self._template_parameters

    @template_parameters.setter
    def template_parameters(self, template_parameters):
        """Sets the template_parameters of this CommandTemplateExt.

        Array of command template parameters  # noqa: E501

        :param template_parameters: The template_parameters of this CommandTemplateExt.  # noqa: E501
        :type: list[CommandTemplateParameterExt]
        """

        self._template_parameters = template_parameters

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
        if issubclass(CommandTemplateExt, dict):
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
        if not isinstance(other, CommandTemplateExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommandTemplateExt):
            return True

        return self.to_dict() != other.to_dict()
