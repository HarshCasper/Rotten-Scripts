import tkinter as tk


def convert_to_greyscale(image, method=3):

    for x in range(image.width()):
        for y in range(image.height()):

            pixel = image.get(x, y)

            if method in (0, 1, 2): # R or G or B
                val = pixel[method]
                pixel = (val, val, val)
            elif method == 3:   # average
                val = sum(pixel)//3
                pixel = (val, val, val)
            #else:              # without changes
            #   pixel = pixel

            image.put('#%02x%02x%02x' % pixel, (x, y))


def add_images(canvas):

    positions = [(450, 450), (150, 150), (450, 150), (150, 450)]
    images = []

    for index, pos in enumerate(positions, 1):

        image = tk.PhotoImage(file="PhotoImage%i.gif" % index)

        convert_to_greyscale(image) #(image, index-1)

        canvas.create_image(pos, image=image)

        images.append(image) 

    return images


def main():
    window = tk.Tk() 
    window.title("Testing stuff")
    window.geometry("600x600+10+20")

    canvas = tk.Canvas(window)
    canvas.config(background="blue")
    canvas.pack(fill=tk.BOTH, expand=True)

    images = add_images(canvas)

    window.mainloop()

main()
