from dataclasses import dataclass

from generated.log_entry_ref_structure import LogEntryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogEntryRef(LogEntryRefStructure):
    """
    Reference to a LOG ENTRY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
