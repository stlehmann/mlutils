from setuptools import setup, find_packages

setup(
    name='mlutils',
    version='0.1.0',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url='https://github.com/stlehmann/mlutils',
    license='MIT',
    author='Stefan Lehmann',
    author_email='stlm@posteo.de',
    description='Machine learning utility package'
)
