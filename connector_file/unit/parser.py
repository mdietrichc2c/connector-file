# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Leonardo Pistone, Nicolas Bessi
#    Copyright 2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
"""Connector Synchronizers."""

from openerp.addons.connector.unit.synchronizer import ImportSynchronizer


class BaseParser(ImportSynchronizer):

    """Base class for a parser.

    The parser takes care of parsing raw files to produce chunks with
    prepared JSON data.

    """

    def __init__(self, environment):
        super(BaseParser, self).__init__(environment)
        self._parse_policy_instance = None
        self._parse_error_policy = None

    def ask_files(self):
        """Defined in specific parsers."""
        raise NotImplementedError

    def parse_one_file(self, attachment_binding_id):
        """Defined in specific parse."""
        raise NotImplementedError
