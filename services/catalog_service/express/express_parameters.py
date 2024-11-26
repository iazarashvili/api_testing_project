from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class ExpressParameter:
    Longitude: Optional[float] = None
    Latitude: Optional[float] = None

    @staticmethod
    def get_dark_store_params(longitude: float, latitude: float):
        params = ExpressParameter(
            Longitude=longitude,
            Latitude=latitude
        )
        return asdict(params)
