from dataclasses import dataclass

from generated.entity_structure import EntityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Entity(EntityStructure):
    """Any data instance to be managed in an operational Version Management System.

    When several DATA SOURCEs coexist (multimodality and/or
    interoperability), an ENTITY has to be related to a given DATA
    SYSTEM in which it is defined.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
