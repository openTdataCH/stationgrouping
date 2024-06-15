from dataclasses import dataclass, field
from typing import Optional, Union

from generated.availability_condition_ref import AvailabilityConditionRef
from generated.day_type_ref import DayTypeRef
from generated.fare_day_type_ref import FareDayTypeRef
from generated.group_of_timebands_ref import GroupOfTimebandsRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.operating_day_ref import OperatingDayRef
from generated.operating_period_ref import OperatingPeriodRef
from generated.validity_condition_ref import ValidityConditionRef
from generated.validity_rule_parameter_ref import ValidityRuleParameterRef
from generated.validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemporalValidityParametersRelStructure(OneToManyRelationshipStructure):
    """
    One to many Relationship for temporal validity parameters.
    """

    class Meta:
        name = "temporalValidityParameters_RelStructure"

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
    group_of_timebands_ref: Optional[GroupOfTimebandsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfTimebandsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_period_ref: Optional[OperatingPeriodRef] = field(
        default=None,
        metadata={
            "name": "OperatingPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            AvailabilityConditionRef,
            ValidityRuleParameterRef,
            ValidityTriggerRef,
            ValidityConditionRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameterRef",
                    "type": ValidityRuleParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTriggerRef",
                    "type": ValidityTriggerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityConditionRef",
                    "type": ValidityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
