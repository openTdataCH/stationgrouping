from dataclasses import dataclass

from generated.type_of_organisation_part_ref_structure import (
    TypeOfOrganisationPartRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfOrganisationPartRef(TypeOfOrganisationPartRefStructure):
    """
    Reference to a TYPE OF ORGANISATION PART.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
