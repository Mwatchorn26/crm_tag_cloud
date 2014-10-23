# -*- coding: utf-8 -*-
from openerp.models import Model
from openerp.fields import Char


class crm_tag_cloud(Model):
    _name = "crm_tag_cloud.crm_tag_cloud"

    name = Char()
