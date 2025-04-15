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


class CopyJobDataToTempModel(object):
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
        'submitted_job_info_id': 'int',
        'path': 'str'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'submitted_job_info_id': 'SubmittedJobInfoId',
        'path': 'Path'
    }

    def __init__(self, session_code=None, submitted_job_info_id=None, path=None, _configuration=None):  # noqa: E501
        """CopyJobDataToTempModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_code = None
        self._submitted_job_info_id = None
        self._path = None
        self.discriminator = None

        if session_code is not None:
            self.session_code = session_code
        if submitted_job_info_id is not None:
            self.submitted_job_info_id = submitted_job_info_id
        if path is not None:
            self.path = path

    @property
    def session_code(self):
        """Gets the session_code of this CopyJobDataToTempModel.  # noqa: E501

        Session code  # noqa: E501

        :return: The session_code of this CopyJobDataToTempModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this CopyJobDataToTempModel.

        Session code  # noqa: E501

        :param session_code: The session_code of this CopyJobDataToTempModel.  # noqa: E501
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
    def submitted_job_info_id(self):
        """Gets the submitted_job_info_id of this CopyJobDataToTempModel.  # noqa: E501

        Subbmited job info id  # noqa: E501

        :return: The submitted_job_info_id of this CopyJobDataToTempModel.  # noqa: E501
        :rtype: int
        """
        return self._submitted_job_info_id

    @submitted_job_info_id.setter
    def submitted_job_info_id(self, submitted_job_info_id):
        """Sets the submitted_job_info_id of this CopyJobDataToTempModel.

        Subbmited job info id  # noqa: E501

        :param submitted_job_info_id: The submitted_job_info_id of this CopyJobDataToTempModel.  # noqa: E501
        :type: int
        """

        self._submitted_job_info_id = submitted_job_info_id

    @property
    def path(self):
        """Gets the path of this CopyJobDataToTempModel.  # noqa: E501

        Path  # noqa: E501

        :return: The path of this CopyJobDataToTempModel.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CopyJobDataToTempModel.

        Path  # noqa: E501

        :param path: The path of this CopyJobDataToTempModel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                path is not None and len(path) > 50):
            raise ValueError("Invalid value for `path`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                path is not None and len(path) < 0):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `0`")  # noqa: E501

        self._path = path

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
        if issubclass(CopyJobDataToTempModel, dict):
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
        if not isinstance(other, CopyJobDataToTempModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CopyJobDataToTempModel):
            return True

        return self.to_dict() != other.to_dict()
