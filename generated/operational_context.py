from dataclasses import dataclass

from generated.operational_context_version_structure import (
    OperationalContextVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperationalContext(OperationalContextVersionStructure):
    """
    Characterization of a set of operational objects, such as timing or links
    determined either by a DEPARTMENT or by an ORGANISATIONAL UNIT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
