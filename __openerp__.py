# -*- coding: utf-8 -*-
{
    'name': "crm_tag_cloud",

    'summary': """
        Tag Cloud Search Filter for Opportunities""",

    'description': """
        This module provides all the tags (aka categories, aka categ_id) 
        as filter options under the search view drawer. It creates a Tag 
        Cloud, allowing the user to see all the tags in one shot.
    """,

    'author': "Transformix Engineering Inc.",
    'website': "http://www.transformix.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],
    'data': ['tag_view.xml'],
    'demo': [],
    'tests': [],
}
