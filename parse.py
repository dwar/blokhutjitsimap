import xml.etree.ElementTree as ElementTree
import os

def main(): 
    # Open original file
    el = ElementTree.parse(os.path.join(os.path.dirname(__file__), 'Blokhut.svg'))
    root = el.getroot()

    ns_array = {
        'svg': 'http://www.w3.org/2000/svg', 
        'xlink': 'http://www.w3.org/1999/xlink',
        'inkscape': 'http://www.inkscape.org/namespaces/inkscape'
    }

    # Remove src images from svg
    root.findall("svg:g/[@id='layer_bron']/..", ns_array)[0].remove(root.findall("svg:g/[@id='layer_bron']", ns_array)[0])
    root.findall("svg:g/[@id='layer_phone']/..", ns_array)[0].remove(root.findall("svg:g/[@id='layer_phone']", ns_array)[0])
    root.findall("svg:g/[@id='layer_hover_phone']/..", ns_array)[0].remove(root.findall("svg:g/[@id='layer_hover_phone']", ns_array)[0])    


    # Make invisable and clickable
    for x in root.findall("svg:g/[@id='layer_hover_both']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = "window.location='https://meetme.bit.nl/AiIscout" + x.attrib["{" + ns_array['inkscape'] + "}label"] + "'"
    for x in root.findall("svg:g/[@id='layer_hover_phone']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = "window.location='https://meetme.bit.nl/AiIscout" + x.attrib["{" + ns_array['inkscape'] + "}label"] + "'"        
    for x in root.findall("svg:g/[@id='layer_hover_desktop']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = "window.location='https://meetme.bit.nl/AiIscout" + x.attrib["{" + ns_array['inkscape'] + "}label"] + "'" 

    req = root.findall("svg:g/*[@id='outline_desktop']", ns_array)[0]
    print("x        : " + req.attrib['x'])
    print("y        : " + req.attrib['y'])
    print("height   : " + req.attrib['height'])
    print("width    : " + req.attrib['width'])

    root.attrib['viewBox'] = " ".join([req.attrib['x'], req.attrib['y'], req.attrib['width'], req.attrib['height']])
    root.attrib['height'] = "100%" #req.attrib['height']
    root.attrib['width'] = "100%" #req.attrib['width']

    el.write(os.path.join(os.path.dirname(__file__),  "test.svg"))

  
if __name__=="__main__": 
    main(); 
