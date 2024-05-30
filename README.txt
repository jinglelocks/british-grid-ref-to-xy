A QGIS plugin for plotting data referenced with the British National Grid (BNG) system. 

Converts BNG two-letter references (0-10 digits) to Cartesian (XY) coordinates, adhering to the bottom-left corner convention. 

Input: a CSV with at least one record and two fields referring to an 'id' and a 'grid reference'. 
Output: a temporary vector layer (point-geometry) with four fields: 'id', 'grid reference', 'easting' and 'northing'. 

Additional support for plotting the centre of a grid square (counter to the bottom-left principle) and for plotting DINTY tetrads is being tested.