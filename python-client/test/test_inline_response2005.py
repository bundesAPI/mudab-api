"""
    Umweltbundesamt: Meeresumweltdatenbank (MUDAB)

    Meeres-Monitoringdaten von Küstenbundesländern und Forschungseinrichtungen   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.mudab.model.parameter import Parameter

from deutschland import mudab

globals()["Parameter"] = Parameter
from deutschland.mudab.model.inline_response2005 import InlineResponse2005


class TestInlineResponse2005(unittest.TestCase):
    """InlineResponse2005 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse2005(self):
        """Test InlineResponse2005"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineResponse2005()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()