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


import eventlet
from eventlet import wsgi
import logging
import os
from oslo_config import cfg
import sys

from . import service
from jenkins.git.pecan import api

log = logging.getLogger(__name__)


def main():
    eventlet.monkey_patch(socket=True, select=True, time=True)
    service.prepare_service("jenkins_solum", sys.argv)
    log.info('Completed configuration file parsing...')
    log.info('Completed logger initialization...')
    app = api.setup_app()
    log.info('Pecan app setup complete...')

    host, port = cfg.CONF.japi.host, cfg.CONF.japi.port

    log.info('Jenkins_Solum api server started in PID %s' % os.getpid())
    log.info('Jenkins_Solum api server is now serving on http://%(host)s:%(port)s' % dict(
            host=host, port=port))
    print ('Jenkins_Solum api server is now serving on http://%(host)s:%(port)s' % dict(
            host=host, port=port))

    wsgi.server(eventlet.listen((host, port)), app, log=log)
