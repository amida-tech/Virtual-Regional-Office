from datetime import datetime

pc_procedure_cpt = {
    "1007926",
    "48153",
    "48154",
    "48140",
    "1007923",
    "48152",
    "00794",
    "48150",
    "1007918",
    "48146",
    "48155",
    "48160",
    "1010904",
    "1010905",
    "77014",
    "4164F",
    "32701",
    "77399",
    "01922",
    "77469",
    "1010921",
    "1010843",
    "1010919",
    "77799",
    "77789",
    "77750",
    "1010895",
    "77423",
    "1015093",
    "1015092",
    "1014921",
    "77372",
    "77371",
    "77373",
    "77295",
    "77301",
    "77386",
    "77385",
    "1022243",
    "4165F",
    "77338",
}


def procedure_match(request_body):
    """
    Determine if there is the veteran requires continuous medication for pancreatic cancer

    :param request_body: request body
    :type request_body: dict
    :return: response body indicating success or failure with additional attributes
    :rtype: dict
    """
    procedure_match_calculation = {
        "success": True,
        "procedure_within_six_months": False
    }

    date_of_claim = request_body["date_of_claim"]
    date_of_claim_datetime = datetime.strptime(date_of_claim, "%Y-%m-%d").date()

    for procedure in request_body["procedure"]:
        code = request_body["code"]
        status = procedure["status"].lower()
        if code in pc_procedure_cpt and status == "active":
            procedure_match_calculation["procedure_within_six_months"] = True
        elif code in pc_procedure_cpt and status != "active":
            procedure_date = procedure["performed_date"]
            procedure_date_formatted = datetime.strptime(procedure_date, "%Y-%m-%d").date()
            if (date_of_claim_datetime - procedure_date_formatted).days <= 180:
                procedure_match_calculation["procedure_within_six_months"] = True

    return procedure_match_calculation
