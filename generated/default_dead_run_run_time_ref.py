from dataclasses import dataclass

from generated.default_dead_run_run_time_ref_structure import (
    DefaultDeadRunRunTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultDeadRunRunTimeRef(DefaultDeadRunRunTimeRefStructure):
    """
    Reference to a DEFAULT DEAD RUN RUN TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
