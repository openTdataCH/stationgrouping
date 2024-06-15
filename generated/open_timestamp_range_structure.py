from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OpenTimestampRangeStructure:
    """Data Type for a range of date times.

    Start time must be specified, end time is optional.

    :ivar start_time: The (inclusive) start time stamp.
    :ivar end_time: The (inclusive) end time stamp. If omitted, the
        range end is open-ended; that is, it should be interpreted as
        "forever".
    """

    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
