from dataclasses import dataclass

from generated.duty_ref_structure import DutyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DutyRef(DutyRefStructure):
    """
    Reference to a DUTY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
