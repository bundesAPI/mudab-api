"""
    Umweltbundesamt: Meeresumweltdatenbank (MUDAB)

    Meeres-Monitoringdaten von Küstenbundesländern und Forschungseinrichtungen   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.mudab.model.filter import Filter
from deutschland.mudab.model.orderby import Orderby
from deutschland.mudab.model.range import Range

from deutschland import mudab

globals()["Filter"] = Filter
globals()["Orderby"] = Orderby
globals()["Range"] = Range
from deutschland.mudab.model.filter_request import FilterRequest


class TestFilterRequest(unittest.TestCase):
    """FilterRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFilterRequest(self):
        """Test FilterRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FilterRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()