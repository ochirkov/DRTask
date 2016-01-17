from setuptools import setup

setup(name='bla',
      version='0.1',
      description='data robot app',
      author='Chirkov Oleksandr',
      author_email='ironloriin20@gmail.com',
      scripts=['bla/bla/bin/drapp'],
      packages=['bla'],
      include_package_data=True,
      zip_safe=False)