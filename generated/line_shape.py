from dataclasses import dataclass

from generated.line_shape_structure_2 import LineShapeStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineShape(LineShapeStructure2):
    """
    The graphical shape of a LINK obtained from a formula or other means, using the
    LOCATION of its limiting POINTs and depending on the LOCATING SYSTEM used for
    the graphical representation.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
