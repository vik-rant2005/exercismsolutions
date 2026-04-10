"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?
    """
    return (
        temperature < 800 and
        neutrons_emitted > 500 and
        temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power for 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', 'black').
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold value.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').
    """
    value = temperature * neutrons_produced_per_second

    if value < 0.9 * threshold:
        return "LOW"
    elif value <= 1.1 * threshold:
        return "NORMAL"
    else:
        return "DANGER"
