from dataclasses import dataclass, field
from typing import Optional

from generated.country_ref import CountryRef
from generated.organisation_version_structure import (
    OrganisationVersionStructure,
)
from generated.postal_address_version_structure import (
    PostalAddressVersionStructure,
)
from generated.type_of_organisation_refs_rel_structure import (
    TypeOfOrganisationRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AuthorityVersionStructure(OrganisationVersionStructure):
    """
    Type for an AUTHORITY.

    :ivar country_ref:
    :ivar address: Address of AUTHORITY.
    :ivar authority_types: Classification of Zone. Used for arbitrary
        documentation -.
    """

    class Meta:
        name = "Authority_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    address: Optional[PostalAddressVersionStructure] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    authority_types: Optional[TypeOfOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "authorityTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
