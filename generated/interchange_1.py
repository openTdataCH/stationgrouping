from dataclasses import dataclass

from generated.interchange_version_structure import InterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Interchange1(InterchangeVersionStructure):
    """
    The scheduled possibility for transfer of passengers between two SERVICE
    JOURNEYs at the same or different STOP POINTs.
    """

    class Meta:
        name = "Interchange"
        namespace = "http://www.netex.org.uk/netex"
