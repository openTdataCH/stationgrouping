from dataclasses import dataclass

from generated.general_frame_member_structure import (
    GeneralFrameMemberStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralFrameMember(GeneralFrameMemberStructure):
    """
    An association of an ENTITY in a GENERAL FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
