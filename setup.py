from setuptools import setup, find_packages


setup(
    name='aiohttp-tools',
    version='0.0.1',
    author='Valery Vishnevskiy',
    author_email='v.v.vishnevskiy@gmail.com',
    license='as-is',
    packages=find_packages(),
    install_requires=[
        'aiohttp'
    ],
    classifiers=[
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
