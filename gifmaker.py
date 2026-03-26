from PIL import Image

img = Image.open("a.png").convert("RGBA")
frames = []
bg_size = (600, 600)

for angle in range(0, 360, 10):
    frame = Image.new("RGBA", bg_size, (0, 0, 0, 0))
    rotated = img.rotate(angle, expand=True)

    x = int((bg_size[0] - rotated.width) / 2)
    y = int((bg_size[1] - rotated.height) / 2)

    frame.paste(rotated, (x, y), rotated)
    frames.append(frame)

frames[0].save("a.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)