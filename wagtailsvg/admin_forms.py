from io import BytesIO
from django.core.files.images import File

from wagtail.admin.forms import (
    WagtailAdminModelForm
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
