LESS-Mixin-for-CSS-arrows
=========================

A customizable LESS mixin to handle CSS arrows.

Usage
-----
`.arrow(size, color, direction, offset, border-size, border-color);`

1.  **Size** is the with of the arrow
2.  **Color** is the color of the arrow (plain color required)
3.  **Direction** is the orientation of the arrow (top, right, bottom, left)
4.  **Offset** is the position of the arrow on its axis (px or %)
4.  **Border-size** is the width of the border if there is one (optional; default "0")
5.  **Border-color** is the color of the border if there is one (optional; default "inherit")


Extra
-----
Drop-shadows can be used on the element to create a shadow on the arrow as well 


Example
-------
`.arrow(10px, #08C, bottom, 50%, 1px, darken(#08C, 10%))`	