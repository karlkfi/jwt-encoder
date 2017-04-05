#!/usr/bin/env python

import click
import jwt
import time

@click.command()
@click.argument('uid', help='Unique ID of the user.', required=True)
@click.argument('private-key-path', help='File path of the auth token secret.', required=True, type=click.File('r'))
@click.option('--duration', default=86400, help='Time until token expiration, in seconds.')
@click.option('--algorithm', default='HS256', help='Algorithm to encode with.')
def cli(uid, private_key_file, duration, algorithm):
    expTime = time.time() + (3600 * duration)
    private_key = private_key_file.read()
    token = jwt.encode({'exp': expTime, 'uid': uid}, private_key, algorithm=algorithm)
    click.echo(token)

cli()
