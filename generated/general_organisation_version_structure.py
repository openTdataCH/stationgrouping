from dataclasses import dataclass

from generated.other_organisation_version_structure import (
    OtherOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralOrganisationVersionStructure(OtherOrganisationVersionStructure):
    """
    Type for an GENERAL ORGANISATION.
    """

    class Meta:
        name = "GeneralOrganisation_VersionStructure"
