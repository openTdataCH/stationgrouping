from dataclasses import dataclass

from generated.sales_notice_assignment_version_structure import (
    SalesNoticeAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesNoticeAssignment(SalesNoticeAssignmentVersionStructure):
    """
    The assignment of a NOTICE to a SALES OFFER PACKAGE or a GROUP OF SALES OFFER
    PACKAGEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
