"""Support for UPC ConnectBox router."""
import voluptuous as vol

from homeassistant.components.device_tracker import (
    DOMAIN,
    PLATFORM_SCHEMA as PARENT_PLATFORM_SCHEMA,
    DeviceScanner,
)
from homeassistant.const import CONF_HOST, CONF_PASSWORD
import homeassistant.helpers.config_validation as cv

DEFAULT_IP = "192.168.0.1"

PLATFORM_SCHEMA = PARENT_PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Optional(CONF_HOST, default=DEFAULT_IP): cv.string,
    }
)


def parse_config(config) -> dict:
    return PLATFORM_SCHEMA(config[DOMAIN])


async def async_get_scanner(hass, config):
    """Return the UPC device scanner."""
    return StubScanner()


class StubScanner(DeviceScanner):
    async def async_scan_devices(self) -> list[str]:
        return []
