
class color:
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

        return color(r, g, b).return_color_in("RGB")

    def return_color_in(self, code):
        if code == "RGB":
            return "{} ({}, {}, {})".format(code, self.R * 255, self.G * 255, self.B * 255)
        if code == "HSB":
            return "{} ({}, {}, {})".format(code, self.R * 360, self.G * 100, self.B * 100)


color1 = color(252 / 255, 200 / 255, 194 / 255)
color2 = color(129 / 255, 181 / 255, 237 / 255)

print(color1.return_color_between(color2, 0.91176471))
