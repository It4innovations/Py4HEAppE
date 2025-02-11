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

class ClusterDetailedReportExt(object):
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
        'total_usage': 'float',
        'name': 'str',
        'description': 'str',
        'cluster_node_types': 'list[ClusterNodeTypeDetailedReportExt]'
    }

    attribute_map = {
        'id': 'Id',
        'total_usage': 'TotalUsage',
        'name': 'Name',
        'description': 'Description',
        'cluster_node_types': 'ClusterNodeTypes'
    }

    def __init__(self, id=None, total_usage=None, name=None, description=None, cluster_node_types=None):  # noqa: E501
        """ClusterDetailedReportExt - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._total_usage = None
        self._name = None
        self._description = None
        self._cluster_node_types = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if total_usage is not None:
            self.total_usage = total_usage
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cluster_node_types is not None:
            self.cluster_node_types = cluster_node_types

    @property
    def id(self):
        """Gets the id of this ClusterDetailedReportExt.  # noqa: E501


        :return: The id of this ClusterDetailedReportExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterDetailedReportExt.


        :param id: The id of this ClusterDetailedReportExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def total_usage(self):
        """Gets the total_usage of this ClusterDetailedReportExt.  # noqa: E501


        :return: The total_usage of this ClusterDetailedReportExt.  # noqa: E501
        :rtype: float
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """Sets the total_usage of this ClusterDetailedReportExt.


        :param total_usage: The total_usage of this ClusterDetailedReportExt.  # noqa: E501
        :type: float
        """

        self._total_usage = total_usage

    @property
    def name(self):
        """Gets the name of this ClusterDetailedReportExt.  # noqa: E501


        :return: The name of this ClusterDetailedReportExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterDetailedReportExt.


        :param name: The name of this ClusterDetailedReportExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ClusterDetailedReportExt.  # noqa: E501


        :return: The description of this ClusterDetailedReportExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterDetailedReportExt.


        :param description: The description of this ClusterDetailedReportExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def cluster_node_types(self):
        """Gets the cluster_node_types of this ClusterDetailedReportExt.  # noqa: E501


        :return: The cluster_node_types of this ClusterDetailedReportExt.  # noqa: E501
        :rtype: list[ClusterNodeTypeDetailedReportExt]
        """
        return self._cluster_node_types

    @cluster_node_types.setter
    def cluster_node_types(self, cluster_node_types):
        """Sets the cluster_node_types of this ClusterDetailedReportExt.


        :param cluster_node_types: The cluster_node_types of this ClusterDetailedReportExt.  # noqa: E501
        :type: list[ClusterNodeTypeDetailedReportExt]
        """

        self._cluster_node_types = cluster_node_types

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
        if issubclass(ClusterDetailedReportExt, dict):
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
        if not isinstance(other, ClusterDetailedReportExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
