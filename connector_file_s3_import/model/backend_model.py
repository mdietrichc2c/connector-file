# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Matthieu Dietrich
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
"""Backend Model for Amazon S3.
"""

from openerp.osv import orm, fields


class file_import_s3_backend(orm.Model):
    """ Specific S3 version of the file import backend """
    _inherit = "file_import.backend"

    def _select_versions(self, cr, uid, context=None):
        """Parent model inheritance (needs redefinition)."""
        return super(file_import_s3_backend,
                     self)._select_versions(cr, uid, context=context) + [
            ('s3_1', 'Amazon S3 v1')]

    _columns = {
        'version': fields.selection(_select_versions,
                                    string='Version',
                                    required=True),
        's3_access_key': fields.char('Amazon S3 Access Key'),
        's3_secret_access_key': fields.char('Amazon S3 Secret Access Key'),
        's3_bucket_name': fields.char('Amazon S3 Bucket Name'),
        's3_input_folder': fields.char('FTP Input folder'),
        's3_failed_folder': fields.char('FTP Output folder'),
        's3_archive_folder': fields.char('FTP Archive folder'),
    }
