# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from petstore_api.configuration import Configuration


class XmlItem(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'attribute_string': 'str',
        'attribute_number': 'float',
        'attribute_integer': 'int',
        'attribute_boolean': 'bool',
        'wrapped_array': 'list[int]',
        'name_string': 'str',
        'name_number': 'float',
        'name_integer': 'int',
        'name_boolean': 'bool',
        'name_array': 'list[int]',
        'name_wrapped_array': 'list[int]',
        'prefix_string': 'str',
        'prefix_number': 'float',
        'prefix_integer': 'int',
        'prefix_boolean': 'bool',
        'prefix_array': 'list[int]',
        'prefix_wrapped_array': 'list[int]',
        'namespace_string': 'str',
        'namespace_number': 'float',
        'namespace_integer': 'int',
        'namespace_boolean': 'bool',
        'namespace_array': 'list[int]',
        'namespace_wrapped_array': 'list[int]',
        'prefix_ns_string': 'str',
        'prefix_ns_number': 'float',
        'prefix_ns_integer': 'int',
        'prefix_ns_boolean': 'bool',
        'prefix_ns_array': 'list[int]',
        'prefix_ns_wrapped_array': 'list[int]'
    }

    attribute_map = {
        'attribute_string': 'attribute_string',
        'attribute_number': 'attribute_number',
        'attribute_integer': 'attribute_integer',
        'attribute_boolean': 'attribute_boolean',
        'wrapped_array': 'wrapped_array',
        'name_string': 'name_string',
        'name_number': 'name_number',
        'name_integer': 'name_integer',
        'name_boolean': 'name_boolean',
        'name_array': 'name_array',
        'name_wrapped_array': 'name_wrapped_array',
        'prefix_string': 'prefix_string',
        'prefix_number': 'prefix_number',
        'prefix_integer': 'prefix_integer',
        'prefix_boolean': 'prefix_boolean',
        'prefix_array': 'prefix_array',
        'prefix_wrapped_array': 'prefix_wrapped_array',
        'namespace_string': 'namespace_string',
        'namespace_number': 'namespace_number',
        'namespace_integer': 'namespace_integer',
        'namespace_boolean': 'namespace_boolean',
        'namespace_array': 'namespace_array',
        'namespace_wrapped_array': 'namespace_wrapped_array',
        'prefix_ns_string': 'prefix_ns_string',
        'prefix_ns_number': 'prefix_ns_number',
        'prefix_ns_integer': 'prefix_ns_integer',
        'prefix_ns_boolean': 'prefix_ns_boolean',
        'prefix_ns_array': 'prefix_ns_array',
        'prefix_ns_wrapped_array': 'prefix_ns_wrapped_array'
    }

    def __init__(self, attribute_string=None, attribute_number=None, attribute_integer=None, attribute_boolean=None, wrapped_array=None, name_string=None, name_number=None, name_integer=None, name_boolean=None, name_array=None, name_wrapped_array=None, prefix_string=None, prefix_number=None, prefix_integer=None, prefix_boolean=None, prefix_array=None, prefix_wrapped_array=None, namespace_string=None, namespace_number=None, namespace_integer=None, namespace_boolean=None, namespace_array=None, namespace_wrapped_array=None, prefix_ns_string=None, prefix_ns_number=None, prefix_ns_integer=None, prefix_ns_boolean=None, prefix_ns_array=None, prefix_ns_wrapped_array=None, local_vars_configuration=None):  # noqa: E501
        """XmlItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attribute_string = None
        self._attribute_number = None
        self._attribute_integer = None
        self._attribute_boolean = None
        self._wrapped_array = None
        self._name_string = None
        self._name_number = None
        self._name_integer = None
        self._name_boolean = None
        self._name_array = None
        self._name_wrapped_array = None
        self._prefix_string = None
        self._prefix_number = None
        self._prefix_integer = None
        self._prefix_boolean = None
        self._prefix_array = None
        self._prefix_wrapped_array = None
        self._namespace_string = None
        self._namespace_number = None
        self._namespace_integer = None
        self._namespace_boolean = None
        self._namespace_array = None
        self._namespace_wrapped_array = None
        self._prefix_ns_string = None
        self._prefix_ns_number = None
        self._prefix_ns_integer = None
        self._prefix_ns_boolean = None
        self._prefix_ns_array = None
        self._prefix_ns_wrapped_array = None
        self.discriminator = None

        if attribute_string is not None:
            self.attribute_string = attribute_string
        if attribute_number is not None:
            self.attribute_number = attribute_number
        if attribute_integer is not None:
            self.attribute_integer = attribute_integer
        if attribute_boolean is not None:
            self.attribute_boolean = attribute_boolean
        if wrapped_array is not None:
            self.wrapped_array = wrapped_array
        if name_string is not None:
            self.name_string = name_string
        if name_number is not None:
            self.name_number = name_number
        if name_integer is not None:
            self.name_integer = name_integer
        if name_boolean is not None:
            self.name_boolean = name_boolean
        if name_array is not None:
            self.name_array = name_array
        if name_wrapped_array is not None:
            self.name_wrapped_array = name_wrapped_array
        if prefix_string is not None:
            self.prefix_string = prefix_string
        if prefix_number is not None:
            self.prefix_number = prefix_number
        if prefix_integer is not None:
            self.prefix_integer = prefix_integer
        if prefix_boolean is not None:
            self.prefix_boolean = prefix_boolean
        if prefix_array is not None:
            self.prefix_array = prefix_array
        if prefix_wrapped_array is not None:
            self.prefix_wrapped_array = prefix_wrapped_array
        if namespace_string is not None:
            self.namespace_string = namespace_string
        if namespace_number is not None:
            self.namespace_number = namespace_number
        if namespace_integer is not None:
            self.namespace_integer = namespace_integer
        if namespace_boolean is not None:
            self.namespace_boolean = namespace_boolean
        if namespace_array is not None:
            self.namespace_array = namespace_array
        if namespace_wrapped_array is not None:
            self.namespace_wrapped_array = namespace_wrapped_array
        if prefix_ns_string is not None:
            self.prefix_ns_string = prefix_ns_string
        if prefix_ns_number is not None:
            self.prefix_ns_number = prefix_ns_number
        if prefix_ns_integer is not None:
            self.prefix_ns_integer = prefix_ns_integer
        if prefix_ns_boolean is not None:
            self.prefix_ns_boolean = prefix_ns_boolean
        if prefix_ns_array is not None:
            self.prefix_ns_array = prefix_ns_array
        if prefix_ns_wrapped_array is not None:
            self.prefix_ns_wrapped_array = prefix_ns_wrapped_array

    @property
    def attribute_string(self):
        """Gets the attribute_string of this XmlItem.  # noqa: E501


        :return: The attribute_string of this XmlItem.  # noqa: E501
        :rtype: str
        """
        return self._attribute_string

    @attribute_string.setter
    def attribute_string(self, attribute_string):
        """Sets the attribute_string of this XmlItem.


        :param attribute_string: The attribute_string of this XmlItem.  # noqa: E501
        :type attribute_string: str
        """

        self._attribute_string = attribute_string

    @property
    def attribute_number(self):
        """Gets the attribute_number of this XmlItem.  # noqa: E501


        :return: The attribute_number of this XmlItem.  # noqa: E501
        :rtype: float
        """
        return self._attribute_number

    @attribute_number.setter
    def attribute_number(self, attribute_number):
        """Sets the attribute_number of this XmlItem.


        :param attribute_number: The attribute_number of this XmlItem.  # noqa: E501
        :type attribute_number: float
        """

        self._attribute_number = attribute_number

    @property
    def attribute_integer(self):
        """Gets the attribute_integer of this XmlItem.  # noqa: E501


        :return: The attribute_integer of this XmlItem.  # noqa: E501
        :rtype: int
        """
        return self._attribute_integer

    @attribute_integer.setter
    def attribute_integer(self, attribute_integer):
        """Sets the attribute_integer of this XmlItem.


        :param attribute_integer: The attribute_integer of this XmlItem.  # noqa: E501
        :type attribute_integer: int
        """

        self._attribute_integer = attribute_integer

    @property
    def attribute_boolean(self):
        """Gets the attribute_boolean of this XmlItem.  # noqa: E501


        :return: The attribute_boolean of this XmlItem.  # noqa: E501
        :rtype: bool
        """
        return self._attribute_boolean

    @attribute_boolean.setter
    def attribute_boolean(self, attribute_boolean):
        """Sets the attribute_boolean of this XmlItem.


        :param attribute_boolean: The attribute_boolean of this XmlItem.  # noqa: E501
        :type attribute_boolean: bool
        """

        self._attribute_boolean = attribute_boolean

    @property
    def wrapped_array(self):
        """Gets the wrapped_array of this XmlItem.  # noqa: E501


        :return: The wrapped_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._wrapped_array

    @wrapped_array.setter
    def wrapped_array(self, wrapped_array):
        """Sets the wrapped_array of this XmlItem.


        :param wrapped_array: The wrapped_array of this XmlItem.  # noqa: E501
        :type wrapped_array: list[int]
        """

        self._wrapped_array = wrapped_array

    @property
    def name_string(self):
        """Gets the name_string of this XmlItem.  # noqa: E501


        :return: The name_string of this XmlItem.  # noqa: E501
        :rtype: str
        """
        return self._name_string

    @name_string.setter
    def name_string(self, name_string):
        """Sets the name_string of this XmlItem.


        :param name_string: The name_string of this XmlItem.  # noqa: E501
        :type name_string: str
        """

        self._name_string = name_string

    @property
    def name_number(self):
        """Gets the name_number of this XmlItem.  # noqa: E501


        :return: The name_number of this XmlItem.  # noqa: E501
        :rtype: float
        """
        return self._name_number

    @name_number.setter
    def name_number(self, name_number):
        """Sets the name_number of this XmlItem.


        :param name_number: The name_number of this XmlItem.  # noqa: E501
        :type name_number: float
        """

        self._name_number = name_number

    @property
    def name_integer(self):
        """Gets the name_integer of this XmlItem.  # noqa: E501


        :return: The name_integer of this XmlItem.  # noqa: E501
        :rtype: int
        """
        return self._name_integer

    @name_integer.setter
    def name_integer(self, name_integer):
        """Sets the name_integer of this XmlItem.


        :param name_integer: The name_integer of this XmlItem.  # noqa: E501
        :type name_integer: int
        """

        self._name_integer = name_integer

    @property
    def name_boolean(self):
        """Gets the name_boolean of this XmlItem.  # noqa: E501


        :return: The name_boolean of this XmlItem.  # noqa: E501
        :rtype: bool
        """
        return self._name_boolean

    @name_boolean.setter
    def name_boolean(self, name_boolean):
        """Sets the name_boolean of this XmlItem.


        :param name_boolean: The name_boolean of this XmlItem.  # noqa: E501
        :type name_boolean: bool
        """

        self._name_boolean = name_boolean

    @property
    def name_array(self):
        """Gets the name_array of this XmlItem.  # noqa: E501


        :return: The name_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._name_array

    @name_array.setter
    def name_array(self, name_array):
        """Sets the name_array of this XmlItem.


        :param name_array: The name_array of this XmlItem.  # noqa: E501
        :type name_array: list[int]
        """

        self._name_array = name_array

    @property
    def name_wrapped_array(self):
        """Gets the name_wrapped_array of this XmlItem.  # noqa: E501


        :return: The name_wrapped_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._name_wrapped_array

    @name_wrapped_array.setter
    def name_wrapped_array(self, name_wrapped_array):
        """Sets the name_wrapped_array of this XmlItem.


        :param name_wrapped_array: The name_wrapped_array of this XmlItem.  # noqa: E501
        :type name_wrapped_array: list[int]
        """

        self._name_wrapped_array = name_wrapped_array

    @property
    def prefix_string(self):
        """Gets the prefix_string of this XmlItem.  # noqa: E501


        :return: The prefix_string of this XmlItem.  # noqa: E501
        :rtype: str
        """
        return self._prefix_string

    @prefix_string.setter
    def prefix_string(self, prefix_string):
        """Sets the prefix_string of this XmlItem.


        :param prefix_string: The prefix_string of this XmlItem.  # noqa: E501
        :type prefix_string: str
        """

        self._prefix_string = prefix_string

    @property
    def prefix_number(self):
        """Gets the prefix_number of this XmlItem.  # noqa: E501


        :return: The prefix_number of this XmlItem.  # noqa: E501
        :rtype: float
        """
        return self._prefix_number

    @prefix_number.setter
    def prefix_number(self, prefix_number):
        """Sets the prefix_number of this XmlItem.


        :param prefix_number: The prefix_number of this XmlItem.  # noqa: E501
        :type prefix_number: float
        """

        self._prefix_number = prefix_number

    @property
    def prefix_integer(self):
        """Gets the prefix_integer of this XmlItem.  # noqa: E501


        :return: The prefix_integer of this XmlItem.  # noqa: E501
        :rtype: int
        """
        return self._prefix_integer

    @prefix_integer.setter
    def prefix_integer(self, prefix_integer):
        """Sets the prefix_integer of this XmlItem.


        :param prefix_integer: The prefix_integer of this XmlItem.  # noqa: E501
        :type prefix_integer: int
        """

        self._prefix_integer = prefix_integer

    @property
    def prefix_boolean(self):
        """Gets the prefix_boolean of this XmlItem.  # noqa: E501


        :return: The prefix_boolean of this XmlItem.  # noqa: E501
        :rtype: bool
        """
        return self._prefix_boolean

    @prefix_boolean.setter
    def prefix_boolean(self, prefix_boolean):
        """Sets the prefix_boolean of this XmlItem.


        :param prefix_boolean: The prefix_boolean of this XmlItem.  # noqa: E501
        :type prefix_boolean: bool
        """

        self._prefix_boolean = prefix_boolean

    @property
    def prefix_array(self):
        """Gets the prefix_array of this XmlItem.  # noqa: E501


        :return: The prefix_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._prefix_array

    @prefix_array.setter
    def prefix_array(self, prefix_array):
        """Sets the prefix_array of this XmlItem.


        :param prefix_array: The prefix_array of this XmlItem.  # noqa: E501
        :type prefix_array: list[int]
        """

        self._prefix_array = prefix_array

    @property
    def prefix_wrapped_array(self):
        """Gets the prefix_wrapped_array of this XmlItem.  # noqa: E501


        :return: The prefix_wrapped_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._prefix_wrapped_array

    @prefix_wrapped_array.setter
    def prefix_wrapped_array(self, prefix_wrapped_array):
        """Sets the prefix_wrapped_array of this XmlItem.


        :param prefix_wrapped_array: The prefix_wrapped_array of this XmlItem.  # noqa: E501
        :type prefix_wrapped_array: list[int]
        """

        self._prefix_wrapped_array = prefix_wrapped_array

    @property
    def namespace_string(self):
        """Gets the namespace_string of this XmlItem.  # noqa: E501


        :return: The namespace_string of this XmlItem.  # noqa: E501
        :rtype: str
        """
        return self._namespace_string

    @namespace_string.setter
    def namespace_string(self, namespace_string):
        """Sets the namespace_string of this XmlItem.


        :param namespace_string: The namespace_string of this XmlItem.  # noqa: E501
        :type namespace_string: str
        """

        self._namespace_string = namespace_string

    @property
    def namespace_number(self):
        """Gets the namespace_number of this XmlItem.  # noqa: E501


        :return: The namespace_number of this XmlItem.  # noqa: E501
        :rtype: float
        """
        return self._namespace_number

    @namespace_number.setter
    def namespace_number(self, namespace_number):
        """Sets the namespace_number of this XmlItem.


        :param namespace_number: The namespace_number of this XmlItem.  # noqa: E501
        :type namespace_number: float
        """

        self._namespace_number = namespace_number

    @property
    def namespace_integer(self):
        """Gets the namespace_integer of this XmlItem.  # noqa: E501


        :return: The namespace_integer of this XmlItem.  # noqa: E501
        :rtype: int
        """
        return self._namespace_integer

    @namespace_integer.setter
    def namespace_integer(self, namespace_integer):
        """Sets the namespace_integer of this XmlItem.


        :param namespace_integer: The namespace_integer of this XmlItem.  # noqa: E501
        :type namespace_integer: int
        """

        self._namespace_integer = namespace_integer

    @property
    def namespace_boolean(self):
        """Gets the namespace_boolean of this XmlItem.  # noqa: E501


        :return: The namespace_boolean of this XmlItem.  # noqa: E501
        :rtype: bool
        """
        return self._namespace_boolean

    @namespace_boolean.setter
    def namespace_boolean(self, namespace_boolean):
        """Sets the namespace_boolean of this XmlItem.


        :param namespace_boolean: The namespace_boolean of this XmlItem.  # noqa: E501
        :type namespace_boolean: bool
        """

        self._namespace_boolean = namespace_boolean

    @property
    def namespace_array(self):
        """Gets the namespace_array of this XmlItem.  # noqa: E501


        :return: The namespace_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._namespace_array

    @namespace_array.setter
    def namespace_array(self, namespace_array):
        """Sets the namespace_array of this XmlItem.


        :param namespace_array: The namespace_array of this XmlItem.  # noqa: E501
        :type namespace_array: list[int]
        """

        self._namespace_array = namespace_array

    @property
    def namespace_wrapped_array(self):
        """Gets the namespace_wrapped_array of this XmlItem.  # noqa: E501


        :return: The namespace_wrapped_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._namespace_wrapped_array

    @namespace_wrapped_array.setter
    def namespace_wrapped_array(self, namespace_wrapped_array):
        """Sets the namespace_wrapped_array of this XmlItem.


        :param namespace_wrapped_array: The namespace_wrapped_array of this XmlItem.  # noqa: E501
        :type namespace_wrapped_array: list[int]
        """

        self._namespace_wrapped_array = namespace_wrapped_array

    @property
    def prefix_ns_string(self):
        """Gets the prefix_ns_string of this XmlItem.  # noqa: E501


        :return: The prefix_ns_string of this XmlItem.  # noqa: E501
        :rtype: str
        """
        return self._prefix_ns_string

    @prefix_ns_string.setter
    def prefix_ns_string(self, prefix_ns_string):
        """Sets the prefix_ns_string of this XmlItem.


        :param prefix_ns_string: The prefix_ns_string of this XmlItem.  # noqa: E501
        :type prefix_ns_string: str
        """

        self._prefix_ns_string = prefix_ns_string

    @property
    def prefix_ns_number(self):
        """Gets the prefix_ns_number of this XmlItem.  # noqa: E501


        :return: The prefix_ns_number of this XmlItem.  # noqa: E501
        :rtype: float
        """
        return self._prefix_ns_number

    @prefix_ns_number.setter
    def prefix_ns_number(self, prefix_ns_number):
        """Sets the prefix_ns_number of this XmlItem.


        :param prefix_ns_number: The prefix_ns_number of this XmlItem.  # noqa: E501
        :type prefix_ns_number: float
        """

        self._prefix_ns_number = prefix_ns_number

    @property
    def prefix_ns_integer(self):
        """Gets the prefix_ns_integer of this XmlItem.  # noqa: E501


        :return: The prefix_ns_integer of this XmlItem.  # noqa: E501
        :rtype: int
        """
        return self._prefix_ns_integer

    @prefix_ns_integer.setter
    def prefix_ns_integer(self, prefix_ns_integer):
        """Sets the prefix_ns_integer of this XmlItem.


        :param prefix_ns_integer: The prefix_ns_integer of this XmlItem.  # noqa: E501
        :type prefix_ns_integer: int
        """

        self._prefix_ns_integer = prefix_ns_integer

    @property
    def prefix_ns_boolean(self):
        """Gets the prefix_ns_boolean of this XmlItem.  # noqa: E501


        :return: The prefix_ns_boolean of this XmlItem.  # noqa: E501
        :rtype: bool
        """
        return self._prefix_ns_boolean

    @prefix_ns_boolean.setter
    def prefix_ns_boolean(self, prefix_ns_boolean):
        """Sets the prefix_ns_boolean of this XmlItem.


        :param prefix_ns_boolean: The prefix_ns_boolean of this XmlItem.  # noqa: E501
        :type prefix_ns_boolean: bool
        """

        self._prefix_ns_boolean = prefix_ns_boolean

    @property
    def prefix_ns_array(self):
        """Gets the prefix_ns_array of this XmlItem.  # noqa: E501


        :return: The prefix_ns_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._prefix_ns_array

    @prefix_ns_array.setter
    def prefix_ns_array(self, prefix_ns_array):
        """Sets the prefix_ns_array of this XmlItem.


        :param prefix_ns_array: The prefix_ns_array of this XmlItem.  # noqa: E501
        :type prefix_ns_array: list[int]
        """

        self._prefix_ns_array = prefix_ns_array

    @property
    def prefix_ns_wrapped_array(self):
        """Gets the prefix_ns_wrapped_array of this XmlItem.  # noqa: E501


        :return: The prefix_ns_wrapped_array of this XmlItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._prefix_ns_wrapped_array

    @prefix_ns_wrapped_array.setter
    def prefix_ns_wrapped_array(self, prefix_ns_wrapped_array):
        """Sets the prefix_ns_wrapped_array of this XmlItem.


        :param prefix_ns_wrapped_array: The prefix_ns_wrapped_array of this XmlItem.  # noqa: E501
        :type prefix_ns_wrapped_array: list[int]
        """

        self._prefix_ns_wrapped_array = prefix_ns_wrapped_array

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_json_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        def get_value(val):
            if hasattr(val, "to_json_dict"):
                return val.to_json_dict()
            elif hasattr(val, "to_dict"):
                return val.to_dict()
            else:
                return val

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            key = self.attribute_map.get(attr, attr)
            if isinstance(value, list):
                result[key] = list(map(
                    lambda x: get_value(x),
                    value
                ))
            elif hasattr(value, "to_json_dict"):
                result[key] = value.to_json_dict()
            elif hasattr(value, "to_dict"):
                result[key] = value.to_dict()
            elif isinstance(value, dict):
                result[key] = dict(map(
                    lambda item: (item[0], get_value(item[1])),
                    value.items()
                ))
            else:
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
        if not isinstance(other, XmlItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XmlItem):
            return True

        return self.to_dict() != other.to_dict()
