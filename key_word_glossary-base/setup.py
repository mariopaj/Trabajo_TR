import pathlib
from setuptools import find_packages, setup


HERE = pathlib.Path(__file__).parent


VERSION = '0.1'
PACKAGE_NAME = 'key_word_glossary'
AUTHOR = 'Mario Pajares García'
AUTHOR_EMAIL = 'mariopajares1996@gmail.com'
URL = 'https://github.com/mariopaj'


LICENSE = 'MIT'
DESCRIPTION = 'Librería para elaborar glosarios a través de key words' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = [
      'pandas', 'people_also_ask', 'youtubesearchpython', 'time', 'numpy', 'deepl'
      ]


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)