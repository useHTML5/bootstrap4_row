from __future__ import unicode_literals
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models
from . import forms


@plugin_pool.register_plugin
class Bootstrap4RowPlugin(CMSPluginBase):
    module = "Блоки"
    model = models.Bootstrap4Row
    name = 'Колонки'
    render_template = 'bootstrap4_row/row.html'
    allow_children = True
    child_classes = 'Bootstrap4ColumnPlugin',
    form = forms.NewRowForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        data = form.cleaned_data
        for x in range(int(data['create_columns']) if data['create_columns'] is not None else 0):
            col = Bootstrap4ColumnPlugin(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=obj.numchild,
                plugin_type=Bootstrap4ColumnPlugin.__name__
            )
            obj.add_child(instance=col)


@plugin_pool.register_plugin
class Bootstrap4ColumnPlugin(CMSPluginBase):
    module = "Блоки"
    model = models.Bootstrap4Column
    name = 'Колонка'
    render_template = 'bootstrap4_row/column.html'
    parent_classes = 'Bootstrap4RowPlugin',
    require_parent = True
    allow_children = True
