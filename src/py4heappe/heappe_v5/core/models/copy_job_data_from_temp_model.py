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


class CopyJobDataFromTempModel(object):
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
        'created_job_info_id': 'int',
        'temp_session_code': 'str'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'created_job_info_id': 'CreatedJobInfoId',
        'temp_session_code': 'TempSessionCode'
    }

    def __init__(self, session_code=None, created_job_info_id=None, temp_session_code=None, _configuration=None):  # noqa: E501
        """CopyJobDataFromTempModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_code = None
        self._created_job_info_id = None
        self._temp_session_code = None
        self.discriminator = None

        if session_code is not None:
            self.session_code = session_code
        if created_job_info_id is not None:
            self.created_job_info_id = created_job_info_id
        if temp_session_code is not None:
            self.temp_session_code = temp_session_code

    @property
    def session_code(self):
        """Gets the session_code of this CopyJobDataFromTempModel.  # noqa: E501

        Session code  # noqa: E501

        :return: The session_code of this CopyJobDataFromTempModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this CopyJobDataFromTempModel.

        Session code  # noqa: E501

        :param session_code: The session_code of this CopyJobDataFromTempModel.  # noqa: E501
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
    def created_job_info_id(self):
        """Gets the created_job_info_id of this CopyJobDataFromTempModel.  # noqa: E501

        Created job info id  # noqa: E501

        :return: The created_job_info_id of this CopyJobDataFromTempModel.  # noqa: E501
        :rtype: int
        """
        return self._created_job_info_id

    @created_job_info_id.setter
    def created_job_info_id(self, created_job_info_id):
        """Sets the created_job_info_id of this CopyJobDataFromTempModel.

        Created job info id  # noqa: E501

        :param created_job_info_id: The created_job_info_id of this CopyJobDataFromTempModel.  # noqa: E501
        :type: int
        """

        self._created_job_info_id = created_job_info_id

    @property
    def temp_session_code(self):
        """Gets the temp_session_code of this CopyJobDataFromTempModel.  # noqa: E501

        Temp session code  # noqa: E501

        :return: The temp_session_code of this CopyJobDataFromTempModel.  # noqa: E501
        :rtype: str
        """
        return self._temp_session_code

    @temp_session_code.setter
    def temp_session_code(self, temp_session_code):
        """Sets the temp_session_code of this CopyJobDataFromTempModel.

        Temp session code  # noqa: E501

        :param temp_session_code: The temp_session_code of this CopyJobDataFromTempModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                temp_session_code is not None and len(temp_session_code) > 50):
            raise ValueError("Invalid value for `temp_session_code`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                temp_session_code is not None and len(temp_session_code) < 0):
            raise ValueError("Invalid value for `temp_session_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._temp_session_code = temp_session_code

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
        if issubclass(CopyJobDataFromTempModel, dict):
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
        if not isinstance(other, CopyJobDataFromTempModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CopyJobDataFromTempModel):
            return True

        return self.to_dict() != other.to_dict()
