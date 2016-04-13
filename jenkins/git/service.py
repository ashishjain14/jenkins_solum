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

"""
Parses configuration file, initializes logger
"""

from oslo_config import cfg

from jenkins.git.pecan import log_helper

# Register options for logger
LOGGING_SERVICE_OPTS = [
    cfg.StrOpt('log_file',
               help='Log file location'),
    cfg.StrOpt('log_level',
               help='Loggging level'),
]

def prepare_service(service_name, argv=[]):
    """

    :param service_name: Name of the service
    :param argv: Configuration file
    :return:
    """

    cfg.CONF(argv[1:], project='japi')

    opt_group = cfg.OptGroup(name=service_name, title='Logging options for\
                                                      the service')
    cfg.CONF.register_group(opt_group)
    cfg.CONF.register_opts(LOGGING_SERVICE_OPTS, opt_group)

    log_file = cfg.CONF._get("log_file", group=opt_group)
    log_level = cfg.CONF._get("log_level", group=opt_group)

    log_helper.setup_logging(log_file, log_level)