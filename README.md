# Calculates Body Mass Index
> Python module that calculates Body Mass Index and returns ranges 

## Executing tests
`python3 -m unittest`

## Running the program

### As a Python module
`python3 -m bmi`

### As a Docker container

* First build it: `docker build --tag=romenrg/bmi:0.0.1 .`
* Then run it: `docker run -it romenrg/bmi:0.0.1`