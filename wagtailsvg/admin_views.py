from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.urls import reverse

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
            form.save()
            return JsonResponse(
                {
                    "title": _("Success"),
                    "next_url": reverse("wagtailsvg_svg_modeladmin_index"),
                }, status=200,
            )
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

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            form.save()
            return JsonResponse(
                {
                    "title": _("Success"),
                    "next_url": reverse("wagtailsvg_svg_modeladmin_index"),
                }, status=200,
            )
        else:
            return JsonResponse(
                {
                    "title": _("Failed"),
                    "message": _(
                        "The Svg could not be edited due to errors."
                    ),
                    "errors": form.errors,
                }, status=400,
            )
