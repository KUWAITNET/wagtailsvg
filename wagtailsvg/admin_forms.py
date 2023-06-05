from io import BytesIO
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import File
from django.utils.html import format_html
from django.utils.translation import gettext as _

from wagtail.admin.forms import (
    WagtailAdminModelForm
)
from wagtail.admin.forms.collections import (
    collection_member_permission_formset_factory,
)

from wagtailsvg.models import Svg
from wagtailsvg.helpers import (
    check_if_svg_clean_from_scripts,
    clear_svg_from_scripts,
)


class DiwanSvgForm(WagtailAdminModelForm):
    clean_and_save = forms.BooleanField(
        initial=False, required=False
    )

    class Meta:
        model = Svg
        fields = [
            "title", "file", "collection", "tags",
        ]

    def clean(self):
        cleaned_data = super(DiwanSvgForm, self).clean()
        svg_file = cleaned_data.get("file")
        clean_and_save = cleaned_data.get("clean_and_save")

        if not clean_and_save:
            is_file_clean = check_if_svg_clean_from_scripts(svg_file)
            if not is_file_clean:
                error_msg = _(
                    "Selected file has malicious scripts, We can not save it to avoid security issues"
                    "<div class='help-text-line'>"
                    "<span>we can remove malicious scripts from your file so you can use it </span>"
                    f"<a id='cleanAndSaveBtn' class='btn btn-primary' data-file={svg_file}>"
                    "Clean And Save File</a>"
                    "</div>"
                )

                raise ValidationError({
                    "file": format_html(error_msg)
                })

        else:
            cleaned_xml_bytes = clear_svg_from_scripts(svg_file)
            cleaned_data["file"] = File(
                file=BytesIO(cleaned_xml_bytes),
                name=svg_file.name.split("/")[-1],
            )

        return cleaned_data


GroupSvgPermissionFormSet = collection_member_permission_formset_factory(
    Svg,
    [
        ("add_svg", _("Add"), _("Add/edit Svg you own")),
        ("change_svg", _("Edit"), _("Edit Svg image")),
        ("choose_svg", _("Choose"), _("Select Svg in choosers")),
    ],
    "wagtailsvg/permissions/includes/svg_permissions_formset.html",
)
