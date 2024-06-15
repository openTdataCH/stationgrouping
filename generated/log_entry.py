from dataclasses import dataclass

from generated.log_entry_version_structure import LogEntryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogEntry(LogEntryVersionStructure):
    """
    A time-stamped record of an event or change of state.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
