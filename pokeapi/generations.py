import aiohttp

class Generation:
    def __init__(self , raw_gen_data )->None:
        self.data = raw_gen_data

    @property
    def raw(self):
        return self.data

    @property
    def abilities(self):
        return self.data['abilities']


