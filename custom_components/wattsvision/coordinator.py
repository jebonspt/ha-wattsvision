import logging

from datetime import timedelta

from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)

from .api import WattsVisionApi

_LOGGER = logging.getLogger(__name__)


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

        super().__init__(
            hass,
            _LOGGER,
            name="Watts Vision",
            update_interval=timedelta(minutes=2),
        )

    async def _async_update_data(self):
        data = await self.api.get_smarthome()

        _LOGGER.warning(
            "WATTS DATA: %s",
            data,
        )

        return data