# Changelog for Evergreen Skills for Software Developers

This file keeps a log of version releases. This file is maintained
[following best practices about changelogs](https://keepachangelog.com/en/1.0.0/).

## Versioning guideline

* Each significant change should be described in the "unpublished" section
* Entry versions should follow the following:
  * Syntax:
    * [X.Y.Z] - YYYY-MM-DD (Short description)
  * Convention:
    * For X.Y.Z, increment the digit following this scheme:
      * X = breaking change (previous version is now deprecated),
      * Y = additive change (previous version is still valid),
      * Z = just a simple patch (for a typo or error).
* When the new version is released, a new [Unreleased] section is created in the "Release Change History" below.

## Release Change History

### [1.0.0] - 2020-12-26 (First release)

#### Added

* Module provides:
    * Two static methods:
        * `calculate_bmi`: Calculates BMI, provided weight and height
        * `calculate_weight`: Calculates weight, provided height and BMI
    * Several class methods:
        * `calculate_bmi_with_info`: Calculate BMI with range info, providing weight, height and language
        * `range_info`: Return range info, providing BMI and language
        * `ranges_with_info`: Return info of all ranges
        * `calculate_weight_ranges`: Return weight ranges, providing height 
        * `calculate_weight_ranges_with_info`: Return weight ranges info, providing height and language
        * `calculate_healthy_weight`: Return healthy weight range, providing height
    * Module provides class attributes:
        * `boundaries`: List with the boundaries for BMI ranges, as defined by the WHO
        * `ranges_i18n`: Text defining each BMI range, as per the WHO, in English and Spanish
* CLI provides several commands:
    * `calculate`: Calculate BMI, providing weight and height
    * `calculate_info`: Calculate BMI with range info, providing weight, height and language
    * `range_info`: Return range info, providing BMI and language
    * `ranges_info`: Return info of all ranges
    * `calculate_weight`: Calculate weight, providing height and BMI
    * `weight_ranges`: Calculate weight ranges, providing height
    * `healthy_weight`: Show healthy weight range, providing height

#### Changed

* .

#### Removed

* .
