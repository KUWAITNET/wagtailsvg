from bs4 import BeautifulSoup


def clear_svg_from_scripts(svg_file):
    """
        1- remove the clear html and scripts nodes totally
            with their included tags/scripts

        2- xml tags themself may have JS events,
            like (`onmouseover`, `onmouseout`, .. )
            so remove them

        3- xml tags themself may have Links to External Js code
           inside (`href`, `src`), so remove them
    """

    file_xml = BeautifulSoup(svg_file, "xml")
    for element in file_xml.find_all(["script", "html"]):
        element.decompose()

    for element in file_xml.find_all(True):
        copy_attrs = element.attrs.copy()

        for attr in element.attrs:
            att_name = attr.lower()

            if att_name.startswith('on'):
                del copy_attrs[attr]

            if att_name == "href" or att_name == "scr":
                if element[attr].lower().startswith('javascript:'):
                    del copy_attrs[attr]

        element.attrs = copy_attrs

    cleaned_xml_bytes = bytes(file_xml.prettify(), 'utf8')

    return cleaned_xml_bytes
