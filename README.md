# Blokhut Jitsi Map
Interactieve kaart van de blokhut om verschillende ruimtes/plekken virtueel binnen te gaan. Voor de iScout editie van 2021 tijdens Covid-19

## Kaartjes
Er zijn een aantal kaartje van de blokhut met linkjes naar verschillende jitsi ruimtes.
- [phone.svg](https://dwar.github.io/blokhutjitsimap/phone.svg) is voor mobiel (Smal)
- [desktop.svg](https://dwar.github.io/blokhutjitsimap/desktop.svg) is voor de desktop (Breedt)
- [android.svg](https://dwar.github.io/blokhutjitsimap/android.svg) voor android met de jitsi app (deep link)

Eenmaal in een ruimte kan de met de terugknop weer terug naar het kaartje, om in een andere ruimte te kijken.

### Techniek
Het bestand parse.py maakt van het bestand Blokhut.svg de 3 output bestanden. (phone.svg, desktop.svg en android.svg) 
Blokhut.svg is gemaakt met inkscape en kan daar ook nog mee bewerkt worden. De url waar de ruimte naar verwijst wordt gegenereerd in parse.py. Dit gebeurd aan de hand van de uit Blokhut.svg en jitsi_host, event_prefix (en pre en post) uit parse.py
