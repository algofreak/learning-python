def color_detector(color):
    if color[0] == 0 and color[1] == 0 and color[2] == 0:
        return "Black"
    elif color[0] == 255 and color[1] == 255 and color[2] == 255:
        return "White"
    elif color[0] == 0 and color[1] == 100 and color[2] == 50:
        return "Red"
    elif color[0] == 1 and color[1] == 0 and color[2] == 0:
        return "Still Black"
    else:
        return "ERROR ERROR ERROR ERROR"


while True:
    print("Enter RGB: ")
    r = input("")
    if r == 'q':
        break;
    g = input("")
    b = input("")
    color = [int(r), int(g), int(b)]
    print("RGB" + color.__str__() + " is " + color_detector(color))
