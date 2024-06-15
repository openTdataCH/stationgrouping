from dataclasses import dataclass

from generated.rounding_versioned_structure import RoundingVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Rounding(RoundingVersionedStructure):
    """
    Parameters describing how the results of calculations are to be rounded to the
    nearest quantum.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
