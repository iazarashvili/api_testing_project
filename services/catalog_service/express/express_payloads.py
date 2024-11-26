from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class ExpressPayloads:
    correlationId: Optional[str] = None

    @staticmethod
    def post_express(correlation_id):
        payloads = ExpressPayloads(
            correlationId=correlation_id
        )
        return asdict(payloads)
