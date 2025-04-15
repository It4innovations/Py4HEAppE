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


class ExtendedProjectInfoExt(object):
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
        'accounting_string': 'str',
        'primary_investigator_contact': 'str',
        'contacts': 'list[str]',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'command_templates': 'list[CommandTemplateExt]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'accounting_string': 'AccountingString',
        'primary_investigator_contact': 'PrimaryInvestigatorContact',
        'contacts': 'Contacts',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'command_templates': 'CommandTemplates'
    }

    def __init__(self, id=None, name=None, description=None, accounting_string=None, primary_investigator_contact=None, contacts=None, start_date=None, end_date=None, command_templates=None, _configuration=None):  # noqa: E501
        """ExtendedProjectInfoExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._accounting_string = None
        self._primary_investigator_contact = None
        self._contacts = None
        self._start_date = None
        self._end_date = None
        self._command_templates = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if accounting_string is not None:
            self.accounting_string = accounting_string
        if primary_investigator_contact is not None:
            self.primary_investigator_contact = primary_investigator_contact
        if contacts is not None:
            self.contacts = contacts
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if command_templates is not None:
            self.command_templates = command_templates

    @property
    def id(self):
        """Gets the id of this ExtendedProjectInfoExt.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtendedProjectInfoExt.

        Id  # noqa: E501

        :param id: The id of this ExtendedProjectInfoExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ExtendedProjectInfoExt.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtendedProjectInfoExt.

        Name  # noqa: E501

        :param name: The name of this ExtendedProjectInfoExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ExtendedProjectInfoExt.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExtendedProjectInfoExt.

        Description  # noqa: E501

        :param description: The description of this ExtendedProjectInfoExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def accounting_string(self):
        """Gets the accounting_string of this ExtendedProjectInfoExt.  # noqa: E501

        Accounting string  # noqa: E501

        :return: The accounting_string of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: str
        """
        return self._accounting_string

    @accounting_string.setter
    def accounting_string(self, accounting_string):
        """Sets the accounting_string of this ExtendedProjectInfoExt.

        Accounting string  # noqa: E501

        :param accounting_string: The accounting_string of this ExtendedProjectInfoExt.  # noqa: E501
        :type: str
        """

        self._accounting_string = accounting_string

    @property
    def primary_investigator_contact(self):
        """Gets the primary_investigator_contact of this ExtendedProjectInfoExt.  # noqa: E501

        Primary investigator contact  # noqa: E501

        :return: The primary_investigator_contact of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: str
        """
        return self._primary_investigator_contact

    @primary_investigator_contact.setter
    def primary_investigator_contact(self, primary_investigator_contact):
        """Sets the primary_investigator_contact of this ExtendedProjectInfoExt.

        Primary investigator contact  # noqa: E501

        :param primary_investigator_contact: The primary_investigator_contact of this ExtendedProjectInfoExt.  # noqa: E501
        :type: str
        """

        self._primary_investigator_contact = primary_investigator_contact

    @property
    def contacts(self):
        """Gets the contacts of this ExtendedProjectInfoExt.  # noqa: E501

        Array of contacts  # noqa: E501

        :return: The contacts of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: list[str]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this ExtendedProjectInfoExt.

        Array of contacts  # noqa: E501

        :param contacts: The contacts of this ExtendedProjectInfoExt.  # noqa: E501
        :type: list[str]
        """

        self._contacts = contacts

    @property
    def start_date(self):
        """Gets the start_date of this ExtendedProjectInfoExt.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_date of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ExtendedProjectInfoExt.

        Start date  # noqa: E501

        :param start_date: The start_date of this ExtendedProjectInfoExt.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ExtendedProjectInfoExt.  # noqa: E501

        End date  # noqa: E501

        :return: The end_date of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ExtendedProjectInfoExt.

        End date  # noqa: E501

        :param end_date: The end_date of this ExtendedProjectInfoExt.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def command_templates(self):
        """Gets the command_templates of this ExtendedProjectInfoExt.  # noqa: E501

        Array of command templates  # noqa: E501

        :return: The command_templates of this ExtendedProjectInfoExt.  # noqa: E501
        :rtype: list[CommandTemplateExt]
        """
        return self._command_templates

    @command_templates.setter
    def command_templates(self, command_templates):
        """Sets the command_templates of this ExtendedProjectInfoExt.

        Array of command templates  # noqa: E501

        :param command_templates: The command_templates of this ExtendedProjectInfoExt.  # noqa: E501
        :type: list[CommandTemplateExt]
        """

        self._command_templates = command_templates

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
        if issubclass(ExtendedProjectInfoExt, dict):
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
        if not isinstance(other, ExtendedProjectInfoExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtendedProjectInfoExt):
            return True

        return self.to_dict() != other.to_dict()
