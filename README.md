nose-testrail
============

This nose plugin purpose is to send a test result data to [TestRail](http://www.gurock.com/testrail/).

## Instalation

Using [pip](https://pypi.python.org/pypi/pip):

```
pip install git+https://bitbucket.org/50onred/nose-testrail.git@master#egg=krypton-master
```

## Requirements

* [nose](https://nose.readthedocs.org/en/latest/)
* Python 2.7
* testrail account

## Environment Variables
Some environment variables are needed to run this plugin.

* `TESTRAIL_HOST`: URL of your testrail application (example: `example.testrail.com`)
* `TESTRAIL_USERNAME`: Username/Email of the account
* `TESTRAIL_PASSWORD`: Password
* `TESTRAIL_RUN_ID`: TestRail [test run](http://docs.gurock.com/testrail-userguide/userguide-gettingstarted#test_runs_and_tests) ID

## Adding Test Case ID to the test

Decorator `case_id` needs to be specified in each test. Test that doesn't have this decorator will be run in the test execution however the result will net be sent.

Example Test *test_hello.py*:

```
from unittest import TestCase
from nose_testrail.plugin import case_id
import time


class TestOne(TestCase):
    @case_id(1)
    def test_pass(self):
        time.sleep(4)
        self.assertTrue(True)

    @case_id(2)
    def test_failed(self):
        time.sleep(7)
        self.assertTrue(False)
```

## Running nose with nose-testrail
To send test result to TestRail option `--with-nose-testrail` is required.

```
nosetests test_hello.py --with-nose-testrail
```

## Result Sent
This plugin will send the following information.

* Test Result: PASS/FAILED
* Comment: If test failed sending traceback
* Elapsed: Duration of each test.



