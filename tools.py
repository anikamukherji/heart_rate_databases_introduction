def valid_units(unit):
    """
    Checks if given unit is supported
    :param unit: age unit
    :type unit: string

    :return: whether given unit of time is supported
    :rtype: boolean
    """
    supported_units = ["day", "week", "month", "year"]
    return unit in supported_units
