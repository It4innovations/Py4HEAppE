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


class ProblemDetails(object):
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
        'type': 'str',
        'title': 'str',
        'status': 'int',
        'detail': 'str',
        'instance': 'str'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'instance': 'instance'
    }

    def __init__(self, type=None, title=None, status=None, detail=None, instance=None, _configuration=None):  # noqa: E501
        """ProblemDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self._instance = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if instance is not None:
            self.instance = instance

    @property
    def type(self):
        """Gets the type of this ProblemDetails.  # noqa: E501


        :return: The type of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProblemDetails.


        :param type: The type of this ProblemDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this ProblemDetails.  # noqa: E501


        :return: The title of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemDetails.


        :param title: The title of this ProblemDetails.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this ProblemDetails.  # noqa: E501


        :return: The status of this ProblemDetails.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProblemDetails.


        :param status: The status of this ProblemDetails.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this ProblemDetails.  # noqa: E501


        :return: The detail of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProblemDetails.


        :param detail: The detail of this ProblemDetails.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this ProblemDetails.  # noqa: E501


        :return: The instance of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ProblemDetails.


        :param instance: The instance of this ProblemDetails.  # noqa: E501
        :type: str
        """

        self._instance = instance

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
        if issubclass(ProblemDetails, dict):
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
        if not isinstance(other, ProblemDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProblemDetails):
            return True

        return self.to_dict() != other.to_dict()
