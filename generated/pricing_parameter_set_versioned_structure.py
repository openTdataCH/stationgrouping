from dataclasses import dataclass, field
from typing import Optional, Union

from generated.day_type_ref import DayTypeRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.fare_day_type_ref import FareDayTypeRef
from generated.month_validity_offsets_rel_structure import (
    MonthValidityOffsetsRelStructure,
)
from generated.multilingual_string import MultilingualString
from generated.price_unit_ref import PriceUnitRef
from generated.price_units_rel_structure import PriceUnitsRelStructure
from generated.pricing_rules_rel_structure import PricingRulesRelStructure
from generated.pricing_services_rel_structure import (
    PricingServicesRelStructure,
)
from generated.rounding_ref import RoundingRef
from generated.roundings_rel_structure import RoundingsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingParameterSetVersionedStructure(DataManagedObjectStructure):
    """
    Type for PRICING PARAMETERS.

    :ivar name: Name of PRICING PARAMETERS parameter set.
    :ivar price_unit_ref:
    :ivar price_units: Set of Rounding paraemeters.
    :ivar pricing_rules: Table of Month Validty offsets for each month.
    :ivar allow_cumulative_discounts: Whether cumulative discounts are
        allowed.
    :ivar rounding_ref:
    :ivar roundings: Set of Rounding paraemeters.
    :ivar fare_day_type_ref_or_day_type_ref:
    :ivar month_validity_offsets: Table of Month Validty offsets for
        each month.
    :ivar pricing_services:
    """

    class Meta:
        name = "PricingParameterSet_VersionedStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_units: Optional[PriceUnitsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_rules: Optional[PricingRulesRelStructure] = field(
        default=None,
        metadata={
            "name": "pricingRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allow_cumulative_discounts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowCumulativeDiscounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    roundings: Optional[RoundingsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_day_type_ref_or_day_type_ref: Optional[
        Union[FareDayTypeRef, DayTypeRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    month_validity_offsets: Optional[MonthValidityOffsetsRelStructure] = field(
        default=None,
        metadata={
            "name": "monthValidityOffsets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_services: Optional[PricingServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "pricingServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
