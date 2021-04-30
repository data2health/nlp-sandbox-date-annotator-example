# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TextDateAnnotationAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, date=None, date_format=None):  # noqa: E501
        """TextDateAnnotationAllOf - a model defined in OpenAPI

        :param date: The date of this TextDateAnnotationAllOf.  # noqa: E501
        :type date: date
        :param date_format: The date_format of this TextDateAnnotationAllOf.  # noqa: E501
        :type date_format: str
        """
        self.openapi_types = {
            'date': date,
            'date_format': str
        }

        self.attribute_map = {
            'date': 'date',
            'date_format': 'dateFormat'
        }

        self._date = date
        self._date_format = date_format

    @classmethod
    def from_dict(cls, dikt) -> 'TextDateAnnotationAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextDateAnnotation_allOf of this TextDateAnnotationAllOf.  # noqa: E501
        :rtype: TextDateAnnotationAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def date(self):
        """Gets the date of this TextDateAnnotationAllOf.

        The date contained in the annotation  # noqa: E501

        :return: The date of this TextDateAnnotationAllOf.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TextDateAnnotationAllOf.

        The date contained in the annotation  # noqa: E501

        :param date: The date of this TextDateAnnotationAllOf.
        :type date: date
        """

        self._date = date

    @property
    def date_format(self):
        """Gets the date_format of this TextDateAnnotationAllOf.

        Date format (ISO 8601)  # noqa: E501

        :return: The date_format of this TextDateAnnotationAllOf.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this TextDateAnnotationAllOf.

        Date format (ISO 8601)  # noqa: E501

        :param date_format: The date_format of this TextDateAnnotationAllOf.
        :type date_format: str
        """

        self._date_format = date_format
