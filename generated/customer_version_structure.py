from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from generated.customer_accounts_rel_structure import (
    CustomerAccountsRelStructure,
)
from generated.customer_eligibilities_rel_structure import (
    CustomerEligibilitiesRelStructure,
)
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.fare_contracts_rel_structure import FareContractsRelStructure
from generated.gender_enumeration import GenderEnumeration
from generated.postal_address import PostalAddress
from generated.private_code_structure import PrivateCodeStructure
from generated.telephone_contact_structure import TelephoneContactStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerVersionStructure(DataManagedObjectStructure):
    """
    Type for CUSTOMER.

    :ivar surname: Curname of CUSTOMER.
    :ivar first_name: First name of CUSTOMER.
    :ivar title: Title  of CUSTOMER.
    :ivar date_of_birth: Date of birth of  CUSTOMER.
    :ivar gender: Genfer of CUSTOMER.
    :ivar height: Height of CUSTOMER.
    :ivar photo: Photo of CUSTOMER.
    :ivar email: Email address of CUSTOMER. +v1.1
    :ivar phone:
    :ivar postal_address:
    :ivar identity_document_ref: Identifier of Identity document of
        CUSTOMER.
    :ivar customer_eligibilities: Eligibilities  for CUSTOMER.
    :ivar customer_accounts: CUSTOMER ACCOUNTs belonging to customer.
    :ivar fare_contracts: FARE CONTRACTs belonging to customer.
    """

    class Meta:
        name = "Customer_VersionStructure"

    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    date_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfBirth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender: Optional[GenderEnumeration] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    photo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Photo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    phone: Optional[TelephoneContactStructure] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    identity_document_ref: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "IdentityDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_eligibilities: Optional[CustomerEligibilitiesRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "customerEligibilities",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    customer_accounts: Optional[CustomerAccountsRelStructure] = field(
        default=None,
        metadata={
            "name": "customerAccounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contracts: Optional[FareContractsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareContracts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
