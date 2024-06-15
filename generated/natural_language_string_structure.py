from dataclasses import dataclass, field
from typing import Optional

from generated.lang_value import LangValue

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NaturalLanguageStringStructure:
    """
    Tyoe for a string in a specified language.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    lang: Optional[LangValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
