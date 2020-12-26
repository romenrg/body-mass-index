# Calculates Body Mass Index
[![Codeship Status for romenrg/body-mass-index](https://app.codeship.com/projects/e0077cc0-7641-43c1-9cb1-1b41646a852d/status?branch=master)](https://app.codeship.com/projects/422578)
> Python module that providing Body Mass Index (BMI) utilities. Also providing a CLI. 


## Executing tests
`python3 -m unittest`

## Running the program

### As a Python module
`python3 -m bmi`

### As a Docker container

* First build it: `docker build --tag=romenrg/bmi:0.0.1 .`
* Then run it: `docker run -it romenrg/bmi:0.0.1`