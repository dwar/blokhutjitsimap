# Blokhut Jitsi Map
Interactieve kaart van de blokhut om verschillende ruimtes/plekken virtueel binnen te gaan. Voor de iScout editie van 2021 tijdens Covid-19


## Inkscape
De svg files zijn alleen nog bewerkt met inkscape. Blokhut.svg is de bron, de afbeeldingen voor mobiel en desktop moeten handmatig gemaakt worden.
- Blokhut_M.svg is voor mobiel (Smal zonder hover)
- Blokhut_Desktop.svg is voor de desktop (Breed met hover)

### Interactie
Onder de laag Desktop bevinden zich de lagen met de overlays. (D-Keuken enz) Op deze laag staat als het goed is 1 group met een 1 path en 1 text. De group is opacity = 1

Events van de group:
- onclick
  ```
  window.location='https://meetme.bit.nl/AIiScout_Keuken'
  ```
- onmouseout
  ```
  this.style.opacity = 0;
  ```
- onmouseover
  ```
  this.style.opacity = 1;
  ```
