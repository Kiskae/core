from homeassistant import config_entries

from .const import DOMAIN


class ConnectBoxConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, info):
        return self.async_abort(reason="not_implemented")

    async def async_step_ssdp(self, discovery_info):
        return self.async_abort(reason="not_implemented")

    async def async_step_import(self, discovery_info):
        return self.async_abort(reason="not_implemented")

    async def _async_step_probe_host(self):
        return self.async_abort(reason="not_implemented")
