from setuptools import setup

setup(name='pynotes',
      version='1.0.0',
      description='A python package for taking awesome notes!',
      url='http://github.com/bryantfhayes/pynotes',
      author='Bryant Hayes',
      author_email='bryantfhayes@gmail.com',
      license='MIT',
      entry_points={
        'console_scripts': [
            'pyn = pynotes.__main__:main'
        ]
      },
      packages=['pynotes'],
      dependency_links=[],
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
