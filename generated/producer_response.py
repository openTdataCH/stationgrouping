from dataclasses import dataclass

from generated.producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProducerResponse(ProducerResponseStructure):
    """
    Subsititutable type for a SIRI r Producer esponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
