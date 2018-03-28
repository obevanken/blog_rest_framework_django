import environ

project_root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, False),)
CURRENT_ENV = 'dev' 


env.read_env('./mysite/{}.env'.format(CURRENT_ENV))
