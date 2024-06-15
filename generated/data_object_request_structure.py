from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_functional_service_request_structure import (
    AbstractFunctionalServiceRequestStructure,
)
from generated.extensions_1 import Extensions1
from generated.network_frame_request_policy_structure import (
    NetworkFrameRequestPolicyStructure,
)
from generated.network_frame_topic import NetworkFrameTopic

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Service Request Type for one or more NeTEx Data Objects,

    :ivar topics: One or more Request filters that specify tthe data to
        be included in output. Multiple filters are logically ANDed.
    :ivar policy: Policies to apply when fetching data specified by
        Topics.
    :ivar extensions:
    """

    topics: "DataObjectRequestStructure.Topics" = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    policy: Optional[NetworkFrameRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "Policy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class Topics:
        network_frame_topic: NetworkFrameTopic = field(
            metadata={
                "name": "NetworkFrameTopic",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
