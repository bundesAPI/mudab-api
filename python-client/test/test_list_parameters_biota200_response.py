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
from deutschland.mudab.model.list_parameters_biota200_response import (
    ListParametersBiota200Response,
)


class TestListParametersBiota200Response(unittest.TestCase):
    """ListParametersBiota200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListParametersBiota200Response(self):
        """Test ListParametersBiota200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListParametersBiota200Response()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
