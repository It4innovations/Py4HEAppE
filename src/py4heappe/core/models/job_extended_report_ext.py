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


class JobExtendedReportExt(object):
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
        'state': 'JobStateExt',
        'tasks': 'list[TaskExtendedReportExt]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'state': 'State',
        'tasks': 'Tasks'
    }

    def __init__(self, id=None, name=None, state=None, tasks=None, _configuration=None):  # noqa: E501
        """JobExtendedReportExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._state = None
        self._tasks = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if tasks is not None:
            self.tasks = tasks

    @property
    def id(self):
        """Gets the id of this JobExtendedReportExt.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this JobExtendedReportExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobExtendedReportExt.

        Id  # noqa: E501

        :param id: The id of this JobExtendedReportExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this JobExtendedReportExt.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this JobExtendedReportExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobExtendedReportExt.

        Name  # noqa: E501

        :param name: The name of this JobExtendedReportExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this JobExtendedReportExt.  # noqa: E501


        :return: The state of this JobExtendedReportExt.  # noqa: E501
        :rtype: JobStateExt
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this JobExtendedReportExt.


        :param state: The state of this JobExtendedReportExt.  # noqa: E501
        :type: JobStateExt
        """

        self._state = state

    @property
    def tasks(self):
        """Gets the tasks of this JobExtendedReportExt.  # noqa: E501

        List of task extended reports  # noqa: E501

        :return: The tasks of this JobExtendedReportExt.  # noqa: E501
        :rtype: list[TaskExtendedReportExt]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this JobExtendedReportExt.

        List of task extended reports  # noqa: E501

        :param tasks: The tasks of this JobExtendedReportExt.  # noqa: E501
        :type: list[TaskExtendedReportExt]
        """

        self._tasks = tasks

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
        if issubclass(JobExtendedReportExt, dict):
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
        if not isinstance(other, JobExtendedReportExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobExtendedReportExt):
            return True

        return self.to_dict() != other.to_dict()
