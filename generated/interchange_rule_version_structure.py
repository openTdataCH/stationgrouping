from dataclasses import dataclass, field
from typing import Optional

from generated.control_centre_ref import ControlCentreRef
from generated.interchange_rule_parameter_structure import (
    InterchangeRuleParameterStructure,
)
from generated.interchange_rule_timings_rel_structure import (
    InterchangeRuleTimingsRelStructure,
)
from generated.interchange_version_structure import InterchangeVersionStructure
from generated.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleVersionStructure(InterchangeVersionStructure):
    """
    Type for INTERCHANGE RULE.

    :ivar connection_zone_ref: Reference to a CONNEXTION ZONE area.
    :ivar control_centre_ref:
    :ivar exclude: Whether rule is to exclude any connections that
        satisfy the criteria. Default is false.
    :ivar timings: Additional timings for  the INTERCHANGE RULE for
        specific TIME DEMAND TYPEs.
    :ivar feeder_filter: Feeder end of INTERCHANGE RULE.
    :ivar distributor_filter: Distributor end of INTERCHANGE RULE.
    """

    class Meta:
        name = "InterchangeRule_VersionStructure"

    connection_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ConnectionZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    control_centre_ref: Optional[ControlCentreRef] = field(
        default=None,
        metadata={
            "name": "ControlCentreRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timings: Optional[InterchangeRuleTimingsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    feeder_filter: Optional[InterchangeRuleParameterStructure] = field(
        default=None,
        metadata={
            "name": "FeederFilter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distributor_filter: Optional[InterchangeRuleParameterStructure] = field(
        default=None,
        metadata={
            "name": "DistributorFilter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
