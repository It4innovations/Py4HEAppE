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


class UserGroupListReportExt(object):
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
        'total_usage': 'float',
        'usage_type': 'UsageTypeExt',
        'project': 'ProjectListReportExt'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'total_usage': 'TotalUsage',
        'usage_type': 'UsageType',
        'project': 'Project'
    }

    def __init__(self, id=None, name=None, description=None, total_usage=None, usage_type=None, project=None, _configuration=None):  # noqa: E501
        """UserGroupListReportExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._total_usage = None
        self._usage_type = None
        self._project = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if total_usage is not None:
            self.total_usage = total_usage
        if usage_type is not None:
            self.usage_type = usage_type
        if project is not None:
            self.project = project

    @property
    def id(self):
        """Gets the id of this UserGroupListReportExt.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this UserGroupListReportExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserGroupListReportExt.

        Id  # noqa: E501

        :param id: The id of this UserGroupListReportExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserGroupListReportExt.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this UserGroupListReportExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserGroupListReportExt.

        Name  # noqa: E501

        :param name: The name of this UserGroupListReportExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UserGroupListReportExt.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this UserGroupListReportExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserGroupListReportExt.

        Description  # noqa: E501

        :param description: The description of this UserGroupListReportExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def total_usage(self):
        """Gets the total_usage of this UserGroupListReportExt.  # noqa: E501

        Total usage  # noqa: E501

        :return: The total_usage of this UserGroupListReportExt.  # noqa: E501
        :rtype: float
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """Sets the total_usage of this UserGroupListReportExt.

        Total usage  # noqa: E501

        :param total_usage: The total_usage of this UserGroupListReportExt.  # noqa: E501
        :type: float
        """

        self._total_usage = total_usage

    @property
    def usage_type(self):
        """Gets the usage_type of this UserGroupListReportExt.  # noqa: E501


        :return: The usage_type of this UserGroupListReportExt.  # noqa: E501
        :rtype: UsageTypeExt
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this UserGroupListReportExt.


        :param usage_type: The usage_type of this UserGroupListReportExt.  # noqa: E501
        :type: UsageTypeExt
        """

        self._usage_type = usage_type

    @property
    def project(self):
        """Gets the project of this UserGroupListReportExt.  # noqa: E501


        :return: The project of this UserGroupListReportExt.  # noqa: E501
        :rtype: ProjectListReportExt
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this UserGroupListReportExt.


        :param project: The project of this UserGroupListReportExt.  # noqa: E501
        :type: ProjectListReportExt
        """

        self._project = project

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
        if issubclass(UserGroupListReportExt, dict):
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
        if not isinstance(other, UserGroupListReportExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserGroupListReportExt):
            return True

        return self.to_dict() != other.to_dict()
