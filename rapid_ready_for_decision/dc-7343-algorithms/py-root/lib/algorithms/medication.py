from datetime import datetime

pc_medication_rx = {
    1165953,
    1663183,
    1663184,
    583218,
    1119399,
    1119400,
    1119401,
    1119402,
    1163786,
    1163787,
    1308426,
    1308428,
    1308430,
    1308432,
    1310138,
    1310144,
    1310147,
    1869512,
    1869513,
    1869515,
    1869516,
    1869518,
    1869520,
    2056894,
    2056895,
    2056896,
    2056897,
    845505,
    845506,
    845507,
    845510,
    845511,
    845512,
    845514,
    845515,
    845517,
    845518,
    977426,
    977427,
    977429,
    977430,
    977431,
    977433,
    977434,
    977435,
    977436,
    977437,
    977438,
    977439,
    977440,
    998188,
    998189,
    998190,
    998191,
    1088250,
    1088251,
    1088252,
    1088253,
    1088254,
    1088255,
    1162503,
    1162504,
    477321,
    540423,
    603202,
    603203,
    603205,
    603206,
    603207,
    603208,
    1791700,
    1791702,
    1148918,
    1156710,
    1718998,
    1718999,
    1719000,
    1719002,
    1719003,
    1719004,
    1719005,
    1720960,
    1720975,
    1720977,
    1998781,
    1998782,
    1998783,
    2058857,
    2058858,
    2058860,
    2058861,
    2058863,
    2058866,
    2058867,
    2058880,
    2058881,
    2058882,
    2058883,
    2058890,
    2058891,
    2058892,
    2058893,
    2058894,
    2058895,
    2058912,
    2058918,
    2058927,
    2058928,
    2058933,
    2058934,
    1719769,
    1719772,
    1719774,
    1719777,
    1597583,
    1597584,
    1597585,
    1597586,
    1597587,
    1942480,
    1942481,
    1942482,
    1942483,
    1942484,
    1942485,
    1942486,
    1942487,
    1942488,
    1942489,
    1165372,
    1244550,
    1244551,
    1244552,
    1244553,
    1244555,
    1244556,
    1244558,
    1740892,
    1740893,
    1740894,
    1740897,
    1740898,
    1740899,
    1740900,
    1812477,
    1812478,
    1812480,
    1812481,
    1812482,
    1812483,
    1812484,
    2375816,
    2375817,
    2375818,
    2375820,
    2375821,
    2375823,
    1163532,
    1663180,
    1663181,
    312199,
    316429,
    377111,
    583214,
    1160852,
    1160853,
    1541889,
    1541890,
    1541927,
    1541928,
    616277,
    616278,
    616279,
    616281,
    616282,
    616283,
    616284,
    616285,
    616286,
    616287,
    616288,
    616289,
    616291,
    616292,
    1160121,
    1736775,
    1736776,
    1736781,
    1736783,
    1736784,
    1736785,
    1736786,
    1797528,
    358819,
    1158877,
    1158878,
    200327,
    200328,
    213292,
    213293,
    315557,
    315558,
    368280,
    371250,
    573202,
    573203,
    1152129,
    1736852,
    1736853,
    1736854,
    309311,
    328303,
    376433,
    1001404,
    1001405,
    1001406,
    1093279,
    1093280,
    1101768,
    1101769,
    1101771,
    1101772,
    1101773,
    1111070,
    1111071,
    1111072,
    1111073,
    1160617,
    1860479,
    1860480,
    1860481,
    1860482,
    1860485,
    1860486,
    1860619,
    1861411,
    1918045,
    376888,
    1090557,
    1090558,
    1090559,
    1090560,
    1160449,
    1654342,
    1654344,
    1654357,
    1654359,
    1654361,
    1654363,
    1654365,
    1654367,
    207194,
    207198,
    207200,
    2360541,
    2360542,
    2360543,
    2360545,
    2360546,
    2360548,
    2380608,
    2380609,
    2380610,
    2380611,
    2380613,
    2380614,
    2380617,
    312068,
    312069,
    312070,
    312071,
    314152,
    328441,
    328442,
    328443,
    328444,
    330472,
    373140,
    567985,
    567989,
    567991,
    898589,
    898591,
    898601,
    898603,
    898605,
    898607,
    1162540,
    731119,
    731131,
    749806,
    749809,
    749811,
    749812,
    749813,
    749814,
    749815,
    749816,
    749817,
    749818
}

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
        "success": True
    }

    veterans_medication_list = request_body["medication"]
    date_of_claim = request_body["date_of_claim"]
    date_of_claim_date = datetime.strptime(date_of_claim, "%Y-%m-%d").date()

    vet_is_taking_pc_medication_within_six_months = False
    medication_matches = 0
    for medication in veterans_medication_list:
        if medication["text"].lower() in [x.lower() for x in pc_medications] or \
                medication["code"] in [str(x) for x in pc_medication_rx]:
            medication_date = medication["date"]
            medication_date_formatted = datetime.strptime(medication_date, "%Y-%m-%d").date()
            if (date_of_claim_date - medication_date_formatted).days <= 180:
                vet_is_taking_pc_medication_within_six_months = True
            else:
                continue

    medication_match_calculation["continuous_medication_required"] = vet_is_taking_pc_medication_within_six_months

    return medication_match_calculation

