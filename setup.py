from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with open("dev-requirements.txt") as f:
    dev_requires = f.read().splitlines()

setup(
    name='myTFlib',
    version='0.1.0',
    description='My custom TensorFlow-based CV library',
    author='Your Name',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires
    },
)