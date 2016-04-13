# Copyright 2016 - Wipro Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""v1 API Controller"""

import logging

from pecan import expose
from pecan import request
from webob.exc import status_map

from jenkins.git.handler import handler as api_handler

log = logging.getLogger(__name__)


class JenkinsController(object):

    @expose(generic=True, template='index.html')
    def index(self):
        return dict()

    # Method to create jenkins job pipeline
    @index.when(method='POST', template='json')
    def post(self, **kwargs):
        log.info("Received request to create a job pipeline")

        handler = api_handler.ApiHandler()
        resp = handler.create_pipeline(**kwargs)
        return resp