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


class EndFileTransferModel(object):
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
        'public_key': 'str'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'submitted_job_info_id': 'SubmittedJobInfoId',
        'public_key': 'PublicKey'
    }

    def __init__(self, session_code=None, submitted_job_info_id=None, public_key=None, _configuration=None):  # noqa: E501
        """EndFileTransferModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_code = None
        self._submitted_job_info_id = None
        self._public_key = None
        self.discriminator = None

        if session_code is not None:
            self.session_code = session_code
        if submitted_job_info_id is not None:
            self.submitted_job_info_id = submitted_job_info_id
        if public_key is not None:
            self.public_key = public_key

    @property
    def session_code(self):
        """Gets the session_code of this EndFileTransferModel.  # noqa: E501

        Session code  # noqa: E501

        :return: The session_code of this EndFileTransferModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this EndFileTransferModel.

        Session code  # noqa: E501

        :param session_code: The session_code of this EndFileTransferModel.  # noqa: E501
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
        """Gets the submitted_job_info_id of this EndFileTransferModel.  # noqa: E501

        Subbmited job info id  # noqa: E501

        :return: The submitted_job_info_id of this EndFileTransferModel.  # noqa: E501
        :rtype: int
        """
        return self._submitted_job_info_id

    @submitted_job_info_id.setter
    def submitted_job_info_id(self, submitted_job_info_id):
        """Sets the submitted_job_info_id of this EndFileTransferModel.

        Subbmited job info id  # noqa: E501

        :param submitted_job_info_id: The submitted_job_info_id of this EndFileTransferModel.  # noqa: E501
        :type: int
        """

        self._submitted_job_info_id = submitted_job_info_id

    @property
    def public_key(self):
        """Gets the public_key of this EndFileTransferModel.  # noqa: E501

        Public key  # noqa: E501

        :return: The public_key of this EndFileTransferModel.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this EndFileTransferModel.

        Public key  # noqa: E501

        :param public_key: The public_key of this EndFileTransferModel.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

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
        if issubclass(EndFileTransferModel, dict):
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
        if not isinstance(other, EndFileTransferModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndFileTransferModel):
            return True

        return self.to_dict() != other.to_dict()
