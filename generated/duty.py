from dataclasses import dataclass

from generated.duty_version_structure import DutyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Duty(DutyVersionStructure):
    """
    The work to be performed by a driver on a particular DAY TYPE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
