import os
from conans import ConanFile
from conans.tools import Version


class BlazeConan(ConanFile):
    name = "blaze"
    version = "3.4"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://bitbucket.org/blaze-lib/blaze"
    description = "open-source, high-performance C++ math library for dense and sparse arithmetic"
    topics = ("conan", "blaze", "math", "algebra", "linear algebra", "high-performance")
    license = "New (Revised) BSD license"

    no_copy_source = True

    def source(self):
        self.run("git clone https://bitbucket.org/blaze-lib/blaze")
        self.run("cd blaze && git checkout v%s" % self.version)

    def package(self):
        self.copy(pattern="*.h", src="blaze", dst="include")
