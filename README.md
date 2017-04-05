# jwt-encoder
Generates a [JWT](http://jwt.io/) token from a user ID and private key file.

## Usage

Docker Image: [karlkfi/jwt-encoder](https://hub.docker.com/r/karlkfi/jwt-encoder/)

```
docker run --rm -v "${PWD}/<private_key_file>:/key" karlkfi/jwt-encoder <username> /key --duration=86400 --algorithm=HS256
```
