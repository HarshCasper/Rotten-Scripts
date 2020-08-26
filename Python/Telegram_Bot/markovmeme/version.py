"""

Copyright (C) 2019-2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

__version__ = "0.0.1"
AUTHOR = "Vanessa Sochat"
AUTHOR_EMAIL = "vsochat@stanford.edu"
NAME = "markovmeme"
PACKAGE_URL = "http://www.github.com/vsoch/markovmeme"
KEYWORDS = "generate memes using a Markov Model"
DESCRIPTION = "Command line tool for generating markov memes."
LICENSE = "LICENSE"

################################################################################
# Requirements


INSTALL_REQUIRES = (("Pillow", {"min_version": "6.0.0"}),)
TESTS_REQUIRES = (("pytest", {"min_version": "4.6.2"}),)

INSTALL_REQUIRES_ALL = INSTALL_REQUIRES
