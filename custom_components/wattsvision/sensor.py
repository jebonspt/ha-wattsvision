from homeassistant.components.sensor import SensorEntity


async def async_setup_entry(
    hass,
    entry,
    async_add_entities,
):
    async_add_entities(
        [
            WattsVisionStatusSensor()
        ]
    )


class WattsVisionStatusSensor(
    SensorEntity
):
    _attr_name = "Watts Vision Status"
    _attr_unique_id = "wattsvision_status"

    @property
    def native_value(self):
        return "Integration Loaded"