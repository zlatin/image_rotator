# Image rotator

API that allows you to upload products with images.
Image is rotated and rotation time measured on uplod.
Product can only be edited once.

## Development

To start development

1. Install dependencies with

   pipenv install

1. copy `env-development` to `.env`. Never use development env settings in production

   cp env-development .env

To run dev server run

    pipenv run server

To run tests run command

    pipenv run test

## Production

For production use copy `env-example` to `.env`.

    cp env-example .env

Edit `.env` file according to your server setup.
