from datetime import datetime

snomed_cancer = {187791002,
                 187792009,
                 254611009,
                 255088001,
                 363418001,
                 363419009,
                 372003004,
                 700423003,
                 94459006,
                 1651000119109,
                 187793004,
                 372119009,
                 372142002,
                 735735001,
                 93715005,
                 93843007,
                 93939009,
                 94082003,
                 94460001,
                 363417006,
                 371967001
                 }


def active_cancer_condition(request_body):
    """
    Determine if there is an active pancreatic cancer diagnosis

    :param request_body: request body
    :type request_body: dict
    :return: response body indicating success or failure with additional attributes
    :rtype: dict
    """

    active_cancer_result = {"success": True, "active_cancer_present": False}

    for condition in request_body["condition"]:
        condition_date = datetime.strptime(condition["onset_date"], "%Y-%m-%d").date()
        if int(condition["code"]) in snomed_cancer:
            active_cancer_result["active_cancer_present"] = True

    return active_cancer_result