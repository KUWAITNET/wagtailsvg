from io import BytesIO
from django.core.files.images import File
from django.utils.translation import gettext as _

from wagtail.admin.forms import (
    WagtailAdminModelForm
)
from wagtail.admin.forms.collections import (
    collection_member_permission_formset_factory,
)

from wagtailsvg.models import Svg
from wagtailsvg.helpers import (
    clear_svg_from_scripts,
)


class DiwanSvgForm(WagtailAdminModelForm):
    class Meta:
        model = Svg
        fields = [
            "title", "file", "collection", "tags",
        ]

    def clean(self):
        cleaned_data = super(DiwanSvgForm, self).clean()

        svg_file = cleaned_data.get("file")
        cleaned_xml_bytes = clear_svg_from_scripts(svg_file)

        cleaned_data["file"] = File(
            file=BytesIO(cleaned_xml_bytes),
            name=svg_file.name.split("/")[-1],
        )
        return cleaned_data


GroupSvgPermissionFormSet = collection_member_permission_formset_factory(
    Svg,
    [
        ("add_svg", _("Add"), _("Add/edit images you own")),
        ("change_svg", _("Edit"), _("Edit any image")),
        ("choose_svg", _("Choose"), _("Select images in choosers")),
    ],
    "wagtailsvg/permissions/includes/svg_permissions_formset.html",
)
