#!/usr/bin/env python3

# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Contributor(s): Sergey Sharybin
#
# #**** END GPL LICENSE BLOCK #****

# <pep8 compliant>

# Usage: ./check_release.py -- ../path/to/release/folder


import os
import sys
import unittest

import check_module_enabled
import check_module_numpy
import check_module_requests
import check_static_binaries
from check_utils import sliceCommandLineArguments


def load_tests(loader, standard_tests, pattern):
    standard_tests.addTests(loader.loadTestsFromTestCase(
        check_module_enabled.UnitTesting))
    standard_tests.addTests(loader.loadTestsFromTestCase(
        check_module_numpy.UnitTesting))
    standard_tests.addTests(loader.loadTestsFromTestCase(
        check_module_requests.UnitTesting))
    standard_tests.addTests(loader.loadTestsFromTestCase(
        check_static_binaries.UnitTesting))
    return standard_tests


def main():
    # Slice command line arguments by '--'
    unittest_args, parser_args = sliceCommandLineArguments()
    # Construct and run unit tests.
    unittest.main(argv=unittest_args)


if __name__ == "__main__":
    main()