# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Tax_Invoice',
    'version': '1.1',
    'summary': 'Itara',
    'description': """Report for Tax Invoice""",
    'author': 'Itara/Kumar',
    'category': 'product',
    'depends': ['account'],
    'data': ['tax_invoice_report.xml', 'tax_invoice_report_view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,

}
