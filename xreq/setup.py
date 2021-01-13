from setuptools import setup

setup(
    name='scaling-robot',
    version='0.1',
    install_requires=[
        'Faker',
        'apache-airflow',
        'tweepy',

        #'numpy', 'pandas', 'numba',
        #'pydbgen',  # Data Generation

        #############################################
        # Web profile

        
        'requests', 'requests_oauthlib',  # HTTP client
        'aiohttp[speedups]',  #Async HTTP
        'dnspython',

        # 'django',               # Main Web Framework        
        'fastapi',              # Async micro HTTP framework
        'jinja2',               # template engine

        'websockets',           # Module available for uvicorn
        'aiofiles',             # async file server
        'httptools',            # Needed for uvicorn HTTP upgrade
        'Twisted[tls, http2]',  # Internet Apps
        'uvloop',               #high performance async loop
        'gunicorn',             # WSGI HTTP Server, and worker supervisor
        'uvicorn',              # ASGI Server

        # 'channels', 'channels_redis',   # ASGI Websockets

        # 'celery[redis]>=5.0.0',         # Distributor Task System
        # 'django-celery-beat',           # async and scheduled
        # # 'eventlet', 'gevent',         # async event frameworks
        
        # 'djangorestframework',  # Rest Framework
        # 'django-redis',         # Redis Cache
        # 'django-filter',        # ORM View Filters
        # 'markdown',             # Markdown support for the browsable API.


        'sqlalchemy', #ORM mainly for Fast
        'redis', 'aioredis', #redis drivers
        'pymongo', 'motor', #Mongo Drivers IO
        
        # 'psycopg2-binary', 'mysqlclient',  # RMDB drivers
    ]
)
