from dataclasses import dataclass

from generated.organisational_unit_version_structure import (
    OrganisationalUnitVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationalUnit(OrganisationalUnitVersionStructure):
    """
    OrganisationalUnit of an ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
