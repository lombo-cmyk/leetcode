from unittest import TestCase
from time import time_ns
import logging
import sys
from os import getcwd

logger = logging.getLogger(__name__)
logging.basicConfig(filename=f'{getcwd()}/PythonLogs.log',
                    level=logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stdout_handler)


class TimedTestCase(TestCase):
    test_case_time_start = 0

    def setUp(self) -> None:
        super(TimedTestCase, self).setUp()
        self.test_case_time_start = time_ns()

    def tearDown(self) -> None:
        super(TimedTestCase, self).tearDown()
        logger.info(f"{self._testMethodName}: Test case execution time: "
                    f"{time_ns() - self.test_case_time_start} ns")
