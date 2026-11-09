import aiohttp

from .const import (
    TOKEN_URL,
    USER_URL,
    SMARTHOME_URL,
    CLIENT_ID,
)


class WattsVisionApi:
    def __init__(self, email: str, password: str):
        self._email = email
        self._password = password
        self._token = None

    async def authenticate(self):
        payload = {
            "grant_type": "password",
            "username": self._email,
            "password": self._password,
            "client_id": CLIENT_ID,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(TOKEN_URL, data=payload) as resp:
                resp.raise_for_status()
                data = await resp.json()

        self._token = data["access_token"]
        return self._token

    async def _headers(self):
        if not self._token:
            await self.authenticate()

        return {
            "Authorization": f"Bearer {self._token}"
        }

    async def get_user(self):
        headers = await self._headers()

        async with aiohttp.ClientSession() as session:
            async with session.post(
                USER_URL,
                headers=headers,
            ) as resp:
                resp.raise_for_status()
                return await resp.json()

    async def get_smarthome_id(self):
        user_data = await self.get_user()

        return (
            user_data["data"]["smarthomes"][0]["smarthome_id"]
        )

    async def get_smarthome(self):
        smarthome_id = await self.get_smarthome_id()

        headers = await self._headers()

        payload = {
            "smarthome_id": smarthome_id,
            "lang": "nl_NL",
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                SMARTHOME_URL,
                headers=headers,
                data=payload,
            ) as resp:
                resp.raise_for_status()
                return await resp.json()