"""Setup file for myTFlib"""
# python setup.py build_ext --inplace
# python setup.py bdist_wheel

from __future__ import annotations
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
import sys


def load_module(path: str = "src/myTFlib/__init__.py"):
    """Load module from given path"""
    full_path = Path(__file__).parent / path
    spec = spec_from_file_location("myTFlib", str(full_path))
    if not spec or not spec.loader:
        raise ImportError(f"Cannot load module from {full_path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_version() -> str:
    """Extract __version__ from myTFlib.__init__"""
    return getattr(load_module(), "__version__", "0.0.0")


# Requirements
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with open("dev-requirements.txt") as f:
    dev_requires = f.read().splitlines()

# Cython extensions
cython_modules = [
    Extension(
        name=str(file.relative_to("src").with_suffix("")).replace("/", "."),
        sources=[str(file)],
    )
    for file in Path("src").rglob("*.pyx")
]

setup(
    name="myTFlib",
    version=get_version(),
    description="My custom TensorFlow-based CV library",
    author="Daeseong Jung",
    author_email="jds.illusory@gmail.com",
    python_requires=">=3.9",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    ext_modules=cythonize(
        cython_modules,
        compiler_directives={"language_level": "3"},
    ),
    zip_safe=False,
)