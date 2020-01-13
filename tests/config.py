class Config:
    def __init__(self, env):
        # SUPPORT_ENV = ['dev', 'qa']

        # if env.lower( ) not in SUPPORT_ENV:
        #     raise Exception('Not supported env')
        self.base_url = {
            'dev': 'https://www.imdb.com',
            'qa': 'https://www.test.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80,
            'staging': 8088
        }[env]