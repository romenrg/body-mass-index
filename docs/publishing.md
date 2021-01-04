# Publishing to PyPI

This module has been made available to pip, having been published in [PyPI](https://pypi.org/project/body-mass-index/)

## Steps

* To generate the `dist` folder, with the packaged files, from the repository root, run `python3 setup.py sdist bdist_wheel`.
* Then, upload the new version to PyPI with `python3 -m twine upload --repository testpypi dist/*`.
    * The prompt will ask for credentials. The API token must be provided.

## Detailed steps

See the official guide on [packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

## Other notes

* To include the `logging_config.ini` file, we had to create a `MANIFEST.in` and add the `include_package_data=True` option 
to the setup. 

