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

jitsi_host = "meetme.bit.nl"
event_prefix = 'AriensIngridIscout2021'

pre = "window.location='https://" + jitsi_host + "/" + event_prefix
post = "#config.prejoinPageEnabled=false&config.startWithVideoMuted=false&config.startWithAudioMuted=false'"
input = 'Blokhut.svg'

pre_desktop = pre
post_desktop = post
output_desktop = "desktop.svg"

pre_phone = pre
post_phone = post
output_phone = "phone.svg"

pre_android = "window.location='intent://"  + jitsi_host + "/" + event_prefix
post_android = "#config.prejoinPageEnabled=false&config.startWithVideoMuted=false&config.startWithAudioMuted=false#Intent;scheme=org.jitsi.meet;package=org.jitsi.meet;end'"
output_android = "android.svg"



def main(): 
    # Open original file
    # el = ElementTree.parse(os.path.join(os.path.dirname(__file__), 'Blokhut.svg'))
    el = ElementTree.parse(os.path.join(os.path.dirname(__file__), 'Blokhut.svg'))
    root = el.getroot()
    for ns, url in ns_array.items():
        ElementTree.register_namespace(ns,url)

    base_dir = os.path.dirname(__file__)
    input_file = os.path.join(base_dir, 'Blokhut.svg')

    map_make_desktop(input_file, os.path.join(base_dir, output_desktop))
    map_make_android(input_file, os.path.join(base_dir, output_android))
    map_make_phone(input_file, os.path.join(base_dir, output_phone))



def map_make_generic(src):
    print(src)
    el = ElementTree.parse(src)
    root = el.getroot()

    # Remove src images from svg
    map_id_del(root, "layer_bron")
    map_id_del(root, "layer_background")
    map_id_del(root, "script2")

    map_layer_showall(root)
    return el, root

def map_make_desktop(src, dest):
    el, root = map_make_generic(src)
    map_outline_from(root, "outline_desktop")
    map_id_del(root, "layer_phone")
    map_hover_addlink(root, pre_desktop, post_desktop)

    el.write(dest)

def map_make_phone(src, dest):
    el, root = map_make_generic(src)
    map_outline_from(root, "outline_phone")
    map_id_del(root, "layer_desktop")
    map_hover_addlink(root, pre_phone, post_phone)
    el.write(dest)

def map_make_android(src, dest):
    el, root = map_make_generic(src)
    map_outline_from(root, "outline_phone")
    map_id_del(root, "layer_desktop")
    map_hover_addlink(root, pre_android, post_android)
    el.write(dest)

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


