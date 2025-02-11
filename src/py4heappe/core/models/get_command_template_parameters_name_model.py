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

class GetCommandTemplateParametersNameModel(object):
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
        'command_template_id': 'int',
        'project_id': 'int',
        'user_script_path': 'str'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'command_template_id': 'CommandTemplateId',
        'project_id': 'ProjectId',
        'user_script_path': 'UserScriptPath'
    }

    def __init__(self, session_code=None, command_template_id=None, project_id=None, user_script_path=None):  # noqa: E501
        """GetCommandTemplateParametersNameModel - a model defined in Swagger"""  # noqa: E501
        self._session_code = None
        self._command_template_id = None
        self._project_id = None
        self._user_script_path = None
        self.discriminator = None
        if session_code is not None:
            self.session_code = session_code
        if command_template_id is not None:
            self.command_template_id = command_template_id
        if project_id is not None:
            self.project_id = project_id
        if user_script_path is not None:
            self.user_script_path = user_script_path

    @property
    def session_code(self):
        """Gets the session_code of this GetCommandTemplateParametersNameModel.  # noqa: E501


        :return: The session_code of this GetCommandTemplateParametersNameModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this GetCommandTemplateParametersNameModel.


        :param session_code: The session_code of this GetCommandTemplateParametersNameModel.  # noqa: E501
        :type: str
        """

        self._session_code = session_code

    @property
    def command_template_id(self):
        """Gets the command_template_id of this GetCommandTemplateParametersNameModel.  # noqa: E501


        :return: The command_template_id of this GetCommandTemplateParametersNameModel.  # noqa: E501
        :rtype: int
        """
        return self._command_template_id

    @command_template_id.setter
    def command_template_id(self, command_template_id):
        """Sets the command_template_id of this GetCommandTemplateParametersNameModel.


        :param command_template_id: The command_template_id of this GetCommandTemplateParametersNameModel.  # noqa: E501
        :type: int
        """

        self._command_template_id = command_template_id

    @property
    def project_id(self):
        """Gets the project_id of this GetCommandTemplateParametersNameModel.  # noqa: E501


        :return: The project_id of this GetCommandTemplateParametersNameModel.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GetCommandTemplateParametersNameModel.


        :param project_id: The project_id of this GetCommandTemplateParametersNameModel.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def user_script_path(self):
        """Gets the user_script_path of this GetCommandTemplateParametersNameModel.  # noqa: E501


        :return: The user_script_path of this GetCommandTemplateParametersNameModel.  # noqa: E501
        :rtype: str
        """
        return self._user_script_path

    @user_script_path.setter
    def user_script_path(self, user_script_path):
        """Sets the user_script_path of this GetCommandTemplateParametersNameModel.


        :param user_script_path: The user_script_path of this GetCommandTemplateParametersNameModel.  # noqa: E501
        :type: str
        """

        self._user_script_path = user_script_path

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
        if issubclass(GetCommandTemplateParametersNameModel, dict):
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
        if not isinstance(other, GetCommandTemplateParametersNameModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
