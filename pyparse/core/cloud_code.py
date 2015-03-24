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

from __future__ import unicode_literals, division, absolute_import, print_function
from pyparse.request import request


class CloudCode(object):

    @staticmethod
    def call(func_name, **arguments):
        return request('post', 'functions/{}'.format(func_name), arguments=arguments)

    @staticmethod
    def background_job(job_name, **arguments):
        return request('post', 'jobs/{}'.format(job_name), arguments=arguments)