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


class ModifyClusterModel(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'master_node_name': 'str',
        'scheduler_type': 'SchedulerType',
        'connection_protocol': 'ClusterConnectionProtocol',
        'time_zone': 'str',
        'port': 'int',
        'update_job_state_by_service_account': 'bool',
        'domain_name': 'str',
        'proxy_connection_id': 'int'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'master_node_name': 'MasterNodeName',
        'scheduler_type': 'SchedulerType',
        'connection_protocol': 'ConnectionProtocol',
        'time_zone': 'TimeZone',
        'port': 'Port',
        'update_job_state_by_service_account': 'UpdateJobStateByServiceAccount',
        'domain_name': 'DomainName',
        'proxy_connection_id': 'ProxyConnectionId'
    }

    def __init__(self, session_code=None, id=None, name=None, description=None, master_node_name=None, scheduler_type=None, connection_protocol=None, time_zone=None, port=None, update_job_state_by_service_account=None, domain_name=None, proxy_connection_id=None, _configuration=None):  # noqa: E501
        """ModifyClusterModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_code = None
        self._id = None
        self._name = None
        self._description = None
        self._master_node_name = None
        self._scheduler_type = None
        self._connection_protocol = None
        self._time_zone = None
        self._port = None
        self._update_job_state_by_service_account = None
        self._domain_name = None
        self._proxy_connection_id = None
        self.discriminator = None

        if session_code is not None:
            self.session_code = session_code
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if master_node_name is not None:
            self.master_node_name = master_node_name
        if scheduler_type is not None:
            self.scheduler_type = scheduler_type
        if connection_protocol is not None:
            self.connection_protocol = connection_protocol
        if time_zone is not None:
            self.time_zone = time_zone
        if port is not None:
            self.port = port
        if update_job_state_by_service_account is not None:
            self.update_job_state_by_service_account = update_job_state_by_service_account
        if domain_name is not None:
            self.domain_name = domain_name
        if proxy_connection_id is not None:
            self.proxy_connection_id = proxy_connection_id

    @property
    def session_code(self):
        """Gets the session_code of this ModifyClusterModel.  # noqa: E501

        Session code  # noqa: E501

        :return: The session_code of this ModifyClusterModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this ModifyClusterModel.

        Session code  # noqa: E501

        :param session_code: The session_code of this ModifyClusterModel.  # noqa: E501
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
    def id(self):
        """Gets the id of this ModifyClusterModel.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this ModifyClusterModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModifyClusterModel.

        Id  # noqa: E501

        :param id: The id of this ModifyClusterModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModifyClusterModel.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this ModifyClusterModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyClusterModel.

        Name  # noqa: E501

        :param name: The name of this ModifyClusterModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ModifyClusterModel.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ModifyClusterModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyClusterModel.

        Description  # noqa: E501

        :param description: The description of this ModifyClusterModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 100):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def master_node_name(self):
        """Gets the master_node_name of this ModifyClusterModel.  # noqa: E501

        Master node name  # noqa: E501

        :return: The master_node_name of this ModifyClusterModel.  # noqa: E501
        :rtype: str
        """
        return self._master_node_name

    @master_node_name.setter
    def master_node_name(self, master_node_name):
        """Sets the master_node_name of this ModifyClusterModel.

        Master node name  # noqa: E501

        :param master_node_name: The master_node_name of this ModifyClusterModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                master_node_name is not None and len(master_node_name) > 100):
            raise ValueError("Invalid value for `master_node_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                master_node_name is not None and len(master_node_name) < 0):
            raise ValueError("Invalid value for `master_node_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._master_node_name = master_node_name

    @property
    def scheduler_type(self):
        """Gets the scheduler_type of this ModifyClusterModel.  # noqa: E501


        :return: The scheduler_type of this ModifyClusterModel.  # noqa: E501
        :rtype: SchedulerType
        """
        return self._scheduler_type

    @scheduler_type.setter
    def scheduler_type(self, scheduler_type):
        """Sets the scheduler_type of this ModifyClusterModel.


        :param scheduler_type: The scheduler_type of this ModifyClusterModel.  # noqa: E501
        :type: SchedulerType
        """

        self._scheduler_type = scheduler_type

    @property
    def connection_protocol(self):
        """Gets the connection_protocol of this ModifyClusterModel.  # noqa: E501


        :return: The connection_protocol of this ModifyClusterModel.  # noqa: E501
        :rtype: ClusterConnectionProtocol
        """
        return self._connection_protocol

    @connection_protocol.setter
    def connection_protocol(self, connection_protocol):
        """Sets the connection_protocol of this ModifyClusterModel.


        :param connection_protocol: The connection_protocol of this ModifyClusterModel.  # noqa: E501
        :type: ClusterConnectionProtocol
        """

        self._connection_protocol = connection_protocol

    @property
    def time_zone(self):
        """Gets the time_zone of this ModifyClusterModel.  # noqa: E501

        Time zone  # noqa: E501

        :return: The time_zone of this ModifyClusterModel.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ModifyClusterModel.

        Time zone  # noqa: E501

        :param time_zone: The time_zone of this ModifyClusterModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                time_zone is not None and len(time_zone) > 10):
            raise ValueError("Invalid value for `time_zone`, length must be less than or equal to `10`")  # noqa: E501
        if (self._configuration.client_side_validation and
                time_zone is not None and len(time_zone) < 0):
            raise ValueError("Invalid value for `time_zone`, length must be greater than or equal to `0`")  # noqa: E501

        self._time_zone = time_zone

    @property
    def port(self):
        """Gets the port of this ModifyClusterModel.  # noqa: E501

        Port  # noqa: E501

        :return: The port of this ModifyClusterModel.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ModifyClusterModel.

        Port  # noqa: E501

        :param port: The port of this ModifyClusterModel.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def update_job_state_by_service_account(self):
        """Gets the update_job_state_by_service_account of this ModifyClusterModel.  # noqa: E501

        Update job state by service account  # noqa: E501

        :return: The update_job_state_by_service_account of this ModifyClusterModel.  # noqa: E501
        :rtype: bool
        """
        return self._update_job_state_by_service_account

    @update_job_state_by_service_account.setter
    def update_job_state_by_service_account(self, update_job_state_by_service_account):
        """Sets the update_job_state_by_service_account of this ModifyClusterModel.

        Update job state by service account  # noqa: E501

        :param update_job_state_by_service_account: The update_job_state_by_service_account of this ModifyClusterModel.  # noqa: E501
        :type: bool
        """

        self._update_job_state_by_service_account = update_job_state_by_service_account

    @property
    def domain_name(self):
        """Gets the domain_name of this ModifyClusterModel.  # noqa: E501

        Domain name  # noqa: E501

        :return: The domain_name of this ModifyClusterModel.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ModifyClusterModel.

        Domain name  # noqa: E501

        :param domain_name: The domain_name of this ModifyClusterModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                domain_name is not None and len(domain_name) > 20):
            raise ValueError("Invalid value for `domain_name`, length must be less than or equal to `20`")  # noqa: E501
        if (self._configuration.client_side_validation and
                domain_name is not None and len(domain_name) < 0):
            raise ValueError("Invalid value for `domain_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._domain_name = domain_name

    @property
    def proxy_connection_id(self):
        """Gets the proxy_connection_id of this ModifyClusterModel.  # noqa: E501

        Proxy connection id  # noqa: E501

        :return: The proxy_connection_id of this ModifyClusterModel.  # noqa: E501
        :rtype: int
        """
        return self._proxy_connection_id

    @proxy_connection_id.setter
    def proxy_connection_id(self, proxy_connection_id):
        """Sets the proxy_connection_id of this ModifyClusterModel.

        Proxy connection id  # noqa: E501

        :param proxy_connection_id: The proxy_connection_id of this ModifyClusterModel.  # noqa: E501
        :type: int
        """

        self._proxy_connection_id = proxy_connection_id

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
        if issubclass(ModifyClusterModel, dict):
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
        if not isinstance(other, ModifyClusterModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyClusterModel):
            return True

        return self.to_dict() != other.to_dict()
