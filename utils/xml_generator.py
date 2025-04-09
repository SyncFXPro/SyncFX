from lxml import etree

def generate_xml(beat_times, output_path="output/beat_markers.xml"):
    fcpxml = etree.Element("fcpxml", version="1.8")
    resources = etree.SubElement(fcpxml, "resources")
    library = etree.SubElement(fcpxml, "library")
    event = etree.SubElement(library, "event", name="BeatMarkers")
    project = etree.SubElement(event, "project", name="AutoMarkers")
    sequence = etree.SubElement(project, "sequence", duration="600/600s", format="r1")
    spine = etree.SubElement(sequence, "spine")

    for i, time in enumerate(beat_times):
        marker = etree.SubElement(spine, "marker", start=f"{time}s", duration="1/600s", value=f"Beat {i+1}")

    tree = etree.ElementTree(fcpxml)
    tree.write(output_path, pretty_print=True, xml_declaration=True, encoding="utf-8")
