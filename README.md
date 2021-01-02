# Calculates Body Mass Index
[![Codeship Status for romenrg/body-mass-index](https://app.codeship.com/projects/e0077cc0-7641-43c1-9cb1-1b41646a852d/status?branch=master)](https://app.codeship.com/projects/422578)
> Python module that provides utilities related to calculating the Body Mass Index (BMI). Also provides a Command Line Interface (CLI). 

## Module usage

This library can be used from Python code, imported as a Python module.

### Importing it

In order to use this library:
 * Install it with pip (consider using pipfiles to keep track of your dependencies)
 * import it in your code

## Standalone usage

This library can also be used as a CLI utility. And it can be run both with Python or with Docker.

### Run the module

Install it with pip.

Then, you can run the CLI utility in two different ways.

### As a Python module
`python3 -m bmi  [command] [params]`

### As a Docker container
`docker run -it romenrg/bmi:0.0.1 [command] [params]`

Notes:
* If no command is provided, help will be displayed
* Example providing command with parameters `docker run -it romenrg/bmi:0.0.1 calculate 80 1.80`

## Source code usage

You can also, clone the source repo in order to build a Docker image, run tests and/or contribute.

### Build

Python, as an interpreted language, doesn't have to be built, but the Docker image does.

#### Create a Docker image from sources
`docker build --tag=romenrg/bmi:0.0.1 .`

### Test

Existing unit tests can be run in two different ways.

#### As a Python module
`python3 -m unittest`

#### As a Docker container
`docker run -it --entrypoint python3 romenrg/bmi:0.0.1 -m unittest`

### Run

You can run the module from sources in the same way you can once you have installed it. See [Run the module](#run-the-module)

## Contribute

Any contributions (i.e. PRs or issues) are welcome. Please feel free to propose changes following [the contributing guideline](CONTRIBUTING.md).
