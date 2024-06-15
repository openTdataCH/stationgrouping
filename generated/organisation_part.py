from dataclasses import dataclass

from generated.organisation_part_version_structure import (
    OrganisationPartVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationPart(OrganisationPartVersionStructure):
    """
    A named subdivision of an ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
