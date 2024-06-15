from dataclasses import dataclass

from generated.interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyInterchangeRefStructure(InterchangeRefStructure):
    """
    Type for a reference to a SERVICE JOURNEY INTERCHANGE.
    """
