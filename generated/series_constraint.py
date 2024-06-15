from dataclasses import dataclass

from generated.series_constraint_version_structure import (
    SeriesConstraintVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraint(SeriesConstraintVersionStructure):
    """
    A particular tariff, described by a combination of parameters.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
