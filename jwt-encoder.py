#!/usr/bin/env python

import click
import jwt
import time

@click.command()
@click.argument('uid', required=True)
@click.argument('private_key_path', required=True, type=click.File('r'))
@click.option('--duration', default=86400, help='Time until token expiration, in seconds (default: 86400).')
@click.option('--algorithm', default='HS256', help='Algorithm to encode with (default: HS256).')
def cli(uid, private_key_path, duration, algorithm):
    """Generates a JWT token from a user ID and private key file.

    Arguments:
    uid -- Unique ID of the user.
    private_key_path -- File path of the auth token secret.
    """
    expTime = time.time() + (3600 * duration)
    private_key = private_key_path.read()
    token = jwt.encode({'exp': expTime, 'uid': uid}, private_key, algorithm=algorithm)
    click.echo(token)

cli()
