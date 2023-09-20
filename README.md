# Python Typescript Transformer Example Repository

This repository contains a simple example of a Python Typescript Transformer.

## Entrypoint

The `main.ts` file is the entrypoint for the transformer. It contains the following endpoints:

### GET /health

This endpoint is used by the transformer shell to check if the transformer is healthy.

### POST /transform

This endpoint is used by the transformer shell to transform data.

## Development

prerequisites:
- Python
- NodeJS (required for tests)
- Docker

create environment
```bash
python -m venv .testvenv
soruce .testvenv/bin/activate
```

install dependencies:
```bash
pip install -r requirements.txt
```

run the transformer shell
```bash
docker-compose -f test/docker/docker-compose.yaml up -d
```

> Note:
> If you want to run the transformer locally without tests and use something like Postman or Insomnia to test it manually, run with ` uvicorn --app-dir src main:app --reload`

> Note:
> If you want to skip tests all together as part of the build process,remove the `.github/workflows/test.yml` workflow file

## Testing

Install test environment requirements
```bash
yarn install
```

In another terminal or tab, run:
```bash
yarn test:watch
```

to run the tests on the built transformer.

When changes are made any of the files the transformer will be reloaded and the tests will be run again.

### Change the transformer

To change the transformer modify the contents of the transformer method

### Change the input and output data

To change the validation of inputs and outputs edit the `test/expected.json` file. This file specify the event payloads that are sent to the transformer and the expected output. The `:uuid:` and `:date:` values for the expected outcome matches to any string.

### Further customization

Change the `test/app.spec.ts` file to add additional tests and more advanced validation. Further change the files in the `src` directory to add more advanced logic.

## Deployment

The github action will automatically build and push the release artifact to the github release.

Pushes to the `main` branch will trigger a release pull request, that runs tests to validate the release. Once the pull request has been merged the release will be published, together with the artifact.

To use this transformer in the [Flowcore](https://flowcore.io) platform, create a new adapter and point it to the github release artifact.

The shell will then download the artifact, run it and for each data point post to the `transform` endpoint.