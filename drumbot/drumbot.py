"""
Asyncio Drumbot API implementation for Python
"""

import aiohttp


class Drumbot:
    def __init__(self,
                 session=aiohttp.ClientSession()):
        self.session = session
        self.patterns = 'https://api.noopschallenge.com/drumbot/patterns'

    async def get_all_patterns(self):
        async with self.session.get(self.patterns) as p:
            return p.json()
    
    async def get_pattern(self, pattern):
        def make_url(pattern):
            return f'{self.patterns}/{pattern}'
        async with self.session.get(make_url(pattern)) as p:
            return p.json()
