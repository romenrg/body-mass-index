# Body Mass Index (BMI) - Utilities
[![Codeship Status for romenrg/body-mass-index](https://app.codeship.com/projects/e0077cc0-7641-43c1-9cb1-1b41646a852d/status?branch=master)](https://app.codeship.com/projects/422578)
> Python module that provides utilities related to the Body Mass Index (BMI). Also provides a Command Line Interface (CLI). 

## Table of contents

- [Module usage](#module-usage)
    - [Install & Import](#install--import)
    - [Available functions](#available-functions)
- [Standalone usage](#standalone-usage)
    - [Run the CLI](#run-the-cli)
    - [Available CLI commands](#available-cli-commands)
- [Source code usage](#source-code-usage)
    - [Build](#build)
    - [Test](#test)
    - [Run](#run)
- [Contribute](#contribute)

## <a name="module-usage"></a>Module usage

This library can be used from Python code, imported as a Python module.

### <a name="install--import"></a>Install & Import

 * Install it with pip:
    * `pip install body-mass-index`
    * Although you might consider using `pipenv`, which creates a Pipfile to keep track of your dependencies. 
    In that case, the install command would be:
        * `pipenv install body-mass-index`
 * Then, import this module in your code:
     * `from bmi import Bmi`
     * Note that the `Bmi` class contains all the utilities of this module
 * Now, use it.
     * E.g. `Bmi.calculate_bmi(80, 1.80)`
 
### <a name="available-functions"></a>Available functions

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
   

## <a name="standalone-usage"></a>Standalone usage

This library can also be used as a CLI utility. And it can be run both with Python or with Docker.

### <a name="run-the-cli"></a>Run the CLI

Install it with pip.

Then, you can run the CLI utility in two different ways.

#### As a Python module
`python3 -m bmi  [command] [params]`

#### As a Docker container
`docker run -it romenrg/bmi:0.0.1 [command] [params]`

Notes:
* If no command is provided, help will be displayed
* Example providing command with parameters `docker run -it romenrg/bmi:0.0.1 calculate 80 1.80`

### <a name="available-cli-commands"></a>Available CLI commands

* `calculate_bmi`: Calculate BMI, provided weight (kg) and height (m) [info]
* `get_bmi_range_info`: Return range info, provided BMI and language
* `get_bmi_ranges_info`: Return info of all BMI ranges
* `calculate_weight`: Calculate weight (kg), provided height (m) and BMI
* `calculate_weight_ranges_info`: Calculate weight ranges (kg), based on BMI ranges; provided height (m)
* `calculate_healthy_weight`: Calculate healthy weight range (kg), provided height (m)


## <a name="source-code-usage"></a>Source code usage

You can also clone the repository in order to build a Docker image, run tests, execute the module locally and/or 
contribute to keep improving this module.

### <a name="build"></a>Build

Python, as an interpreted language, doesn't have to be built, but the Docker image does.

#### Create a Docker image from sources
`docker build --tag=romenrg/bmi:0.0.1 .`

### <a name="test"></a>Test

Existing unit tests can be run in two different ways.

#### As a Python module
`python3 -m unittest`

#### As a Docker container
`docker run -it --entrypoint python3 romenrg/bmi:0.0.1 -m unittest`

### <a name="run"></a>Run

You can run the CLI from the source code in the same way you can when you installed it. See the [Run the CLI](#run-the-cli) section.


## <a name="contribute"></a>Contribute

Any contributions (i.e. PRs or issues) are welcome. Please feel free to propose changes following [the contributing guideline](https://github.com/romenrg/body-mass-index/blob/master/CONTRIBUTING.md).
