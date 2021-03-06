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

# Ref: Parse Error Code: http://www.parse.com/docs/dotnet/api/html/T_Parse_ParseException_ErrorCode.htm


class ParseError(Exception):

    def __init__(self, code, reason):
        self.code = code
        """:type: int"""
        self.reason = reason
        """:type: str"""

    def __str__(self):
        return '{0.reason} ({0.code}) '.format(self)


class ParseInternalServerError(ParseError):
    pass
