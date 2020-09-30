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


class OuterComposite(object):
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
        'my_number': 'float',
        'my_string': 'str',
        'my_boolean': 'bool'
    }

    attribute_map = {
        'my_number': 'my_number',
        'my_string': 'my_string',
        'my_boolean': 'my_boolean'
    }

    def __init__(self, my_number=None, my_string=None, my_boolean=None, local_vars_configuration=None):  # noqa: E501
        """OuterComposite - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._my_number = None
        self._my_string = None
        self._my_boolean = None
        self.discriminator = None

        if my_number is not None:
            self.my_number = my_number
        if my_string is not None:
            self.my_string = my_string
        if my_boolean is not None:
            self.my_boolean = my_boolean

    @property
    def my_number(self):
        """Gets the my_number of this OuterComposite.  # noqa: E501


        :return: The my_number of this OuterComposite.  # noqa: E501
        :rtype: float
        """
        return self._my_number

    @my_number.setter
    def my_number(self, my_number):
        """Sets the my_number of this OuterComposite.


        :param my_number: The my_number of this OuterComposite.  # noqa: E501
        :type my_number: float
        """

        self._my_number = my_number

    @property
    def my_string(self):
        """Gets the my_string of this OuterComposite.  # noqa: E501


        :return: The my_string of this OuterComposite.  # noqa: E501
        :rtype: str
        """
        return self._my_string

    @my_string.setter
    def my_string(self, my_string):
        """Sets the my_string of this OuterComposite.


        :param my_string: The my_string of this OuterComposite.  # noqa: E501
        :type my_string: str
        """

        self._my_string = my_string

    @property
    def my_boolean(self):
        """Gets the my_boolean of this OuterComposite.  # noqa: E501


        :return: The my_boolean of this OuterComposite.  # noqa: E501
        :rtype: bool
        """
        return self._my_boolean

    @my_boolean.setter
    def my_boolean(self, my_boolean):
        """Sets the my_boolean of this OuterComposite.


        :param my_boolean: The my_boolean of this OuterComposite.  # noqa: E501
        :type my_boolean: bool
        """

        self._my_boolean = my_boolean

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
        if not isinstance(other, OuterComposite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OuterComposite):
            return True

        return self.to_dict() != other.to_dict()
