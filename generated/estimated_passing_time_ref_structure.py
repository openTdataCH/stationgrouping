from dataclasses import dataclass

from generated.passing_time_ref_structure import PassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimeRefStructure(PassingTimeRefStructure):
    """
    Type for a reference to an ESTIMATED PASSING TIME.
    """
