import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    image = np.zeros((width, height))

    for x in range(width):
        for y in range(height):
            real = xmin + (x / width) * (xmax - xmin)
            imag = ymin + (y / height) * (ymax - ymin)
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[x, y] = color

    return image

def display_fractal(image):
    plt.imshow(image, cmap='viridis', extent=(-2, 2, -2, 2))
    plt.colorbar()
    plt.title('Mandelbrot Fractal')
    plt.show()

if __name__ == "__main__":
    width, height = 800, 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    max_iter = 100

    fractal_image = generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)
    display_fractal(fractal_image)
