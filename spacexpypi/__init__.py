"""Simple PyPi Wrapper for the SpaceX APIs."""

import logging
import aiohttp
import json

_LOGGER = logging.getLogger("spacex-pypi")

BASE_URL = "https://api.spacexdata.com/v4"

class SpaceX:
    def __init__(self):
        """Initialize the session."""
        self.retry = 5
        self._session = aiohttp.ClientSession()

    async def close(self):
        """Close the session."""
        await self._session.close()

    async def api_request(self, endpoint):
        """Make an api request."""
        response = {}

        url = BASE_URL + str(endpoint)

        async with await self._session.get(url) as resp:
            response = await resp.text()

        if response is not None:
            try:
                return json.loads(response)
            except json.decoder.JSONDecodeError as error:
                raise ValueError("Error decoding SpaceX Data (%s).", error)
            except Exception as error:
                raise ValueError("Unknown error in SpaceX data (%s),", error)
        else:
            raise ConnectionError("Error getting data for: %s", endpoint);

    async def get_roadster_status(self):
        """Get the roadster status."""
        return await self.api_request("/roadster")

    async def get_next_launch(self):
        """Get the next SpaceX Launch details."""
        return await self.api_request("/launches/next")

    async def get_latest_launch(self):
        """Get the latest SpaceX Launch details."""
        return await self.api_request("/launches/latest")

    async def get_upcoming_launches(self):
        """Get all upcoming launches."""
        return await self.api_request("/launches/upcoming")

    async def get_latest_launch(self):
        """Get the latest SpaceX Launch details."""
        return await self.api_request("/launches/latest")

    async def get_launchpads(self):
        """Get all launchpads."""
        return await self.api_request("/launchpads")
