from django.http import JsonResponse
from django.utils.translation import gettext as _

from wagtail.contrib.modeladmin.views import (
    CreateView,
    EditView,
)
from wagtailsvg.admin_forms import DiwanSvgForm


class DiwanSVGCreateView(CreateView):
    form_class = DiwanSvgForm

    def get_form_class(self):
        return DiwanSvgForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return super().post(request, *args, **kwargs)

        else:
            return JsonResponse(
                {
                    "title": _("Failed"),
                    "message": _(
                        "The Svg could not be created due to errors."
                    ),
                    "errors": form.errors,
                }, status=400,
            )


class DiwanSVGEditView(EditView):
    form_class = DiwanSvgForm

    def get_form_class(self):
        return DiwanSvgForm

