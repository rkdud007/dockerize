from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='hdp',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    package_data={
        'hdp': [
            'compiled_cairo/*',
            'build/compiled_cairo_files/*',
            'tools/py/*',
            'packages/hdp_bootloader/*'
        ],
    },
)