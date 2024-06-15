from dataclasses import dataclass

from generated.data_source_ref_structure import DataSourceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataSourceRef(DataSourceRefStructure):
    """
    Reference  to a DATA SOURCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
