from dataclasses import dataclass

from generated.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractGeometricPrimitive(AbstractGeometricPrimitiveType):
    """
    The AbstractGeometricPrimitive element is the abstract head of the substitution
    group for all (pre- and user-defined) geometric primitives.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
