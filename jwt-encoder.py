#!/usr/bin/env python

import click
import jwt
import time

@click.command()
@click.option('--uid', help='Unique ID of the user.', required=True)
@click.option('--private-key-path', help='File path of the auth token secret.', required=True)
@click.option('--duration', default=86400, help='Time until token expiration, in seconds.')
@click.option('--algorithm', default='HS256', help='Algorithm to encode with.')
def cli(private_key_path, uid, duration, algorithm):
    expTime = time.time() + (3600 * duration)
    file = open(private_key_path, 'r')
    secret_key = file.read()
    token = jwt.encode({'exp': expTime, 'uid': uid}, secret_key, algorithm=algorithm)
    click.echo(token)

cli()
