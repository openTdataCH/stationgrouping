from dataclasses import dataclass

from generated.minimum_stay_version_structure import (
    MinimumStayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MinimumStay(MinimumStayVersionStructure):
    """
    Details of any minimum stay at the destination  required  to use the product.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
