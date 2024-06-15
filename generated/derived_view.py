from dataclasses import dataclass

from generated.derived_view_structure import DerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DerivedView(DerivedViewStructure):
    """
    Abstract derived view of a MANAGED OBJECT for general purpose use.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
