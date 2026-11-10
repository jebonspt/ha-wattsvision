from homeassistant import config_entries


class ConfigFlow(config_entries.ConfigFlow):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        return self.async_abort(reason="not_implemented")
