import requests
import asyncio
import logging

log = logging.getLogger(__name__)


class ProteinApi:
    """
    A class to represent API for Protein data bank
    """
    data = []

    def __init__(self,  timeout=1):
        self.timeout = timeout

    async def get_data(self, url):
        """Returns data requested by url"""
        if not url:
            log.debug('Provided url is wrong')
            return None
        try:
            response = requests.get(url)
            log.debug(f'Requesting data for {url}')
            await asyncio.sleep(self.timeout)
            return response.json()
        except Exception as error:
            log.error(f'Error occurred while requesting data for {url}: {error}')
            raise

    def get_data_in_loop(self, urls):
        """Performs parallel requests to urls provided in arguments"""
        log.debug(f'Start requesting set of data')
        loop = asyncio.get_event_loop()
        tasks = [self.get_data(url) for url in urls]
        responses = loop.run_until_complete(asyncio.gather(*tasks))
        for response in responses:
            self.data.append(response)
        loop.close()
