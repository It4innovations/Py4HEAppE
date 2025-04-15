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


class ModifyProjectClusterNodeTypeAggregationModel(object):
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
        'session_code': 'str',
        'project_id': 'int',
        'cluster_node_type_aggregation_id': 'int',
        'allocation_amount': 'int'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'project_id': 'ProjectId',
        'cluster_node_type_aggregation_id': 'ClusterNodeTypeAggregationId',
        'allocation_amount': 'AllocationAmount'
    }

    def __init__(self, session_code=None, project_id=None, cluster_node_type_aggregation_id=None, allocation_amount=None, _configuration=None):  # noqa: E501
        """ModifyProjectClusterNodeTypeAggregationModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_code = None
        self._project_id = None
        self._cluster_node_type_aggregation_id = None
        self._allocation_amount = None
        self.discriminator = None

        if session_code is not None:
            self.session_code = session_code
        if project_id is not None:
            self.project_id = project_id
        if cluster_node_type_aggregation_id is not None:
            self.cluster_node_type_aggregation_id = cluster_node_type_aggregation_id
        if allocation_amount is not None:
            self.allocation_amount = allocation_amount

    @property
    def session_code(self):
        """Gets the session_code of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501

        Session code  # noqa: E501

        :return: The session_code of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this ModifyProjectClusterNodeTypeAggregationModel.

        Session code  # noqa: E501

        :param session_code: The session_code of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                session_code is not None and len(session_code) > 50):
            raise ValueError("Invalid value for `session_code`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                session_code is not None and len(session_code) < 0):
            raise ValueError("Invalid value for `session_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._session_code = session_code

    @property
    def project_id(self):
        """Gets the project_id of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501

        Project id  # noqa: E501

        :return: The project_id of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ModifyProjectClusterNodeTypeAggregationModel.

        Project id  # noqa: E501

        :param project_id: The project_id of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def cluster_node_type_aggregation_id(self):
        """Gets the cluster_node_type_aggregation_id of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501

        Cluster node type aggregation id  # noqa: E501

        :return: The cluster_node_type_aggregation_id of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501
        :rtype: int
        """
        return self._cluster_node_type_aggregation_id

    @cluster_node_type_aggregation_id.setter
    def cluster_node_type_aggregation_id(self, cluster_node_type_aggregation_id):
        """Sets the cluster_node_type_aggregation_id of this ModifyProjectClusterNodeTypeAggregationModel.

        Cluster node type aggregation id  # noqa: E501

        :param cluster_node_type_aggregation_id: The cluster_node_type_aggregation_id of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501
        :type: int
        """

        self._cluster_node_type_aggregation_id = cluster_node_type_aggregation_id

    @property
    def allocation_amount(self):
        """Gets the allocation_amount of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501

        Allocation amount  # noqa: E501

        :return: The allocation_amount of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501
        :rtype: int
        """
        return self._allocation_amount

    @allocation_amount.setter
    def allocation_amount(self, allocation_amount):
        """Sets the allocation_amount of this ModifyProjectClusterNodeTypeAggregationModel.

        Allocation amount  # noqa: E501

        :param allocation_amount: The allocation_amount of this ModifyProjectClusterNodeTypeAggregationModel.  # noqa: E501
        :type: int
        """

        self._allocation_amount = allocation_amount

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
        if issubclass(ModifyProjectClusterNodeTypeAggregationModel, dict):
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
        if not isinstance(other, ModifyProjectClusterNodeTypeAggregationModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyProjectClusterNodeTypeAggregationModel):
            return True

        return self.to_dict() != other.to_dict()
