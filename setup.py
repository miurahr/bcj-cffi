import os
from setuptools import setup
from setuptools.command.egg_info import egg_info


# Work around pypa/setuptools#436.
class my_egg_info(egg_info):
    def run(self):
        try:
            os.remove(os.path.join(self.egg_info, "SOURCES.txt"))
        except FileNotFoundError:
            pass
        super().run()


setup(use_scm_version={"local_scheme": "no-local-version"},
      package_dir={"": "src"},
      cffi_modules=["src/ffi_build.py:ffibuilder"],
      cmdclass={"egg_info": my_egg_info},
      )
