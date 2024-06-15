from dataclasses import dataclass

from generated.other_organisation_ref_structure import (
    OtherOrganisationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherOrganisationRef(OtherOrganisationRefStructure):
    """
    Reference to an OTHER ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
