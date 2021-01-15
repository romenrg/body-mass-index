import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="body-mass-index",
    version="1.0.1",
    author="Romen Rodriguez-Gil",
    author_email="contact@romenrg.com",
    description="Utilities related to the Body Mass Index (BMI): Calculating it, calculating healthy weight, ranges, " +
                "boundaries,...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/romenrg/body-mass-index",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
