from dataclasses import dataclass

from generated.type_of_organisation_ref_structure import (
    TypeOfOrganisationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfOrganisationRef(TypeOfOrganisationRefStructure):
    """
    Reference to a TYPE OF ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
