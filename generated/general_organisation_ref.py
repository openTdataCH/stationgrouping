from dataclasses import dataclass

from generated.general_organisation_ref_structure import (
    GeneralOrganisationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralOrganisationRef(GeneralOrganisationRefStructure):
    """
    Reference to a GENERAL ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
