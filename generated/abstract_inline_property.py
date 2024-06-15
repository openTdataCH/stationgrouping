from dataclasses import dataclass

from generated.inline_property_type import InlinePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractInlineProperty(InlinePropertyType):
    """
    Gml:abstractInlineProperty may be used as the head of a subtitution group of
    more specific elements providing a value inline.
    """

    class Meta:
        name = "abstractInlineProperty"
        namespace = "http://www.opengis.net/gml/3.2"
