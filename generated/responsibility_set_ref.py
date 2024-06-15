from dataclasses import dataclass

from generated.responsibility_set_ref_structure import (
    ResponsibilitySetRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilitySetRef(ResponsibilitySetRefStructure):
    """Reference to RESPONSIBILITY SET for managing the object.

    If absent, then responsibility is same as for containing context of
    this object.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
