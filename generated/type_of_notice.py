from dataclasses import dataclass

from generated.type_of_notice_value_structure import TypeOfNoticeValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfNotice(TypeOfNoticeValueStructure):
    """
    A classification of a NOTICE according to its functional purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
