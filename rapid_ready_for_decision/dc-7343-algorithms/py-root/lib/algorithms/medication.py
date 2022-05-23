from datetime import datetime


pc_medications = {
    "Gemcitabine",
    "5-fluorouracil",
    "Irinotecan",
    "Oxaliplatin",
    "Albumin-bound paclitaxel",
    "Capecitabine",
    "Cisplatin",
    "Paclitaxel",
    "Docetaxel",
    "Irinotecan liposome",
    "Sunitinib",
    "Everolimus",
    "Octreotide",
    "Lanreotide",
}


def medication_match(request_body):
    """
    Determine if there is the veteran requires continuous medication for pancreatic cancer

    :param request_body: request body
    :type request_body: dict
    :return: response body indicating success or failure with additional attributes
    :rtype: dict
    """

    medication_match_calculation = {
        "success": True,
        "continuous_medication_required": False
    }

    date_of_claim = request_body["date_of_claim"]
    date_of_claim_date = datetime.strptime(date_of_claim, "%Y-%m-%d").date()

    for medication in request_body["medication"]:

        if medication["text"].lower() in [x.lower() for x in pc_medications]:
            if medication["status"].lower() != "active":
                medication_date = medication["authored_on"]
                medication_date_formatted = datetime.strptime(medication_date, "%Y-%m-%d").date()
                if (date_of_claim_date - medication_date_formatted).days <= 180:
                    medication_match_calculation["continuous_medication_required"] = True
            else:
                medication_match_calculation["continuous_medication_required"] = True

    return medication_match_calculation

