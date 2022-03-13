# Pillow GIF gradient issue

Environment
- OS: `Ubuntu 18.04`
- Python: `3.9.10`
- Pillow: `9.0.1`

## Description
Saving as `gif` format seems to restrict color pallet and lose the transparency from the original image.

In the following example, we have a gradient that when we save as `gif` output, we can notice that it becomes striped and lose the transparency.

Original image (saved as `png`):
![Original](output.png)

Git format:

![Gif](output.gif)

## Getting started
Install requirements
```
pip install -r requirements.txt
```

## Run
In order to regenerate images run:
```
python main.py
```
It'll generate `output.png` and `output.gif`