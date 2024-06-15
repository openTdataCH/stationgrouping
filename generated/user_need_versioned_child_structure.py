from dataclasses import dataclass, field
from typing import Optional, Union

from generated.encumbrance_enumeration import EncumbranceEnumeration
from generated.entity_in_version_structure import VersionedChildStructure
from generated.medical_need_enumeration import MedicalNeedEnumeration
from generated.mobility_enumeration import MobilityEnumeration
from generated.pyschosensory_need_enumeration import (
    PyschosensoryNeedEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserNeedVersionedChildStructure(VersionedChildStructure):
    """
    Type for of a USER NEED.

    :ivar choice:
    :ivar excluded: Whether user need is included or excluded. Default
        is included.
    :ivar need_ranking: Relative ranking of need on a scale 1-5
    """

    class Meta:
        name = "UserNeed_VersionedChildStructure"

    choice: Optional[
        Union[
            MobilityEnumeration,
            PyschosensoryNeedEnumeration,
            MedicalNeedEnumeration,
            EncumbranceEnumeration,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityNeed",
                    "type": MobilityEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PsychosensoryNeed",
                    "type": PyschosensoryNeedEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MedicalNeed",
                    "type": MedicalNeedEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EncumbranceNeed",
                    "type": EncumbranceEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    excluded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Excluded",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    need_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "NeedRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
