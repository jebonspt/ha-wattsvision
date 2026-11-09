from datetime import timedelta

from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)

from .api import WattsVisionApi


class WattsVisionCoordinator(DataUpdateCoordinator):
    def __init__(
        self,
        hass,
        email,
        password,
    ):
        self.api = WattsVisionApi(
            email,
            password,
        )

import logging

from datetime import timedelta

from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)

from .api import WattsVisionApi

_LOGGER = logging.getLogger(__name__)

super().__init__(
    hass,
    _LOGGER,
    name="Watts Vision",
    update_interval=timedelta(minutes=2),
)
