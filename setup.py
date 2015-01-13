from setuptools import find_packages, setup

setup(
    name='nose-testrail',
    version='0.1.0',
    description='Plugin to send test result to testrail',
    author='Daniel Anggrianto',
    author_email='d.anggrianto@gmail.com',
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'nose.plugins.0.10': [
            'nose_testrail = nose_testrail.plugin:NoseTestRail'
        ]
    },
)
