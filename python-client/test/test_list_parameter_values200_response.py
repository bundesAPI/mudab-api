"""
    Umweltbundesamt: Meeresumweltdatenbank (MUDAB)

    Meeres-Monitoringdaten von Küstenbundesländern und Forschungseinrichtungen   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.mudab.model.parameter_value import ParameterValue

from deutschland import mudab

globals()["ParameterValue"] = ParameterValue
from deutschland.mudab.model.list_parameter_values200_response import (
    ListParameterValues200Response,
)


class TestListParameterValues200Response(unittest.TestCase):
    """ListParameterValues200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListParameterValues200Response(self):
        """Test ListParameterValues200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListParameterValues200Response()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()