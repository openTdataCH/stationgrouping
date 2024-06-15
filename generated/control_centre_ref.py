from dataclasses import dataclass

from generated.control_centre_ref_structure import ControlCentreRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControlCentreRef(ControlCentreRefStructure):
    """
    Reference to a CONTROL CENTRE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
