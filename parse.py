import xml.etree.ElementTree as ElementTree

import os
import copy

ns_array = {
    'dc': 'http://purl.org/dc/elements/1.1/',
    'cc': 'http://creativecommons.org/ns#',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'svg': 'http://www.w3.org/2000/svg',
    'xlink': 'http://www.w3.org/1999/xlink',
    'sodipodi': 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd',
    'inkscape': 'http://www.inkscape.org/namespaces/inkscape'
}

pre = "window.location='https://meetme.bit.nl/AriensIngridIscout2021"
post = "#config.prejoinPageEnabled=false&config.startWithVideoMuted=false&config.startWithAudioMuted=false'"

def main(): 
    # Open original file
    # el = ElementTree.parse(os.path.join(os.path.dirname(__file__), 'Blokhut.svg'))
    el = ElementTree.parse(os.path.join(os.path.dirname(__file__), 'Blokhut.svg'))
    root = el.getroot()
    for ns, url in ns_array.items():
        ElementTree.register_namespace(ns,url)

    # Remove src images from svg
    map_id_del(root, "layer_bron")
    map_id_del(root, "layer_background")
    map_id_del(root, "script2")

    map_layer_showall(root)

    if False:
         map_outline_from(root, "outline_phone")
         map_id_del(root, "layer_desktop")
         map_hover_addlink(root, pre, post)
        #  map_hover_addlink(root, "window.location='https://meetme.bit.nl/AiIscout", "#config.startWithVideoMuted=true&config.startWithAudioMuted=true'")
         el.write(os.path.join(os.path.dirname(__file__),  "phone.svg"))
    else:
         map_outline_from(root, "outline_desktop")
         map_id_del(root, "layer_phone")
         map_hover_addlink(root, pre, post)
         el.write(os.path.join(os.path.dirname(__file__),  "desktop.svg"))

def map_outline_from(root, outline):
    req = root.findall(".//*[@id='"+outline+"']", ns_array)[0]
    root.attrib['viewBox'] = " ".join([req.attrib['x'], req.attrib['y'], req.attrib['width'], req.attrib['height']])
    # print("x        : " + req.attrib['x'])
    # print("y        : " + req.attrib['y'])
    # print("height   : " + req.attrib['height'])
    # print("width    : " + req.attrib['width'])

    root.attrib['height'] = "100%" 
    root.attrib['width'] = "100%" 

def map_id_del(root, layer):
    root.findall(".//*[@id='"+layer+"']/..", ns_array)[0].remove(root.findall(".//*[@id='"+layer+"']", ns_array)[0])

def map_layer_showall(root):
    layers = root.findall(".//*[@inkscape:groupmode='layer']", ns_array)
    for l in layers:
        l.attrib['style'] = "display:inline"
        # print(l.attrib['id'])

def map_hover_addlink(root,pre,post):
    # Make clickable and hide hovers by default
    for x in root.findall(".//*[@id='layer_hover_both']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = pre + x.attrib["{" + ns_array['inkscape'] + "}label"] + post
    for x in root.findall(".//*[@id='layer_hover_phone']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = pre + x.attrib["{" + ns_array['inkscape'] + "}label"] + post        
    for x in root.findall(".//*[@id='layer_hover_desktop']/svg:g", ns_array):
        x.attrib['style'] = 'opacity:0'
        x.attrib['onclick'] = pre + x.attrib["{" + ns_array['inkscape'] + "}label"] + post 

if __name__=="__main__": 
    main(); 
