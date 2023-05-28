from wagtail.contrib.modeladmin.views import (
    CreateView,
    EditView,
)
from wagtailsvg.admin_forms import DiwanSvgForm


class DiwanSVGCreateView(CreateView):
    form_class = DiwanSvgForm

    def get_form_class(self):
        return DiwanSvgForm


class DiwanSVGEditView(EditView):
    form_class = DiwanSvgForm

    def get_form_class(self):
        return DiwanSvgForm

