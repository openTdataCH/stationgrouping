from dataclasses import dataclass, field
from typing import List, Union

from generated.capping_rule_price import CappingRulePrice
from generated.capping_rule_price_ref import CappingRulePriceRef
from generated.controllable_element_price import ControllableElementPrice
from generated.controllable_element_price_ref import (
    ControllableElementPriceRef,
)
from generated.customer_purchase_package_price import (
    CustomerPurchasePackagePrice,
)
from generated.customer_purchase_package_price_ref import (
    CustomerPurchasePackagePriceRef,
)
from generated.distance_matrix_element_price import DistanceMatrixElementPrice
from generated.distance_matrix_element_price_ref import (
    DistanceMatrixElementPriceRef,
)
from generated.fare_price_ref import FarePriceRef
from generated.fare_product_price import FareProductPrice
from generated.fare_product_price_ref import FareProductPriceRef
from generated.fare_structure_element_price import FareStructureElementPrice
from generated.fare_structure_element_price_ref import (
    FareStructureElementPriceRef,
)
from generated.fulfilment_method_price import FulfilmentMethodPrice
from generated.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from generated.geographical_interval_price import GeographicalIntervalPrice
from generated.geographical_interval_price_ref import (
    GeographicalIntervalPriceRef,
)
from generated.geographical_unit_price import GeographicalUnitPrice
from generated.geographical_unit_price_ref import GeographicalUnitPriceRef
from generated.parking_price_ref import ParkingPriceRef
from generated.price_group_ref import PriceGroupRef
from generated.priceable_object_version_structure import (
    ParkingPrice,
    PriceGroup,
)
from generated.quality_structure_factor_price import (
    QualityStructureFactorPrice,
)
from generated.quality_structure_factor_price_ref import (
    QualityStructureFactorPriceRef,
)
from generated.sales_offer_package_price import SalesOfferPackagePrice
from generated.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from generated.series_constraint_price import SeriesConstraintPrice
from generated.series_constraint_price_ref import SeriesConstraintPriceRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.time_interval_price import TimeIntervalPrice
from generated.time_interval_price_ref import TimeIntervalPriceRef
from generated.time_unit_price import TimeUnitPrice
from generated.time_unit_price_ref import TimeUnitPriceRef
from generated.usage_parameter_price import UsageParameterPrice
from generated.usage_parameter_price_ref import UsageParameterPriceRef
from generated.validable_element_price import ValidableElementPrice
from generated.validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompositePricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE PRICEs.
    """

    class Meta:
        name = "compositePrices_RelStructure"

    choice: List[
        Union[
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            UsageParameterPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            SeriesConstraintPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            FarePriceRef,
            PriceGroupRef,
            CustomerPurchasePackagePrice,
            ParkingPrice,
            SalesOfferPackagePrice,
            FulfilmentMethodPrice,
            CappingRulePrice,
            FareProductPrice,
            FareStructureElementPrice,
            TimeIntervalPrice,
            TimeUnitPrice,
            QualityStructureFactorPrice,
            ControllableElementPrice,
            ValidableElementPrice,
            UsageParameterPrice,
            DistanceMatrixElementPrice,
            GeographicalIntervalPrice,
            GeographicalUnitPrice,
            SeriesConstraintPrice,
            PriceGroup,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroupRef",
                    "type": PriceGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": ParkingPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": GeographicalUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroup",
                    "type": PriceGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
