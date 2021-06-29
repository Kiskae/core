from homeassistant import config_entries
from homeassistant.components.upc_connect.const import DOMAIN
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import RESULT_TYPE_ABORT

from .legacy import (
    PLATFORM_SCHEMA as LEGACY_PLATFORM_SCHEMA,
    async_get_scanner as legacy_async_get_scanner,
    parse_config,
)

PLATFORM_SCHEMA = LEGACY_PLATFORM_SCHEMA


async def async_get_scanner(hass: HomeAssistant, config):
    """compat with legacy device_tracker configuration."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_IMPORT},
        data=parse_config(config),
    )
    if result["type"] == RESULT_TYPE_ABORT and result["reason"] == "already_configured":
        # TODO: persistent notification to remove old configuration
        pass

    return await legacy_async_get_scanner(hass, config)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:
    pass
