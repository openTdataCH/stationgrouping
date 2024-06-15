from dataclasses import dataclass

from generated.notice_ref_structure import NoticeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeRef(NoticeRefStructure):
    """
    Reference to a NOTICE i.e. footnote, note,  announcement or other informational
    text element.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
