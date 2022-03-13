from PIL import Image, ImageDraw
from pathlib import Path

def main():
  size = 256
  img = Image.new('RGBA', (size, size))

  # Draw gradient
  draw = ImageDraw.Draw(img)
  colors = _interpolate(
    start=(255, 255, 255, 255),
    end=(0, 0, 0, 0),
    interval=size,
  )
  for col, color in zip(range(256), colors):
    draw.line((0, col, size, col), color)

  # Save as png
  img.save(
    fp=Path("./output.png"),
    format='png',
  )

  # Save as gif
  img.save(
    fp=Path("./output.gif"),
    format='gif',
    save_all=True,
    duration=5,
    optimize=False,
    loop=0,
  )


def _interpolate(start, end, interval):
  delta = [0 if interval == 0 else (e - s) / interval for s, e in zip(start, end)]

  values = []
  for i in range(interval):
    values.append(tuple(round(s + det * i) for s, det in zip(start, delta)))

  return values

main()