# Calculates Body Mass Index
[![Codeship Status for romenrg/body-mass-index](https://app.codeship.com/projects/e0077cc0-7641-43c1-9cb1-1b41646a852d/status?branch=master)](https://app.codeship.com/projects/422578)
> Python module that provides utilities related to calculating the Body Mass Index (BMI). Also provides a Command Line Interface (CLI). 

## Table of contents

- [Module usage](#module-usage)
    - [Install & Import](#install--import)
    - [Available functions](#available-functions)
- [Standalone usage](#standalone-usage)
    - [Run the CLI](#run-the-cli)
    - [Available CLI commands](#available-cli-commands)
- [Source code usage](#module-usage)
    - [Build](#build)
    - [Test](#test)
    - [Run](#run)
- [Contribute](#contribute)

## Module usage

This library can be used from Python code, imported as a Python module.

### Install & Import

In order to use this library:
 * Install it with pip (consider using pipfiles to keep track of your dependencies)
 * import it in your code
 
### Available functions

* Two static methods:
    * `calculate_bmi`: Calculates BMI, provided weight (kg) and height (m)
    * `calculate_weight`: Calculates weight (kg), provided height (m) and BMI
* Several class methods:
    * `calculate_bmi_with_info`: Calculate BMI with range info, provided weight (kg), height (m) and language
    * `get_bmi_range_info`: Return range info, provided BMI and language
    * `get_bmi_ranges_info`: Return info of all ranges
    * `calculate_weight_boundaries`: Calculate weight boundaries (kg), based on BMI; provided height (m) 
    * `calculate_weight_ranges_with_info`: Calculate weight ranges (kg), based on BMI ranges; provided height (m) and language
    * `calculate_healthy_weight`: Calculate healthy weight range (kg), provided height (m)
* Module provides class attributes:
    * `boundaries`: List with the boundaries for BMI ranges, as defined by the WHO
    * `ranges_i18n`: Text defining each BMI range, as per the WHO, in English and Spanish
   

## Standalone usage

This library can also be used as a CLI utility. And it can be run both with Python or with Docker.

### Run the CLI

Install it with pip.

Then, you can run the CLI utility in two different ways.

#### As a Python module
`python3 -m bmi  [command] [params]`

#### As a Docker container
`docker run -it romenrg/bmi:0.0.1 [command] [params]`

Notes:
* If no command is provided, help will be displayed
* Example providing command with parameters `docker run -it romenrg/bmi:0.0.1 calculate 80 1.80`

### Available CLI commands

* `calculate_bmi`: Calculate BMI, provided weight (kg) and height (m) [info]
* `get_bmi_range_info`: Return range info, provided BMI and language
* `get_bmi_ranges_info`: Return info of all BMI ranges
* `calculate_weight`: Calculate weight (kg), provided height (m) and BMI
* `calculate_weight_ranges_info`: Calculate weight ranges (kg), based on BMI ranges; provided height (m)
* `calculate_healthy_weight`: Calculate healthy weight range (kg), provided height (m)


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
