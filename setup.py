from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in project_management/__init__.py
from project_management import __version__ as version

setup(
	name="project_management",
	version=version,
	description="App que permite administrar el ciclo de vida de los proyectos en erpnext, utiliza funcionalidades del modulo project",
	author="buzola",
	author_email="it@buzola.mx",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
