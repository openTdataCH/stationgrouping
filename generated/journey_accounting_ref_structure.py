from dataclasses import dataclass

from generated.assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyAccountingRefStructure(AssignmentRefStructure):
    """
    Type for a reference to a JOURNEY ACCOUNTING.
    """
