from dataclasses import dataclass

from generated.organisation_part_ref_structure import (
    OrganisationPartRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControlCentreRefStructure(OrganisationPartRefStructure):
    """
    Type for a reference to a CONTROL CENTRE.
    """