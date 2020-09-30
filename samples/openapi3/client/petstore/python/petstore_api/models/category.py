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


class Category(object):
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
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, id=None, name='default-name', local_vars_configuration=None):  # noqa: E501
        """Category - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name

    @property
    def id(self):
        """Gets the id of this Category.  # noqa: E501


        :return: The id of this Category.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Category.


        :param id: The id of this Category.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Category.  # noqa: E501


        :return: The name of this Category.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Category.


        :param name: The name of this Category.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, Category):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Category):
            return True

        return self.to_dict() != other.to_dict()
