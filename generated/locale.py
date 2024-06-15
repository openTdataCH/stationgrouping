from dataclasses import dataclass

from generated.locale_structure import LocaleStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Locale(LocaleStructure):
    """
    Common LOCALE dependent properties.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
