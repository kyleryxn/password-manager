import setuptools

with open('requirements.txt', 'r') as file:
    install_requires = file.read().splitlines()

setuptools.setup(
    name='password_manager',
    packages=['password_manager']
)
