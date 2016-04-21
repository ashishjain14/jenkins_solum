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

"""
Handler for API request
"""

import logging
from os import listdir
import requests
import ConfigParser
import uuid

log = logging.getLogger(__name__)

headers = {
        "Content-Type": "application/xml"
    }

class ApiHandler():

    def create_pipeline(self, **kwargs):
        param_list=""
        config_file = "/home/vagrant/jenkins_solum/etc/config/js.conf"
        config = ConfigParser.RawConfigParser()
        config.read(config_file)
        jenkins_template_dir = config.get("jenkins", "job_template_dir")
        jenkins_url = config.get("jenkins", "jenkins_url")
        job_prefix = "createItem?name="

        files = listdir(jenkins_template_dir)

        #Creates jobs in jenkins
        for f in files:
            job_name = f.split('.')[0]
            base_xml = open(jenkins_template_dir+f).read()
            job_creation_url = jenkins_url+job_prefix+job_name
            print job_creation_url
            http_request("POST", job_creation_url, headers, base_xml)


        trigger_job = config.get("jenkins", "trigger_job")
        #fire jenkins pipeline first job
        job_param_list = config.items("jobs_param")
        print job_param_list

        #static param list
        for params in job_param_list:
            param_list = param_list+params[0]+"="+params[1]+"&"

        print param_list

        dynamic_job_param_list = config.items("jobs_param_dynamic")
        #dynamic param list
        rand1 = uuid.uuid4()
        for params in dynamic_job_param_list:
            temp=params[1] % rand1
            param_list = param_list+params[0]+"="+temp+"&"

        print param_list

        pipeline_trigger_url = jenkins_url+"job/"+trigger_job+"/buildWithParameters?"+param_list
           
        print "Pipeline trigger url is ::"
        
        print pipeline_trigger_url
        http_request("POST", pipeline_trigger_url, headers, None)

        """
        base_xml = open(config_file).read()
        request_url = "http://192.168.76.2:8888/"
        job_url = "createItem?name="+"test"
        job_url1 = "job/test/build"
        for op in job_param_list:
            print op[0], op[1]

        job_params = 'test123="sheifali"&sample123="ashishjain"&testparam="iririririr"'
        job_url1 = "job/test/buildWithParameters?"+job_params

        net_url = request_url + job_url
        net_url1 = request_url + job_url1

        print net_url
        print net_url1

        http_request("POST", net_url, headers, base_xml)
        http_request("POST", net_url1, headers, None)

        print "hello"
        """


def http_request(request_type, request_url, headers, payload):
    """
    :param request_type - Valid values GET, POST, DELETE
    :param request_url - HTTP Request URL
    :param headers - HTTP Request headers
    :param payload - Payload for GET or POST request

    """

    resp = {}
    if request_type == 'POST':
        resp = requests.post(request_url, data = payload,
                                 headers = headers)
    return resp
