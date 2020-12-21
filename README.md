# Calculates Body Mass Index
> Python module that calculates Body Mass Index and returns ranges 

## Config

### i18n
For i18n we are experimenting with gettext:
* Generated the base.pot file with utilities (but can be generated manually)
* Replaced strings with gettext used as "\_" 
* Run `msgfmt -o base.mo base` to "compile" translations
Not sure this is an improvement over having the translations in a data structure as I had it

## Executing tests
`python3 -m unittest`

## Running the program

### As a Python module
`python3 -m bmi`

### As a Docker container

* First build it: `docker build --tag=romenrg/bmi:0.0.1 .`
* Then run it: `docker run -it romenrg/bmi:0.0.1`
