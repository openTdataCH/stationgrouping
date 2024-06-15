from dataclasses import dataclass

from generated.dead_run_with_calls_version_structure import (
    DeadRunWithCallsVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRun(DeadRunWithCallsVersionStructure):
    """
    A non-service VEHICLE JOURNEY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
