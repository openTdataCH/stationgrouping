from dataclasses import dataclass, field
from typing import Optional

from generated.alternative_names_rel_structure import (
    AlternativeNamesRelStructure,
)
from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfConcessionVersionStructure(TypeOfValueVersionStructure):
    """
    Type for TYPE OF CONCESSION.

    :ivar alternative_names: Alternative names for value.
    """

    class Meta:
        name = "TypeOfConcession_VersionStructure"

    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
