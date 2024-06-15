from dataclasses import dataclass

from generated.level_ref_structure import LevelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelRef(LevelRefStructure):
    """
    Reference to LEVEL of a SITE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
