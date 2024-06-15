from dataclasses import dataclass

from generated.general_organisation_version_structure import (
    GeneralOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralOrganisation(GeneralOrganisationVersionStructure):
    """
    Any type of GENERAL ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
