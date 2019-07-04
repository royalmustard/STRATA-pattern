<h1>STRATA-pattern</h1>

This is a tool to convert any image file with the following
specifications into a valid pattern bitmap file for the STRATA
SEM/FIB.
- Background is white (No pattern here)
- Pattern is black <br>
Any black value from RGB 0,0,0 to RGB 254,254,254 can be used,
however it is recommended to use RGB 0,0,0 for every part for
the pattern unless different dwell times are required.
Dwell times scale with the RGB value used. RGB 0,0,0 means
the systems maximum dwell time is used and RGB 254, 254, 254
means a dwell time of around 100ns.
<br>
<br>
The program can also be used to convert regular images for patterning,
however the scientific application of that is questionable.
