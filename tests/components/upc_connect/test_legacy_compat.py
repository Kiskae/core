from unittest.mock import patch

from homeassistant.components.device_tracker import DOMAIN
from homeassistant.components.upc_connect.const import DOMAIN as CONFIG_FLOW_DOMAIN
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_PLATFORM
from homeassistant.core import HomeAssistant
from homeassistant.setup import async_setup_component

CONNECTBOX_PLATFORM = {
    DOMAIN: {
        CONF_PLATFORM: "upc_connect",
        CONF_PASSWORD: "12345678",
        CONF_HOST: "192.0.2.1",
    }
}


async def test_legacy_definition(hass: HomeAssistant):
    with patch.object(hass.config_entries.flow, "async_init") as mock_flow_init:
        await async_setup_component(hass, DOMAIN, CONNECTBOX_PLATFORM)
        # flow was started to import old config
        mock_flow_init.assert_called_once()
        mock_flow_init.call_args[0] == CONFIG_FLOW_DOMAIN
