import xml.etree.ElementTree as ElementTree
import os
ns_array = {
    'svg': 'http://www.w3.org/2000/svg', 
    'xlink': 'http://www.w3.org/1999/xlink',
    'inkscape': 'http://www.inkscape.org/namespaces/inkscape'
}

def main(): 
    # Open original file
    el = ElementTree.parse(os.path.join(os.path.dirname(__file__), 'Blokhut.svg'))
    root = el.getroot()

    # Remove src images from svg
    del_layer(root, "layer_bron")
    del_layer(root, "layer_desktop")
    # del_layer(root, "layer_hover_desktop")

    # inkscape:groupmode

    # Make invisable and clickable
    for x in root.findall(".//*[@id='layer_hover_both']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = "window.location='https://meetme.bit.nl/AiIscout" + x.attrib["{" + ns_array['inkscape'] + "}label"] + "'"
    for x in root.findall(".//*[@id='layer_hover_phone']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = "window.location='https://meetme.bit.nl/AiIscout" + x.attrib["{" + ns_array['inkscape'] + "}label"] + "'"        
    for x in root.findall(".//*[@id='layer_hover_desktop']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = "window.location='https://meetme.bit.nl/AiIscout" + x.attrib["{" + ns_array['inkscape'] + "}label"] + "'" 

    layers = root.findall(".//*[@inkscape:groupmode='layer']", ns_array)
    for l in layers:
        l.attrib['style'] = "display:inline"
        print(l.attrib['id'])

    req = root.findall(".//*[@id='outline_phone']", ns_array)[0]
    print("x        : " + req.attrib['x'])
    print("y        : " + req.attrib['y'])
    print("height   : " + req.attrib['height'])
    print("width    : " + req.attrib['width'])

    root.attrib['viewBox'] = " ".join([req.attrib['x'], req.attrib['y'], req.attrib['width'], req.attrib['height']])
    root.attrib['height'] = "100%" 
    root.attrib['width'] = "100%" 

    el.write(os.path.join(os.path.dirname(__file__),  "test.svg"))


def del_layer(root, layer):
    root.findall(".//*[@id='"+layer+"']/..", ns_array)[0].remove(root.findall(".//*[@id='"+layer+"']", ns_array)[0])


if __name__=="__main__": 
    main(); 
