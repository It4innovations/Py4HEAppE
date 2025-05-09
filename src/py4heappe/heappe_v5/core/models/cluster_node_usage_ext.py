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


class ClusterNodeUsageExt(object):
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
        'priority': 'int',
        'cores_per_node': 'int',
        'max_walltime': 'int',
        'number_of_nodes': 'int',
        'number_of_used_nodes': 'int',
        'total_jobs': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'priority': 'Priority',
        'cores_per_node': 'CoresPerNode',
        'max_walltime': 'MaxWalltime',
        'number_of_nodes': 'NumberOfNodes',
        'number_of_used_nodes': 'NumberOfUsedNodes',
        'total_jobs': 'TotalJobs'
    }

    def __init__(self, id=None, name=None, description=None, priority=None, cores_per_node=None, max_walltime=None, number_of_nodes=None, number_of_used_nodes=None, total_jobs=None, _configuration=None):  # noqa: E501
        """ClusterNodeUsageExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._priority = None
        self._cores_per_node = None
        self._max_walltime = None
        self._number_of_nodes = None
        self._number_of_used_nodes = None
        self._total_jobs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if cores_per_node is not None:
            self.cores_per_node = cores_per_node
        if max_walltime is not None:
            self.max_walltime = max_walltime
        if number_of_nodes is not None:
            self.number_of_nodes = number_of_nodes
        if number_of_used_nodes is not None:
            self.number_of_used_nodes = number_of_used_nodes
        if total_jobs is not None:
            self.total_jobs = total_jobs

    @property
    def id(self):
        """Gets the id of this ClusterNodeUsageExt.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterNodeUsageExt.

        Id  # noqa: E501

        :param id: The id of this ClusterNodeUsageExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusterNodeUsageExt.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterNodeUsageExt.

        Name  # noqa: E501

        :param name: The name of this ClusterNodeUsageExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ClusterNodeUsageExt.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterNodeUsageExt.

        Description  # noqa: E501

        :param description: The description of this ClusterNodeUsageExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def priority(self):
        """Gets the priority of this ClusterNodeUsageExt.  # noqa: E501

        Priority  # noqa: E501

        :return: The priority of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ClusterNodeUsageExt.

        Priority  # noqa: E501

        :param priority: The priority of this ClusterNodeUsageExt.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def cores_per_node(self):
        """Gets the cores_per_node of this ClusterNodeUsageExt.  # noqa: E501

        Number of cores per node  # noqa: E501

        :return: The cores_per_node of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._cores_per_node

    @cores_per_node.setter
    def cores_per_node(self, cores_per_node):
        """Sets the cores_per_node of this ClusterNodeUsageExt.

        Number of cores per node  # noqa: E501

        :param cores_per_node: The cores_per_node of this ClusterNodeUsageExt.  # noqa: E501
        :type: int
        """

        self._cores_per_node = cores_per_node

    @property
    def max_walltime(self):
        """Gets the max_walltime of this ClusterNodeUsageExt.  # noqa: E501

        Maximum walltime  # noqa: E501

        :return: The max_walltime of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._max_walltime

    @max_walltime.setter
    def max_walltime(self, max_walltime):
        """Sets the max_walltime of this ClusterNodeUsageExt.

        Maximum walltime  # noqa: E501

        :param max_walltime: The max_walltime of this ClusterNodeUsageExt.  # noqa: E501
        :type: int
        """

        self._max_walltime = max_walltime

    @property
    def number_of_nodes(self):
        """Gets the number_of_nodes of this ClusterNodeUsageExt.  # noqa: E501

        Number of nodes  # noqa: E501

        :return: The number_of_nodes of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._number_of_nodes

    @number_of_nodes.setter
    def number_of_nodes(self, number_of_nodes):
        """Sets the number_of_nodes of this ClusterNodeUsageExt.

        Number of nodes  # noqa: E501

        :param number_of_nodes: The number_of_nodes of this ClusterNodeUsageExt.  # noqa: E501
        :type: int
        """

        self._number_of_nodes = number_of_nodes

    @property
    def number_of_used_nodes(self):
        """Gets the number_of_used_nodes of this ClusterNodeUsageExt.  # noqa: E501

        Number of used nodes  # noqa: E501

        :return: The number_of_used_nodes of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._number_of_used_nodes

    @number_of_used_nodes.setter
    def number_of_used_nodes(self, number_of_used_nodes):
        """Sets the number_of_used_nodes of this ClusterNodeUsageExt.

        Number of used nodes  # noqa: E501

        :param number_of_used_nodes: The number_of_used_nodes of this ClusterNodeUsageExt.  # noqa: E501
        :type: int
        """

        self._number_of_used_nodes = number_of_used_nodes

    @property
    def total_jobs(self):
        """Gets the total_jobs of this ClusterNodeUsageExt.  # noqa: E501

        Total jobs number  # noqa: E501

        :return: The total_jobs of this ClusterNodeUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._total_jobs

    @total_jobs.setter
    def total_jobs(self, total_jobs):
        """Sets the total_jobs of this ClusterNodeUsageExt.

        Total jobs number  # noqa: E501

        :param total_jobs: The total_jobs of this ClusterNodeUsageExt.  # noqa: E501
        :type: int
        """

        self._total_jobs = total_jobs

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
        if issubclass(ClusterNodeUsageExt, dict):
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
        if not isinstance(other, ClusterNodeUsageExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterNodeUsageExt):
            return True

        return self.to_dict() != other.to_dict()
