"""
    Umweltbundesamt: Meeresumweltdatenbank (MUDAB)

    Meeres-Monitoringdaten von Küstenbundesländern und Forschungseinrichtungen   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.mudab.model.messstation import Messstation

from deutschland import mudab

globals()["Messstation"] = Messstation
from deutschland.mudab.model.inline_response2001 import InlineResponse2001


class TestInlineResponse2001(unittest.TestCase):
    """InlineResponse2001 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse2001(self):
        """Test InlineResponse2001"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineResponse2001()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()