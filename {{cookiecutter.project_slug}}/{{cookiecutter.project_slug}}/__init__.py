# cSpell:words {{cookiecutter.project_slug}}

"""{{cookiecutter.project_short_description}}"""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__copyright__ = "Copyright {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
__credits__ = [__author__]
__license__ = "{{cookiecutter.license}}"
__version__ = "{{ cookiecutter.project_version }}"
__version_info__ = (int(v) for v in "{{cookiecutter.project_version}}".split("."))
__maintainer__ = __author__
__status__ = "Prototype"
