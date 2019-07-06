from setuptools import setup

setup(
    name='netl',
    version='0.1',
    packages=['netl', 'tests'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        netl=netl.netlbot:run
    ''',
)

