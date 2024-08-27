"""{{cookiecutter.project_short_description}}."""

from importlib.metadata import version

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__copyright__ = "Copyright {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
__credits__ = [__author__]
__license__ = "{{cookiecutter.license}}"
__version__ = version("{{ cookiecutter.project_slug }}")
__maintainer__ = __author__
__status__ = "Prototype"  # Production

