from dataclasses import dataclass, field

from generated.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class CodeWithAuthorityType(CodeType):
    """
    Gml:CodeWithAuthorityType requires that the codeSpace attribute is provided in
    an instance.
    """

    code_space: str = field(
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        }
    )
