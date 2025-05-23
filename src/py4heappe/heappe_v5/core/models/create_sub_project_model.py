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


class CreateSubProjectModel(object):
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
        'identifier': 'str',
        'description': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'project_id': 'int'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'identifier': 'Identifier',
        'description': 'Description',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'project_id': 'ProjectId'
    }

    def __init__(self, session_code=None, identifier=None, description=None, start_date=None, end_date=None, project_id=None, _configuration=None):  # noqa: E501
        """CreateSubProjectModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_code = None
        self._identifier = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self._project_id = None
        self.discriminator = None

        if session_code is not None:
            self.session_code = session_code
        if identifier is not None:
            self.identifier = identifier
        if description is not None:
            self.description = description
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if project_id is not None:
            self.project_id = project_id

    @property
    def session_code(self):
        """Gets the session_code of this CreateSubProjectModel.  # noqa: E501

        Session code  # noqa: E501

        :return: The session_code of this CreateSubProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this CreateSubProjectModel.

        Session code  # noqa: E501

        :param session_code: The session_code of this CreateSubProjectModel.  # noqa: E501
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
    def identifier(self):
        """Gets the identifier of this CreateSubProjectModel.  # noqa: E501

        Identifier  # noqa: E501

        :return: The identifier of this CreateSubProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this CreateSubProjectModel.

        Identifier  # noqa: E501

        :param identifier: The identifier of this CreateSubProjectModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                identifier is not None and len(identifier) > 50):
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                identifier is not None and len(identifier) < 0):
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `0`")  # noqa: E501

        self._identifier = identifier

    @property
    def description(self):
        """Gets the description of this CreateSubProjectModel.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this CreateSubProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSubProjectModel.

        Description  # noqa: E501

        :param description: The description of this CreateSubProjectModel.  # noqa: E501
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
    def start_date(self):
        """Gets the start_date of this CreateSubProjectModel.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_date of this CreateSubProjectModel.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreateSubProjectModel.

        Start date  # noqa: E501

        :param start_date: The start_date of this CreateSubProjectModel.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CreateSubProjectModel.  # noqa: E501

        End date  # noqa: E501

        :return: The end_date of this CreateSubProjectModel.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CreateSubProjectModel.

        End date  # noqa: E501

        :param end_date: The end_date of this CreateSubProjectModel.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def project_id(self):
        """Gets the project_id of this CreateSubProjectModel.  # noqa: E501

        Project id  # noqa: E501

        :return: The project_id of this CreateSubProjectModel.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateSubProjectModel.

        Project id  # noqa: E501

        :param project_id: The project_id of this CreateSubProjectModel.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

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
        if issubclass(CreateSubProjectModel, dict):
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
        if not isinstance(other, CreateSubProjectModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSubProjectModel):
            return True

        return self.to_dict() != other.to_dict()
