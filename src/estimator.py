def estimator(data):
    numberOfDays = data["timeToElapse"]
    durationType = data["periodType"]
    reportedCases = data["reportedCases"]
    hospitalBeds = data["totalHospitalBeds"]

    def daysConverter(number, durationType):
        if data["periodType"] == 'days':
            days = data["timeToElapse"]
        elif data["periodType"] == 'weeks':
            days = ((data["timeToElapse"]) * 7)
        else:
            days = ((data["timeToElapse"]) * 30)

        return days

    def impactAssess(reportedCases, numberOfDays, hospitalBeds):
        hospitalBeds = hospitalBeds * .35
        impact = reportedCases * 10
        severeImpact = reportedCases * 50
        
        impactTime = impact * ( 2 ** (numberOfDays//3))
        impactTimeSevere = severeImpact * ( 2 ** (numberOfDays//3))

        severeCasesByRequestedTime = int(impactTime *15/100)
        severeSevereCasesByRequestedTime = int(impactTimeSevere *15/100)

        hospitalBedsLeft = ( data["totalHospitalBeds"] * .35 ) - severeCasesByRequestedTime
        severeHospitalBedsLeft = ( data["totalHospitalBeds"] * .35 ) - severeSevereCasesByRequestedTime
        hospitalBedsLeft = int(hospitalBedsLeft)
        severeHospitalBedsLeft = int(severeHospitalBedsLeft)

        return impact, severeImpact, impactTime, impactTimeSevere, severeCasesByRequestedTime, severeSevereCasesByRequestedTime, hospitalBedsLeft, severeHospitalBedsLeft

    numberOfDays = daysConverter(numberOfDays, durationType)
    currentlyInfected, severeCurrentlyInfected, requestedTime, requestedTimeSevere, severeCasesByRequestedTime, severeSevereCasesByRequestedTime, hospitalBedsLeft, severeHospitalBedsLeft = impactAssess(reportedCases, numberOfDays, hospitalBeds)

    data = {}
    dataAndela = data

    impact = {
        "currentlyInfected": currentlyInfected,
        "infectionsByRequestedTime": requestedTime,
        "severeCasesByRequestedTime": severeCasesByRequestedTime,
        "hospitalBedsByRequestedTime": hospitalBedsLeft
    }

    severeImpact = {
        "currentlyInfected": severeCurrentlyInfected,
        "infectionsByRequestedTime": requestedTimeSevere,
        "severeCasesByRequestedTime": severeSevereCasesByRequestedTime,
        "hospitalBedsByRequestedTime": severeHospitalBedsLeft
    }

    data["data"] = dataAndela
    data["impact"] = impact
    data["severeImpact"] = severeImpact

    return data
