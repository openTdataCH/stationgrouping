from dataclasses import dataclass

from generated.trace_structure import TraceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Trace(TraceStructure):
    """A  record of the detailed changes of a given ENTITY IN VERSION from one
    VERSION to the next one.

    A TRACE contains pairs of attributes' old values - new values.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
