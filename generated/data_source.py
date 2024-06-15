from dataclasses import dataclass

from generated.data_source_version_structure import DataSourceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataSource(DataSourceVersionStructure):
    """Identifies the system which has produced the data.

    References to a DATA SOURCE are useful in an interoperated computer
    system.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
