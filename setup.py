from setuptools import find_packages, setup

# with open("README.md", "r", encoding = "utf-8") as fh:
#     long_description = fh.read()

setup(
    name='drdroid-sdk',
    setup_requires=['wheel'],
    packages=['pydoctordroid'],
    include_package_data=True,
    version='0.1.0',
    description='Code Marker Library from Doctor Droid to generate custom events',
    author='Dipesh Mittal',
    author_email="dipesh@drdroid.io",
    license='MIT',
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["urllib3>=1.26.11"],
)
