from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN


class WattsvisionFlowHandler(config_entries.ConfigFlow):
    VERSION = 1
    DOMAIN = DOMAIN

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["email"],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("email"): str,
                    vol.Required("password"): str,
                }
            ),
        )
