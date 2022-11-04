from setuptools import setup , find_packages

setup(
    name = 'preprocesscli',
    version = '0.0.0',
    packages = find_packages(),
    install_requires = [
        'sklearn',
        'pyfiglet',
        'pandas'
    ],
    entry_points='''
     [console_scripts]
     preprocesscli=preprocesscli
    '''
)