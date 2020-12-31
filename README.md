# Calculates Body Mass Index
[![Codeship Status for romenrg/body-mass-index](https://app.codeship.com/projects/e0077cc0-7641-43c1-9cb1-1b41646a852d/status?branch=master)](https://app.codeship.com/projects/422578)
> Python module that provides utilities related to calculating the Body Mass Index (BMI). Also provides a CLI. 

## Build

### As a Docker container
`docker build --tag=romenrg/bmi:0.0.1 .`

## Test

### As a Python module
`python3 -m unittest`

### As a Docker container
`docker run -it --entrypoint python3 romenrg/bmi:0.0.1 -m unittest`

## Run

### As a Python module
`python3 -m bmi  [command] [params]`

### As a Docker container
`docker run -it romenrg/bmi:0.0.1 [command] [params]`

Notes:
* If no command is provided, help will be displayed
* Example providing command with parameters `docker run -it romenrg/bmi:0.0.1 calculate 80 1.80`

## Contribute

Any contributions (i.e. PRs or issues) are welcome. Please feel free to propose changes following [the contributing guideline](CONTRIBUTING.md).
