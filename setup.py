from distutils.core import setup

setup(
    name='startup_name_generator',
    entry_points={
        'console_scripts': ['startup-name-generator=__main__:main'],
    },
    packages=['src'],
    version='0.1',
    url='',
    license='',
    author='',
    author_email='',
    description=''
)
