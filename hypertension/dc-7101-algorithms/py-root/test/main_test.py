import pytest
from lib.main import main
from test.data.htn_data import general_request_data

@pytest.mark.parametrize(
    "request_data, response",
    [
        # 0 readings
        (
            {
                "bp": [
                    {
                        "diastolic": 115,
                        "systolic": 180,
                        "date": "2021-11-01"
                    },
                    {
                        "diastolic": 110,
                        "systolic": 200,
                        "date": "2021-09-01"
                    }
                ],
                "medication": [],
                'date_of_claim': '2021-11-09',
            },
            {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
                "body": {
                    "predominance_calculation": {
                        'sufficient_to_autopopulate': True,
                        "success": True,
                        'predominant_diastolic_reading': 115,
                        'predominant_systolic_reading': 180
                    },
                    "diastolic_history_calculation": {
                        "diastolic_bp_predominantly_100_or_more": True,
                        "success": True 
                    }
                }
            }
        ),
    ],
)
def test_main(request_data, response):
    assert main(request_data) == response

