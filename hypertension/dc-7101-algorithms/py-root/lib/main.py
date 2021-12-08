from typing import Dict
from .utils import sufficient_to_autopopulate, history_of_diastolic_bp

def main(event: Dict):
    try:
        statusCode = 200
        predominance_calculation = sufficient_to_autopopulate(event)
        diastolic_history_calculation = history_of_diastolic_bp(event)
        predominance_calculation_status = predominance_calculation["success"]
        diastolic_history_calculation_status = diastolic_history_calculation["success"]

        # if sufficient_to_autopopulate returns 'success': False, but history_of_diastolic_bp doesn't
        # Note that the inverse can't happen (where history_of_diastolic_bp fails while sufficient_to_autopopulate doesn't)
        # because the only way history_of_diastolic_bp can fail is if there are no bp readings, which would cause
        # sufficient_to_autopopulate to fail as well
        if (
            (diastolic_history_calculation_status and not predominance_calculation_status) 
        ):
            statusCode = 209
        elif not predominance_calculation_status and not diastolic_history_calculation_status:
            statusCode = 400

        return {
            "statusCode": statusCode,
            "headers": {
                "Access-Control-Allow-Headers" : "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": {
                "predominance_calculation": predominance_calculation,
                "diastolic_history_calculation": diastolic_history_calculation 
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Headers" : "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": {
                "predominance_calculation": {
                        "success": False,
                    },
                    "diastolic_history_calculation": {
                        "success": False 
                    } 
            }
        }


