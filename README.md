# Blokhut Jitsi Map
Interactieve kaart van de blokhut om verschillende ruimtes/plekken virtueel binnen te gaan. Voor de iScout editie van 2021 tijdens Covid-19

## Kaartje
Er zijn een aantal kaartje van de blokhut met linkjes naar verschillende jitsi ruimtes. (convigureerbaar in parse.py)
- phone.svg is voor mobiel (Smal)
- desktop.svg is voor de desktop (Breedt)
- android.svg voor android met de jitsi app (deep link)

### Interactie
Het bestand parse.py maakt van het bestant Blokhut.py de 3 output bestanden. 

De onclick van de ruimtes worden gemaakt met parse.py (de bestaande worden overschreven)
- onclick
  ```
  window.location='https://meetme.bit.nl/AIiScout_Keuken'
  ```
De hover over de ruimte wordt verkregen door de transparantie van de elementen '''hover_'''
- onmouseout
  ```
  this.style.opacity = 0;
  ```
- onmouseover
  ```
  this.style.opacity = 1;
  ```
