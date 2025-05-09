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


class TaskSpecificationExt(object):
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
        'name': 'str',
        'min_cores': 'int',
        'max_cores': 'int',
        'walltime_limit': 'int',
        'placement_policy': 'str',
        'priority': 'TaskPriorityExt',
        'job_arrays': 'str',
        'is_exclusive': 'bool',
        'is_rerunnable': 'bool',
        'standard_input_file': 'str',
        'standard_output_file': 'str',
        'standard_error_file': 'str',
        'progress_file': 'str',
        'log_file': 'str',
        'cluster_task_subdirectory': 'str',
        'cluster_node_type_id': 'int',
        'command_template_id': 'int',
        'cpu_hyper_threading': 'bool',
        'required_nodes': 'list[str]',
        'task_paralization_parameters': 'list[TaskParalizationParameterExt]',
        'environment_variables': 'list[EnvironmentVariableExt]',
        'depends_on': 'list[TaskSpecificationExt]',
        'template_parameter_values': 'list[CommandTemplateParameterValueExt]'
    }

    attribute_map = {
        'name': 'Name',
        'min_cores': 'MinCores',
        'max_cores': 'MaxCores',
        'walltime_limit': 'WalltimeLimit',
        'placement_policy': 'PlacementPolicy',
        'priority': 'Priority',
        'job_arrays': 'JobArrays',
        'is_exclusive': 'IsExclusive',
        'is_rerunnable': 'IsRerunnable',
        'standard_input_file': 'StandardInputFile',
        'standard_output_file': 'StandardOutputFile',
        'standard_error_file': 'StandardErrorFile',
        'progress_file': 'ProgressFile',
        'log_file': 'LogFile',
        'cluster_task_subdirectory': 'ClusterTaskSubdirectory',
        'cluster_node_type_id': 'ClusterNodeTypeId',
        'command_template_id': 'CommandTemplateId',
        'cpu_hyper_threading': 'CpuHyperThreading',
        'required_nodes': 'RequiredNodes',
        'task_paralization_parameters': 'TaskParalizationParameters',
        'environment_variables': 'EnvironmentVariables',
        'depends_on': 'DependsOn',
        'template_parameter_values': 'TemplateParameterValues'
    }

    def __init__(self, name=None, min_cores=None, max_cores=None, walltime_limit=None, placement_policy=None, priority=None, job_arrays=None, is_exclusive=None, is_rerunnable=None, standard_input_file=None, standard_output_file=None, standard_error_file=None, progress_file=None, log_file=None, cluster_task_subdirectory=None, cluster_node_type_id=None, command_template_id=None, cpu_hyper_threading=None, required_nodes=None, task_paralization_parameters=None, environment_variables=None, depends_on=None, template_parameter_values=None, _configuration=None):  # noqa: E501
        """TaskSpecificationExt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._min_cores = None
        self._max_cores = None
        self._walltime_limit = None
        self._placement_policy = None
        self._priority = None
        self._job_arrays = None
        self._is_exclusive = None
        self._is_rerunnable = None
        self._standard_input_file = None
        self._standard_output_file = None
        self._standard_error_file = None
        self._progress_file = None
        self._log_file = None
        self._cluster_task_subdirectory = None
        self._cluster_node_type_id = None
        self._command_template_id = None
        self._cpu_hyper_threading = None
        self._required_nodes = None
        self._task_paralization_parameters = None
        self._environment_variables = None
        self._depends_on = None
        self._template_parameter_values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if min_cores is not None:
            self.min_cores = min_cores
        self.max_cores = max_cores
        if walltime_limit is not None:
            self.walltime_limit = walltime_limit
        if placement_policy is not None:
            self.placement_policy = placement_policy
        if priority is not None:
            self.priority = priority
        if job_arrays is not None:
            self.job_arrays = job_arrays
        if is_exclusive is not None:
            self.is_exclusive = is_exclusive
        if is_rerunnable is not None:
            self.is_rerunnable = is_rerunnable
        if standard_input_file is not None:
            self.standard_input_file = standard_input_file
        if standard_output_file is not None:
            self.standard_output_file = standard_output_file
        if standard_error_file is not None:
            self.standard_error_file = standard_error_file
        if progress_file is not None:
            self.progress_file = progress_file
        if log_file is not None:
            self.log_file = log_file
        if cluster_task_subdirectory is not None:
            self.cluster_task_subdirectory = cluster_task_subdirectory
        if cluster_node_type_id is not None:
            self.cluster_node_type_id = cluster_node_type_id
        if command_template_id is not None:
            self.command_template_id = command_template_id
        if cpu_hyper_threading is not None:
            self.cpu_hyper_threading = cpu_hyper_threading
        if required_nodes is not None:
            self.required_nodes = required_nodes
        if task_paralization_parameters is not None:
            self.task_paralization_parameters = task_paralization_parameters
        if environment_variables is not None:
            self.environment_variables = environment_variables
        if depends_on is not None:
            self.depends_on = depends_on
        if template_parameter_values is not None:
            self.template_parameter_values = template_parameter_values

    @property
    def name(self):
        """Gets the name of this TaskSpecificationExt.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskSpecificationExt.

        Name  # noqa: E501

        :param name: The name of this TaskSpecificationExt.  # noqa: E501
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
    def min_cores(self):
        """Gets the min_cores of this TaskSpecificationExt.  # noqa: E501

        Minimum number of cores  # noqa: E501

        :return: The min_cores of this TaskSpecificationExt.  # noqa: E501
        :rtype: int
        """
        return self._min_cores

    @min_cores.setter
    def min_cores(self, min_cores):
        """Sets the min_cores of this TaskSpecificationExt.

        Minimum number of cores  # noqa: E501

        :param min_cores: The min_cores of this TaskSpecificationExt.  # noqa: E501
        :type: int
        """

        self._min_cores = min_cores

    @property
    def max_cores(self):
        """Gets the max_cores of this TaskSpecificationExt.  # noqa: E501

        Maximum number of cores  # noqa: E501

        :return: The max_cores of this TaskSpecificationExt.  # noqa: E501
        :rtype: int
        """
        return self._max_cores

    @max_cores.setter
    def max_cores(self, max_cores):
        """Sets the max_cores of this TaskSpecificationExt.

        Maximum number of cores  # noqa: E501

        :param max_cores: The max_cores of this TaskSpecificationExt.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and max_cores is None:
            raise ValueError("Invalid value for `max_cores`, must not be `None`")  # noqa: E501

        self._max_cores = max_cores

    @property
    def walltime_limit(self):
        """Gets the walltime_limit of this TaskSpecificationExt.  # noqa: E501

        Walltime limit  # noqa: E501

        :return: The walltime_limit of this TaskSpecificationExt.  # noqa: E501
        :rtype: int
        """
        return self._walltime_limit

    @walltime_limit.setter
    def walltime_limit(self, walltime_limit):
        """Sets the walltime_limit of this TaskSpecificationExt.

        Walltime limit  # noqa: E501

        :param walltime_limit: The walltime_limit of this TaskSpecificationExt.  # noqa: E501
        :type: int
        """

        self._walltime_limit = walltime_limit

    @property
    def placement_policy(self):
        """Gets the placement_policy of this TaskSpecificationExt.  # noqa: E501

        Placement policy  # noqa: E501

        :return: The placement_policy of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._placement_policy

    @placement_policy.setter
    def placement_policy(self, placement_policy):
        """Sets the placement_policy of this TaskSpecificationExt.

        Placement policy  # noqa: E501

        :param placement_policy: The placement_policy of this TaskSpecificationExt.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                placement_policy is not None and len(placement_policy) > 40):
            raise ValueError("Invalid value for `placement_policy`, length must be less than or equal to `40`")  # noqa: E501
        if (self._configuration.client_side_validation and
                placement_policy is not None and len(placement_policy) < 0):
            raise ValueError("Invalid value for `placement_policy`, length must be greater than or equal to `0`")  # noqa: E501

        self._placement_policy = placement_policy

    @property
    def priority(self):
        """Gets the priority of this TaskSpecificationExt.  # noqa: E501


        :return: The priority of this TaskSpecificationExt.  # noqa: E501
        :rtype: TaskPriorityExt
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TaskSpecificationExt.


        :param priority: The priority of this TaskSpecificationExt.  # noqa: E501
        :type: TaskPriorityExt
        """

        self._priority = priority

    @property
    def job_arrays(self):
        """Gets the job_arrays of this TaskSpecificationExt.  # noqa: E501

        Job arrays  # noqa: E501

        :return: The job_arrays of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._job_arrays

    @job_arrays.setter
    def job_arrays(self, job_arrays):
        """Sets the job_arrays of this TaskSpecificationExt.

        Job arrays  # noqa: E501

        :param job_arrays: The job_arrays of this TaskSpecificationExt.  # noqa: E501
        :type: str
        """

        self._job_arrays = job_arrays

    @property
    def is_exclusive(self):
        """Gets the is_exclusive of this TaskSpecificationExt.  # noqa: E501

        Is exclusive  # noqa: E501

        :return: The is_exclusive of this TaskSpecificationExt.  # noqa: E501
        :rtype: bool
        """
        return self._is_exclusive

    @is_exclusive.setter
    def is_exclusive(self, is_exclusive):
        """Sets the is_exclusive of this TaskSpecificationExt.

        Is exclusive  # noqa: E501

        :param is_exclusive: The is_exclusive of this TaskSpecificationExt.  # noqa: E501
        :type: bool
        """

        self._is_exclusive = is_exclusive

    @property
    def is_rerunnable(self):
        """Gets the is_rerunnable of this TaskSpecificationExt.  # noqa: E501

        Is rerunnable  # noqa: E501

        :return: The is_rerunnable of this TaskSpecificationExt.  # noqa: E501
        :rtype: bool
        """
        return self._is_rerunnable

    @is_rerunnable.setter
    def is_rerunnable(self, is_rerunnable):
        """Sets the is_rerunnable of this TaskSpecificationExt.

        Is rerunnable  # noqa: E501

        :param is_rerunnable: The is_rerunnable of this TaskSpecificationExt.  # noqa: E501
        :type: bool
        """

        self._is_rerunnable = is_rerunnable

    @property
    def standard_input_file(self):
        """Gets the standard_input_file of this TaskSpecificationExt.  # noqa: E501

        Standard input file  # noqa: E501

        :return: The standard_input_file of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._standard_input_file

    @standard_input_file.setter
    def standard_input_file(self, standard_input_file):
        """Sets the standard_input_file of this TaskSpecificationExt.

        Standard input file  # noqa: E501

        :param standard_input_file: The standard_input_file of this TaskSpecificationExt.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                standard_input_file is not None and len(standard_input_file) > 30):
            raise ValueError("Invalid value for `standard_input_file`, length must be less than or equal to `30`")  # noqa: E501
        if (self._configuration.client_side_validation and
                standard_input_file is not None and len(standard_input_file) < 0):
            raise ValueError("Invalid value for `standard_input_file`, length must be greater than or equal to `0`")  # noqa: E501

        self._standard_input_file = standard_input_file

    @property
    def standard_output_file(self):
        """Gets the standard_output_file of this TaskSpecificationExt.  # noqa: E501

        Standard output file  # noqa: E501

        :return: The standard_output_file of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._standard_output_file

    @standard_output_file.setter
    def standard_output_file(self, standard_output_file):
        """Sets the standard_output_file of this TaskSpecificationExt.

        Standard output file  # noqa: E501

        :param standard_output_file: The standard_output_file of this TaskSpecificationExt.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                standard_output_file is not None and len(standard_output_file) > 30):
            raise ValueError("Invalid value for `standard_output_file`, length must be less than or equal to `30`")  # noqa: E501
        if (self._configuration.client_side_validation and
                standard_output_file is not None and len(standard_output_file) < 0):
            raise ValueError("Invalid value for `standard_output_file`, length must be greater than or equal to `0`")  # noqa: E501

        self._standard_output_file = standard_output_file

    @property
    def standard_error_file(self):
        """Gets the standard_error_file of this TaskSpecificationExt.  # noqa: E501

        Standard error file  # noqa: E501

        :return: The standard_error_file of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._standard_error_file

    @standard_error_file.setter
    def standard_error_file(self, standard_error_file):
        """Sets the standard_error_file of this TaskSpecificationExt.

        Standard error file  # noqa: E501

        :param standard_error_file: The standard_error_file of this TaskSpecificationExt.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                standard_error_file is not None and len(standard_error_file) > 30):
            raise ValueError("Invalid value for `standard_error_file`, length must be less than or equal to `30`")  # noqa: E501
        if (self._configuration.client_side_validation and
                standard_error_file is not None and len(standard_error_file) < 0):
            raise ValueError("Invalid value for `standard_error_file`, length must be greater than or equal to `0`")  # noqa: E501

        self._standard_error_file = standard_error_file

    @property
    def progress_file(self):
        """Gets the progress_file of this TaskSpecificationExt.  # noqa: E501

        Progress file  # noqa: E501

        :return: The progress_file of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._progress_file

    @progress_file.setter
    def progress_file(self, progress_file):
        """Sets the progress_file of this TaskSpecificationExt.

        Progress file  # noqa: E501

        :param progress_file: The progress_file of this TaskSpecificationExt.  # noqa: E501
        :type: str
        """

        self._progress_file = progress_file

    @property
    def log_file(self):
        """Gets the log_file of this TaskSpecificationExt.  # noqa: E501

        Log file  # noqa: E501

        :return: The log_file of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._log_file

    @log_file.setter
    def log_file(self, log_file):
        """Sets the log_file of this TaskSpecificationExt.

        Log file  # noqa: E501

        :param log_file: The log_file of this TaskSpecificationExt.  # noqa: E501
        :type: str
        """

        self._log_file = log_file

    @property
    def cluster_task_subdirectory(self):
        """Gets the cluster_task_subdirectory of this TaskSpecificationExt.  # noqa: E501

        Cluster task subdirectory  # noqa: E501

        :return: The cluster_task_subdirectory of this TaskSpecificationExt.  # noqa: E501
        :rtype: str
        """
        return self._cluster_task_subdirectory

    @cluster_task_subdirectory.setter
    def cluster_task_subdirectory(self, cluster_task_subdirectory):
        """Sets the cluster_task_subdirectory of this TaskSpecificationExt.

        Cluster task subdirectory  # noqa: E501

        :param cluster_task_subdirectory: The cluster_task_subdirectory of this TaskSpecificationExt.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cluster_task_subdirectory is not None and len(cluster_task_subdirectory) > 50):
            raise ValueError("Invalid value for `cluster_task_subdirectory`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                cluster_task_subdirectory is not None and len(cluster_task_subdirectory) < 0):
            raise ValueError("Invalid value for `cluster_task_subdirectory`, length must be greater than or equal to `0`")  # noqa: E501

        self._cluster_task_subdirectory = cluster_task_subdirectory

    @property
    def cluster_node_type_id(self):
        """Gets the cluster_node_type_id of this TaskSpecificationExt.  # noqa: E501

        Cluster node type id  # noqa: E501

        :return: The cluster_node_type_id of this TaskSpecificationExt.  # noqa: E501
        :rtype: int
        """
        return self._cluster_node_type_id

    @cluster_node_type_id.setter
    def cluster_node_type_id(self, cluster_node_type_id):
        """Sets the cluster_node_type_id of this TaskSpecificationExt.

        Cluster node type id  # noqa: E501

        :param cluster_node_type_id: The cluster_node_type_id of this TaskSpecificationExt.  # noqa: E501
        :type: int
        """

        self._cluster_node_type_id = cluster_node_type_id

    @property
    def command_template_id(self):
        """Gets the command_template_id of this TaskSpecificationExt.  # noqa: E501

        Command template id  # noqa: E501

        :return: The command_template_id of this TaskSpecificationExt.  # noqa: E501
        :rtype: int
        """
        return self._command_template_id

    @command_template_id.setter
    def command_template_id(self, command_template_id):
        """Sets the command_template_id of this TaskSpecificationExt.

        Command template id  # noqa: E501

        :param command_template_id: The command_template_id of this TaskSpecificationExt.  # noqa: E501
        :type: int
        """

        self._command_template_id = command_template_id

    @property
    def cpu_hyper_threading(self):
        """Gets the cpu_hyper_threading of this TaskSpecificationExt.  # noqa: E501

        Cpu hyper threading  # noqa: E501

        :return: The cpu_hyper_threading of this TaskSpecificationExt.  # noqa: E501
        :rtype: bool
        """
        return self._cpu_hyper_threading

    @cpu_hyper_threading.setter
    def cpu_hyper_threading(self, cpu_hyper_threading):
        """Sets the cpu_hyper_threading of this TaskSpecificationExt.

        Cpu hyper threading  # noqa: E501

        :param cpu_hyper_threading: The cpu_hyper_threading of this TaskSpecificationExt.  # noqa: E501
        :type: bool
        """

        self._cpu_hyper_threading = cpu_hyper_threading

    @property
    def required_nodes(self):
        """Gets the required_nodes of this TaskSpecificationExt.  # noqa: E501

        Required nodes  # noqa: E501

        :return: The required_nodes of this TaskSpecificationExt.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_nodes

    @required_nodes.setter
    def required_nodes(self, required_nodes):
        """Sets the required_nodes of this TaskSpecificationExt.

        Required nodes  # noqa: E501

        :param required_nodes: The required_nodes of this TaskSpecificationExt.  # noqa: E501
        :type: list[str]
        """

        self._required_nodes = required_nodes

    @property
    def task_paralization_parameters(self):
        """Gets the task_paralization_parameters of this TaskSpecificationExt.  # noqa: E501

        Array of task paralization parameters  # noqa: E501

        :return: The task_paralization_parameters of this TaskSpecificationExt.  # noqa: E501
        :rtype: list[TaskParalizationParameterExt]
        """
        return self._task_paralization_parameters

    @task_paralization_parameters.setter
    def task_paralization_parameters(self, task_paralization_parameters):
        """Sets the task_paralization_parameters of this TaskSpecificationExt.

        Array of task paralization parameters  # noqa: E501

        :param task_paralization_parameters: The task_paralization_parameters of this TaskSpecificationExt.  # noqa: E501
        :type: list[TaskParalizationParameterExt]
        """

        self._task_paralization_parameters = task_paralization_parameters

    @property
    def environment_variables(self):
        """Gets the environment_variables of this TaskSpecificationExt.  # noqa: E501

        Array of environment variables  # noqa: E501

        :return: The environment_variables of this TaskSpecificationExt.  # noqa: E501
        :rtype: list[EnvironmentVariableExt]
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        """Sets the environment_variables of this TaskSpecificationExt.

        Array of environment variables  # noqa: E501

        :param environment_variables: The environment_variables of this TaskSpecificationExt.  # noqa: E501
        :type: list[EnvironmentVariableExt]
        """

        self._environment_variables = environment_variables

    @property
    def depends_on(self):
        """Gets the depends_on of this TaskSpecificationExt.  # noqa: E501

        Depends on  # noqa: E501

        :return: The depends_on of this TaskSpecificationExt.  # noqa: E501
        :rtype: list[TaskSpecificationExt]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """Sets the depends_on of this TaskSpecificationExt.

        Depends on  # noqa: E501

        :param depends_on: The depends_on of this TaskSpecificationExt.  # noqa: E501
        :type: list[TaskSpecificationExt]
        """

        self._depends_on = depends_on

    @property
    def template_parameter_values(self):
        """Gets the template_parameter_values of this TaskSpecificationExt.  # noqa: E501

        Array of command template parameter values  # noqa: E501

        :return: The template_parameter_values of this TaskSpecificationExt.  # noqa: E501
        :rtype: list[CommandTemplateParameterValueExt]
        """
        return self._template_parameter_values

    @template_parameter_values.setter
    def template_parameter_values(self, template_parameter_values):
        """Sets the template_parameter_values of this TaskSpecificationExt.

        Array of command template parameter values  # noqa: E501

        :param template_parameter_values: The template_parameter_values of this TaskSpecificationExt.  # noqa: E501
        :type: list[CommandTemplateParameterValueExt]
        """

        self._template_parameter_values = template_parameter_values

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
        if issubclass(TaskSpecificationExt, dict):
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
        if not isinstance(other, TaskSpecificationExt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskSpecificationExt):
            return True

        return self.to_dict() != other.to_dict()
