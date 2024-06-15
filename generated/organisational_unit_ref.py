from dataclasses import dataclass

from generated.organisational_unit_ref_structure import (
    OrganisationalUnitRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationalUnitRef(OrganisationalUnitRefStructure):
    """
    Reference to a ORGANISATIONAL UNIT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
