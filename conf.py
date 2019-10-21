# This is the main settings file for package setup and PyPi deployment.
# Sphinx configuration is in the docsrc folder

# Main package name
PACKAGE_NAME = 'processfiles'

# Package version in the format (major, minor, release)
PACKAGE_VERSION_TUPLE = (0, 1, 4)

# Short description of the package
PACKAGE_SHORT_DESCRIPTION = 'Python local file process tracker'

# Long description of the package
PACKAGE_DESCRIPTION = """
Use this tool to select files of given file types in a folder, and track whether these files have been processed,
regardless of whether the script needs to be run multiple times. Stores progress on the files as a text file in the
same folder, so that a long-running operation on many files can be resumed where it left off if it was stopped.
It will also automatically estimate time to completion.
See more at the repo page: https://github.com/whoopnip/py-process-files
"""

# Author
PACKAGE_AUTHOR = "Nick DeRobertis"

# Author email
PACKAGE_AUTHOR_EMAIL = 'whoopnip@gmail.com'

# Name of license for package
PACKAGE_LICENSE = 'MIT'

# Classifications for the package, see common settings below
PACKAGE_CLASSIFIERS = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]

# Add any third party packages you use in requirements here
PACKAGE_INSTALL_REQUIRES = [
    # Include the names of the packages and any required versions in as strings
    # e.g.
    # 'package',
    # 'otherpackage>=1,<2'
]

# Sphinx executes all the import statements as it generates the documentation. To avoid having to install all
# the necessary packages, third-party packages can be passed to mock imports to just skip the import.
# By default, everything in PACKAGE_INSTALL_REQUIRES will be passed as mock imports, along with anything here.
# This variable is useful if a package includes multiple packages which need to be ignored.
DOCS_OTHER_MOCK_IMPORTS = [
    # Include the names of the packages as they would be imported, e.g.
    # 'package',
]

PACKAGE_URLS = {
    'Code': 'https://github.com/whoopnip/py-process-files/',
    'Documentation': 'https://whoopnip.github.io/py-process-files/'
}
