from setuptools import setup, find_packages

setup(name='directtextbook',
      version='0.1',
      description='Scraping prices from directtextbook.com',
      author_email='o.volodin@yahoo.com',
      packages=['directtextbook'],
      install_requires=['unirest','beautifulsoup4', 'scraperwiki'],
      zip_safe=False)

