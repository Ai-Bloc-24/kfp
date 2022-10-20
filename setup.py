import os
import re

from setuptools import setup

NAME = 'kfp'

def get_requirements(requirements_file):
    file_path = os.path.join(os.path.dirname(__file__), requirements_file)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if not line.startswith('#') and line]
    return lines

def find_version(*file_path_parts):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, *file_path_parts), 'r') as fp:
        version_file_text = fp.read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file_text,
        re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name=NAME,
    version=find_version('kfp', '__init__.py'),
    description='KubeFlow Pipelines SDK',
    author='The Kubeflow Authors',
    install_requires=get_requirements('requirements.txt'),
    packages=[
        'kfp',
        'kfp.compiler',
        'kfp.components',
        'kfp.components.structures',
        'kfp.dsl',
        'kfp.dsl.extensions',
    ],
    )
