# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PageField
from solo.models import SingletonModel


# from adminsortable.models import SortableMixin

class Bootstrap4Row(CMSPlugin):
    column_classes = models.TextField(verbose_name="Column classes", default='col-lg-4',
                                      help_text="offset-lg-1 mx-lg-2 ")
    row_classes = models.TextField(verbose_name="Row classes", default='row', help_text="row no-gutters")
    container_classes = models.TextField(verbose_name="Container classes", default='container',
                                         help_text='container container-fluid')


class Bootstrap4Column(CMSPlugin):
    override_column_classes = models.TextField(verbose_name="class(переписать родительские)", blank=True)
