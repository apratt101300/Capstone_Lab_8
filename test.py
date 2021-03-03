import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin_converter

class Test_Bitcoin_Converter(TestCase):
    
    @patch('bitcoin_converter.get_bitcoin_api_response')
    def test_calculate_USD(self, mock_rates):
        mock_rate = 1234.567
        # mock_api_response = '{"bpi":{"USD":{"rate_float":51407.7933}}}'
        mock_api_response = {
                            "time": {
                            "updated": "Mar 3, 2021 17:20:00 UTC",
                            "updatedISO": "2021-03-03T17:20:00+00:00",
                            "updateduk": "Mar 3, 2021 at 17:20 GMT"
                            },
                            "disclaimer": " ",
                            "chartName": "Bitcoin",
                            "bpi": {
                            "USD": {
                            "code": "USD",
                            "symbol": "&#36;",
                            "rate": "51,407.7933",
                            "description": "United States Dollar",
                            "rate_float": mock_rate
                            },
                            "GBP": {
                            "code": "GBP",
                            "symbol": "&pound;",
                            "rate": "36,777.1354",
                            "description": "British Pound Sterling",
                            "rate_float": 36777.1354
                            },
                            "EUR": {
                            "code": "EUR",
                            "symbol": "&euro;",
                            "rate": "42,579.0703",
                            "description": "Euro",
                            "rate_float": 42579.0703
                            }
                            }
                            }
        mock_rates.side_effect = [ mock_api_response ]
        result = bitcoin_converter.calculate_USD(5)
        self.assertEqual(6172.835, result)

                        

if __name__ == '__main__':
    unittest.main()                        