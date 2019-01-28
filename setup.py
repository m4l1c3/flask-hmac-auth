from distutils.core import setup

setup(
    name = 'flask_hmac_auth',
    version = '1.0.0',
    description = 'A Flask middleware for HMAC request auth',
    author = 'm4l1c3',
    author_email = 'm4l1c3@tutanota.com',
    url = 'https://github.com/m4l1c3/flask-hmac-auth',
    py_modules=['flask_hmac_auth'],
    install_requires=[
        # list of this package dependencies
    ],
    entry_points='''
        [console_scripts]
        flask_hmac_auth=flask_hmac_auth:cli
    ''',
)
