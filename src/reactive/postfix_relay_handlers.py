# Copyright 2018 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import charms.reactive as reactive
from charm.postfix.postfix_relay import (
    restart_postfix,
    setup_ssl,
    write_configs,
)
from charmhelpers.core.hookenv import (
    config,
    status_set,
)


@reactive.hook('config-changed')
def config_changed():
    status_set('maintenance', 'Updating Postfix configuration')
    if config('ssl_ca'):
        setup_ssl()
    write_configs()
    restart_postfix()
    status_set('active', 'Unit is ready.')
