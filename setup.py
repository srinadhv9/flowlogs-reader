#  Copyright 2015 Observable Networks
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from setuptools import setup, find_packages

PY2 = sys.version_info[0] == 2

setup(
    name='flowlogs_reader',
    version='1.1.1',
    license='Apache',
    url='https://github.com/obsrvbl/flowlogs-reader',

    description='Reader for AWS VPC Flow Logs',
    long_description=(
        'This project provides a convenient interface for accessing '
        'VPC Flow Log data stored in Amazon CloudWatch Logs.'
    ),

    author='Observable Networks',
    author_email='support@observable.net',

    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'flowlogs_reader = flowlogs_reader.__main__:main',
        ],
    },

    packages=find_packages(exclude=[]),
    test_suite='tests',

    install_requires=[
        'boto3>=1.7.75',
        'botocore>=1.10.75',
        'python-dateutil>=2.7.0'
    ],
    tests_require=['mock'] if PY2 else [],
)
