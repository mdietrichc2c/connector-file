# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Matthieu Dietrich
#    Copyright 2016 Camptocamp SA
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
from openerp.addons.connector_file.unit.document import FileSynchronizer, DirectFileSynchronizer, AsyncFileSynchronizer

from .s3_policy import S3FileGetterPolicy
from ..backend import file_import_s3


class S3FileSynchronizer(FileSynchronizer):

    @property
    def file_getter_policy_instance(self):
        """ Return an instance of ``S3FileGetterPolicy``.

        The instantiation is delayed because some synchronizations do
        not need such a unit and the unit may not exist.

        """
        if self._file_getter_policy_instance is None:
            self._file_getter_policy_instance = (
                self.environment.get_connector_unit(S3FileGetterPolicy)
            )
        return self._file_getter_policy_instance


@file_import_s3
class DirectS3FileSynchronizer(S3FileSynchronizer, DirectFileSynchronizer):

    """File Synchronizer, synchronous version."""

    pass


@file_import_s3
class AsyncS3FileSynchronizer(S3FileSynchronizer, AsyncFileSynchronizer):

    """File Synchronizer, asynchronous version."""

    pass
