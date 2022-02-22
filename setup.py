from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

install_requirements = parse_requirements('./requirements.txt', session=False)

reqs = [str(ir.req) for ir in install_requirements]

VERSION = '0.0.1'
DESCRIPTION = 'Covid-19 Data Extractor - India'
LONG_DESCRIPTION = 'Extracts Covid-19 status from "url = https://www.mohfw.gov.in/data/datanew.json" '

setup(
    name = 'CovidStatusIndia',
    version=VERSION,
    author='Sudharshan Akshay',
    author_email='',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    package=find_packages(),
    keywords=['python', 'covid-19', 'covid', 'status','india','data','extactor', 'json','sudharshan', 'akshay'],
    classifiers = [
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developer",
        "Programing Language :: Python :: 3",
        "Operating System :: Linux :: *",
        "Operating System :: Microsoft :: Windows"
    ],
    install_requires = reqs
)