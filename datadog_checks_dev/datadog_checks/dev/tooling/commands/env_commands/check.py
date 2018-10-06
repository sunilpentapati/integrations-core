# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import click

from ..utils import CONTEXT_SETTINGS, abort
from ...e2e import create_interface, get_configured_envs


@click.command(
    'check',
    context_settings=CONTEXT_SETTINGS,
    short_help='Run an Agent check'
)
@click.argument('check')
@click.argument('env', required=False)
@click.option('--rate', '-r', is_flag=True)
def check_run(check, env, rate):
    """Run an Agent check."""
    envs = get_configured_envs(check)
    if not envs:
        abort('No active environments found for `{}`.'.format(check))

    if not env:
        if len(envs) > 1:
            abort('Multiple active environments found for `{}`, please specify one.'.format(check))

        env = envs[0]

    if env not in envs:
        abort('`{}` is not an active environment.'.format(env))

    environment = create_interface(check, env)

    environment.run_check(rate=rate)
