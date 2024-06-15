from dataclasses import dataclass

from generated.responsibility_set_version_structure import (
    ResponsibilitySetVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilitySet(ResponsibilitySetVersionStructure):
    """A set of responsibility roles assignments that can be associated with a DATA
    MANAGED OBJECT.

    A Child ENTITY has the same responsibilities as its parent.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
