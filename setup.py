from setuptools import find_packages, setup

# with open("README.md", "r", encoding = "utf-8") as fh:
#     long_description = fh.read()

setup(
    name='pydoctordroid',
    setup_requires=['wheel'],
    packages=find_packages(),
    include_package_data=True,
    version='0.0.1',
    description='Code Marker Library from Doctor Droid to generate custom events',
    author='Dipesh Mittal',
    author_email = "dipesh@drdroid.io",
    license='MIT',
    python_requires = ">=3.6",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests>=2.28.2, <3.0.0", "protobuf>=4.21.12"],
)