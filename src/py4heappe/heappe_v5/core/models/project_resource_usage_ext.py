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


class ProjectResourceUsageExt(object):
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
        'start_date': 'datetime',
        'end_date': 'datetime',
        'node_types': 'list[ClusterNodeTypeResourceUsageExt]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'accounting_string': 'AccountingString',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'node_types': 'NodeTypes'
    }

    def __init__(self, id=None, name=None, description=None, accounting_string=None, start_date=None, end_date=None, node_types=None, _configuration=None):  # noqa: E501
        """ProjectResourceUsageExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._accounting_string = None
        self._start_date = None
        self._end_date = None
        self._node_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if accounting_string is not None:
            self.accounting_string = accounting_string
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if node_types is not None:
            self.node_types = node_types

    @property
    def id(self):
        """Gets the id of this ProjectResourceUsageExt.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this ProjectResourceUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectResourceUsageExt.

        Id  # noqa: E501

        :param id: The id of this ProjectResourceUsageExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectResourceUsageExt.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this ProjectResourceUsageExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectResourceUsageExt.

        Name  # noqa: E501

        :param name: The name of this ProjectResourceUsageExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectResourceUsageExt.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ProjectResourceUsageExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectResourceUsageExt.

        Description  # noqa: E501

        :param description: The description of this ProjectResourceUsageExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def accounting_string(self):
        """Gets the accounting_string of this ProjectResourceUsageExt.  # noqa: E501

        Accounting string  # noqa: E501

        :return: The accounting_string of this ProjectResourceUsageExt.  # noqa: E501
        :rtype: str
        """
        return self._accounting_string

    @accounting_string.setter
    def accounting_string(self, accounting_string):
        """Sets the accounting_string of this ProjectResourceUsageExt.

        Accounting string  # noqa: E501

        :param accounting_string: The accounting_string of this ProjectResourceUsageExt.  # noqa: E501
        :type: str
        """

        self._accounting_string = accounting_string

    @property
    def start_date(self):
        """Gets the start_date of this ProjectResourceUsageExt.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_date of this ProjectResourceUsageExt.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ProjectResourceUsageExt.

        Start date  # noqa: E501

        :param start_date: The start_date of this ProjectResourceUsageExt.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ProjectResourceUsageExt.  # noqa: E501

        End date  # noqa: E501

        :return: The end_date of this ProjectResourceUsageExt.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ProjectResourceUsageExt.

        End date  # noqa: E501

        :param end_date: The end_date of this ProjectResourceUsageExt.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def node_types(self):
        """Gets the node_types of this ProjectResourceUsageExt.  # noqa: E501

        Array of node types  # noqa: E501

        :return: The node_types of this ProjectResourceUsageExt.  # noqa: E501
        :rtype: list[ClusterNodeTypeResourceUsageExt]
        """
        return self._node_types

    @node_types.setter
    def node_types(self, node_types):
        """Sets the node_types of this ProjectResourceUsageExt.

        Array of node types  # noqa: E501

        :param node_types: The node_types of this ProjectResourceUsageExt.  # noqa: E501
        :type: list[ClusterNodeTypeResourceUsageExt]
        """

        self._node_types = node_types

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
        if issubclass(ProjectResourceUsageExt, dict):
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
        if not isinstance(other, ProjectResourceUsageExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectResourceUsageExt):
            return True

        return self.to_dict() != other.to_dict()
