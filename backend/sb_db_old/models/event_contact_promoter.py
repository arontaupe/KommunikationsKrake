# coding: utf-8

"""
    Sommerblut-Database

    Event and festival info  # noqa: E501

    OpenAPI spec version: 1.5.0
    Contact: support@xtain.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventContactPromoter(object):
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
        'id': 'int',
        'firstname': 'str',
        'surname': 'str',
        'email': 'str',
        'phone': 'str',
        'mobile': 'str',
        'web': 'str',
        'location': 'Location'
    }

    attribute_map = {
        'id': 'id',
        'firstname': 'firstname',
        'surname': 'surname',
        'email': 'email',
        'phone': 'phone',
        'mobile': 'mobile',
        'web': 'web',
        'location': 'location'
    }

    def __init__(self, id=None, firstname=None, surname=None, email=None, phone=None, mobile=None, web=None, location=None):  # noqa: E501
        """EventContactPromoter - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._firstname = None
        self._surname = None
        self._email = None
        self._phone = None
        self._mobile = None
        self._web = None
        self._location = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if firstname is not None:
            self.firstname = firstname
        if surname is not None:
            self.surname = surname
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if mobile is not None:
            self.mobile = mobile
        if web is not None:
            self.web = web
        if location is not None:
            self.location = location

    @property
    def id(self):
        """Gets the id of this EventContactPromoter.  # noqa: E501


        :return: The id of this EventContactPromoter.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventContactPromoter.


        :param id: The id of this EventContactPromoter.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def firstname(self):
        """Gets the firstname of this EventContactPromoter.  # noqa: E501


        :return: The firstname of this EventContactPromoter.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this EventContactPromoter.


        :param firstname: The firstname of this EventContactPromoter.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def surname(self):
        """Gets the surname of this EventContactPromoter.  # noqa: E501


        :return: The surname of this EventContactPromoter.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this EventContactPromoter.


        :param surname: The surname of this EventContactPromoter.  # noqa: E501
        :type: str
        """

        self._surname = surname

    @property
    def email(self):
        """Gets the email of this EventContactPromoter.  # noqa: E501


        :return: The email of this EventContactPromoter.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EventContactPromoter.


        :param email: The email of this EventContactPromoter.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this EventContactPromoter.  # noqa: E501


        :return: The phone of this EventContactPromoter.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this EventContactPromoter.


        :param phone: The phone of this EventContactPromoter.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def mobile(self):
        """Gets the mobile of this EventContactPromoter.  # noqa: E501


        :return: The mobile of this EventContactPromoter.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this EventContactPromoter.


        :param mobile: The mobile of this EventContactPromoter.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def web(self):
        """Gets the web of this EventContactPromoter.  # noqa: E501


        :return: The web of this EventContactPromoter.  # noqa: E501
        :rtype: str
        """
        return self._web

    @web.setter
    def web(self, web):
        """Sets the web of this EventContactPromoter.


        :param web: The web of this EventContactPromoter.  # noqa: E501
        :type: str
        """

        self._web = web

    @property
    def location(self):
        """Gets the location of this EventContactPromoter.  # noqa: E501


        :return: The location of this EventContactPromoter.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EventContactPromoter.


        :param location: The location of this EventContactPromoter.  # noqa: E501
        :type: Location
        """

        self._location = location

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
        if issubclass(EventContactPromoter, dict):
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
        if not isinstance(other, EventContactPromoter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other