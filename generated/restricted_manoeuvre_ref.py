from dataclasses import dataclass

from generated.restricted_manoeuvre_ref_structure import (
    RestrictedManoeuvreRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RestrictedManoeuvreRef(RestrictedManoeuvreRefStructure):
    """
    Reference to a MEETING RESTRICTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
