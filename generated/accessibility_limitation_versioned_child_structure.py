from dataclasses import dataclass, field
from typing import Optional

from generated.audible_signals_available import AudibleSignalsAvailable
from generated.entity_in_version_structure import VersionedChildStructure
from generated.escalator_free_access import EscalatorFreeAccess
from generated.lift_free_access import LiftFreeAccess
from generated.step_free_access import StepFreeAccess
from generated.visual_signs_available import VisualSignsAvailable
from generated.wheelchair_access import WheelchairAccess

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityLimitationVersionedChildStructure(VersionedChildStructure):
    """
    Type for an ACCESSIBILITY LIMITATION.

    :ivar wheelchair_access:
    :ivar step_free_access:
    :ivar escalator_free_access:
    :ivar lift_free_access:
    :ivar audible_signals_available: Whether a PLACE has audible signals
        for the visually impaired.
    :ivar visual_signs_available: Whether a PLACE has visual signals for
        the hearing impaired.
    """

    class Meta:
        name = "AccessibilityLimitation_VersionedChildStructure"

    wheelchair_access: WheelchairAccess = field(
        metadata={
            "name": "WheelchairAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    step_free_access: Optional[StepFreeAccess] = field(
        default=None,
        metadata={
            "name": "StepFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    escalator_free_access: Optional[EscalatorFreeAccess] = field(
        default=None,
        metadata={
            "name": "EscalatorFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lift_free_access: Optional[LiftFreeAccess] = field(
        default=None,
        metadata={
            "name": "LiftFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audible_signals_available: Optional[AudibleSignalsAvailable] = field(
        default=None,
        metadata={
            "name": "AudibleSignalsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    visual_signs_available: Optional[VisualSignsAvailable] = field(
        default=None,
        metadata={
            "name": "VisualSignsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
