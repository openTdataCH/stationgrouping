from dataclasses import dataclass

from generated.frequency_of_use_version_structure import (
    FrequencyOfUseVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FrequencyOfUse(FrequencyOfUseVersionStructure):
    """The limits of usage frequency for a FARE PRODUCT (or one of its components)
    or a SALES OFFER PACKAGE during a specific VALIDITY PERIOD.

    There may be different tariffs depending on how often the right is
    consumed during the period.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
