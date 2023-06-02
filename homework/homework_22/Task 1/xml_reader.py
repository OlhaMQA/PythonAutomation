import xml.etree.ElementTree as ET


class XmlProcessor:

    def xml_to_string(self, root):
        return ET.tostring(root, encoding="unicode")

    def string_to_xml(self, xml_string):
        return ET.fromstring(xml_string)

    def update_all_elements(self, root, tag, value):

        for element in root.iter():
            # update text of element
            if element.tag == tag:
                element.text = value
        return root

    def add_new_attribute(self, root, parent_attr, new_attr, attr_value):

        for element in root.findall(parent_attr):
            new_element = ET.Element(new_attr)
            new_element.text = attr_value
            # Add the new attr element to the current element
            element.append(new_element)
        return root


if __name__ == '__main__':
    processor = XmlProcessor()
    tree = ET.parse('xml.xml')
    root = tree.getroot()
    string_root = processor.xml_to_string(root)
    print(string_root)
    print(processor.string_to_xml(string_root))
    updated_cgpa_root = processor.update_all_elements(root, 'cgpa', '10')
    print(processor.xml_to_string(updated_cgpa_root))
    added_diploma_number_root = processor.add_new_attribute(root, 'student', 'diploma_number', '123456')
    print(processor.xml_to_string(added_diploma_number_root))



