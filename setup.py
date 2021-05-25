# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dep_b']

package_data = \
{'': ['*']}

install_requires = \
['dep_c @ git+https://github.com/mtraynham/poetry_4051.git@f886f69d']

setup_kwargs = {
    'name': 'dep-b',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'mtraynham',
    'author_email': 'test@test.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
