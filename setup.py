from os.path import join, dirname
from setuptools import setup, find_packages

# __version__ = open(join(dirname(__file__), 'slackbot/VERSION')).read().strip()
# 
# install_requires = (
#     # 'requests>=2.4.0',
#     # 'websocket-client>=0.22.0,<=0.44.0',
#     # 'slacker>=0.9.50',
#     # 'six>=1.10.0'
# ) 
# 
excludes = (
    '*test*',
    '*local_settings*',
)

setup(
    name='lmtools',
    version='0.1',
    license='MIT',
    description='Tools for OTR with language models.',
    author='Taylor Sorensen',
    author_email='tsor1313@gmail.com',
    url='http://github.com/tsor13/lmtools',
    packages=find_packages(exclude=excludes),
    entry_points={
        'console_scripts': [
            'lm-pipeline = lmtools.pipeline:main',
            'lm-postprocess = lmtools.postprocessor:main',
        ]
    },
    # install_requires=install_requires,
    # classifiers=['Development Status :: 4 - Beta',
    #             'License :: OSI Approved :: MIT License',
    #             'Operating System :: OS Independent',
    #             'Programming Language :: Python',
    #             'Programming Language :: Python :: 2',
    #             'Programming Language :: Python :: 2.7',
    #             'Programming Language :: Python :: 3',
    #             'Programming Language :: Python :: 3.4',
    #             'Programming Language :: Python :: 3.5',
    #             'Programming Language :: Python :: 3.6']
)