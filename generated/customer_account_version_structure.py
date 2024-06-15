from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from generated.account_status_type_enumeration import (
    AccountStatusTypeEnumeration,
)
from generated.customer_account_status_ref import CustomerAccountStatusRef
from generated.customer_purchase_package_refs_rel_structure import (
    CustomerPurchasePackageRefsRelStructure,
)
from generated.customer_ref import CustomerRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.fare_contracts_rel_structure import FareContractsRelStructure
from generated.multilingual_string import MultilingualString
from generated.type_of_customer_account_ref import TypeOfCustomerAccountRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountVersionStructure(DataManagedObjectStructure):
    """
    Type for CUSTOMER ACCOUNT.

    :ivar name: Name of CUSTOMER ACCOUNT.
    :ivar description: Description of CUSTOMER ACCOUNT.
    :ivar start_date: Start Date of CUSTOMER ACCOUNT.
    :ivar end_date: End Date of CUSTOMER ACCOUNT.
    :ivar customer_ref:
    :ivar type_of_customer_account_ref:
    :ivar customer_account_status_ref:
    :ivar customer_account_status_type: Standard values for account
        status. +v1.1
    :ivar fare_contracts: FARE CONTRACTs for CUSTOMER ACCOUNT +v1.1.
    :ivar customer_purchase_packages: CUSTOMER PURCHASE PACKAGES  for
        CUSTOMER ACCOUT.
    """

    class Meta:
        name = "CustomerAccount_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_customer_account_ref: Optional[TypeOfCustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_status_ref: Optional[CustomerAccountStatusRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_status_type: Optional[AccountStatusTypeEnumeration] = (
        field(
            default=None,
            metadata={
                "name": "CustomerAccountStatusType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    fare_contracts: Optional[FareContractsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareContracts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_packages: Optional[
        CustomerPurchasePackageRefsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
