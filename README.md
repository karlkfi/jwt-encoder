# jwt-encoder
Generates a [JWT](http://jwt.io/) token from a user ID and private key file.

## Usage

docker run --rm -v $PWD/<private_key_file>:/key karlkfi/jwt-encoder <username> /key --duration=86400 --algorithm=HS256
