from os.path import join, abspath, dirname
from setuptools import setup, find_packages

here = abspath(dirname(__file__))

with open(join(here, 'README.rst')) as f:
    readme = f.read()

with open(join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(join(abspath(dirname(__file__)), "VERSION"), "r") as v:
    VERSION = v.read().replace("\n", "")

setup(
    name='waf-brain',
    version=VERSION,
    packages=find_packages(),
    long_description=readme,
    install_requires=required,
    include_package_data=True,
    url='https://github.com/bbva/waf-brain',
    license='Apache2',
    description='WAF-brain: the clever and efficient Firewall for the Web',
    entry_points={'console_scripts': [
        'waf-brain = waf_brain.__main__:serve',
        'waf-models = waf_brain.__main__:list_models',
    ]},
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
    ],
)

