from dataclasses import dataclass, field
from typing import Optional

from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.multilingual_string import MultilingualString
from generated.types_of_value_structure import TypesOfValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValueSetVersionStructure(DataManagedObjectStructure):
    """Type for a VALUE SET.

    Abstract supertype  used to define open  classifications of  value
    types.

    :ivar name: Name of Value.
    :ivar values: Values in Set.
    :ivar class_of_values: Name of Class of Values in Set.
    """

    class Meta:
        name = "ValueSet_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    values: Optional[TypesOfValueStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_values: Optional[str] = field(
        default=None,
        metadata={
            "name": "classOfValues",
            "type": "Attribute",
        },
    )
