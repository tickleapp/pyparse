#
# Copyright 2015 Tickle Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import datetime

from pyparse.core.data.types import (GeoPoint, datetime_to_parse_str, datetime_dict_to_python, datetime_str_to_python,
                                     datetime_to_parse_dict)


class Field(object):

    def __init__(self, parse_name=None, python_name=None, readonly=False):
        self._parse_name = parse_name
        self._python_name = python_name
        self._readonly = readonly

    @property
    def parse_name(self):
        return self._parse_name

    @property
    def python_name(self):
        return self._python_name

    @property
    def readonly(self):
        return self._readonly

    def __str__(self):
        return 'python:{0.python_name} - parse:{0.parse_name}'.format(self)

    @staticmethod
    def to_parse(python_value):
        return python_value

    @staticmethod
    def to_python(parse_value):
        return parse_value


class ListField(Field):
    pass


class AutoDateTimeField(Field):

    @staticmethod
    def to_parse(python_value):
        """
        :type python_value: datetime.datetime
        :rtype: str
        """
        return datetime_to_parse_str(python_value)

    @staticmethod
    def to_python(parse_value):
        """
        :type parse_value: str
        :rtype: datetime.datetime
        """
        return datetime_str_to_python(parse_value)


class DateTimeField(Field):

    @staticmethod
    def to_parse(python_value):
        """
        :type python_value: datetime.datetime
        :rtype: dict
        """
        return datetime_to_parse_dict(python_value)

    @staticmethod
    def to_python(parse_value):
        """
        :type parse_value: dict
        :rtype: datetime.datetime
        """
        return datetime_dict_to_python(parse_value)


class NumberField(Field):
    pass


# noinspection PyPep8Naming
def _create_python_convertible_field(name, PythonConvertibleClass):
    """
    :type name: str
    :type PythonConvertibleClass: class
    :rtype: class
    """
    return type(name, (Field,), {
        'to_parse': staticmethod(lambda python_value: python_value.to_parse()),
        'to_python': staticmethod(lambda parse_value: PythonConvertibleClass.to_python(parse_value)),
    })


GeoPointField = _create_python_convertible_field('GeoPointField', GeoPoint)
