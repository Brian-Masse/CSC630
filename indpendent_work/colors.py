import math

class color:

    hex_values = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"  ]

    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def return_color_between(self, color2, perc):
        r_change = color2.R - self.R
        g_change = color2.G - self.G
        b_change = color2.B - self.B

        r = self.R + (r_change * perc)
        g = self.G + (g_change * perc)
        b = self.B + (b_change * perc)

        return color(r, g, b)

    def return_color_in(self, code):
        if code == "RGB":
            return "{} ({}, {}, {})".format(code, self.R, self.G, self.B)
        if code == "HSB":
            return "{} ({}, {}, {})".format(code, self.R * 360, self.G * 100, self.B * 100)
        if code == "HEX":
            hex1 = self.return_hex(self.R)
            hex2 = self.return_hex(self.G)
            hex3 = self.return_hex(self.B)
            return "#{}{}{}{}{}{}".format( hex1[0], hex1[1], hex2[0], hex2[1], hex3[0], hex3[1] )

    def return_hex(self, component ):
        rounded = math.floor(component / 16)
        remainder = (component / 16) - rounded
        
        hex1 = self.hex_values[rounded]
        hex2 = self.hex_values[math.floor(remainder * 16)]
        return (hex1, hex2)
    
    def return_HSB( self ):
        r = self.R / 255
        g = self.G / 255
        b = self.B / 255

        cmax = max( r, g, b )
        cmin = min( r, g, b )
        delta = cmax - cmin

        h = 0
        s = 0
        v = 0

        # hue:
        if delta == 0:
            h = 0
        elif cmax == r:
            h = 60 * ( (( g - b ) / delta) % 6 )
        elif cmax == g:
            h = 60 * ( (( b - r ) / delta) + 2 )
        elif cmax == b:
            h = 60 * ( (( r - g ) / delta) + 4 )
        
        # saturation
        if cmax == 0:
            s = 0
        else:
            s = delta / cmax
        
        # value
        v = cmax

        return ( h, s * 100, v * 100 )

    def return_color_grad(self, second_color, steps):
        colors = []
        for step in range(0, steps):
            interval = step / (steps - 1)
            color = self.return_color_between(second_color, interval)
            colors.append(color.return_color_in("HEX"))
        return colors

class pallet:
    def __init__(self, grad, primary_color, secondary_color, background, secondary_background):
        self.grad = grad
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.background = background 
        self.secondary_background = secondary_background