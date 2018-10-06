# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from .check import check_run
from .ls import ls
from .start import start
from .stop import stop

ALL_COMMANDS = (
    check_run,
    ls,
    start,
    stop,
)
