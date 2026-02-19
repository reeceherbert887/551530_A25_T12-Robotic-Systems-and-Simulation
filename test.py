from PIL import Image, ImageDraw

def make_silly_image(path="silly_face.png"):
	img = Image.new("RGB", (400, 400), (255, 240, 140))
	d = ImageDraw.Draw(img)
	d.ellipse((50, 50, 350, 350), fill=(255, 255, 0), outline=(0, 0, 0), width=4)
	d.ellipse((125, 140, 175, 190), fill=(0, 0, 0))
	d.ellipse((225, 140, 275, 190), fill=(0, 0, 0))
	d.arc((130, 200, 270, 320), start=0, end=180, fill=(0, 0, 0), width=6)
	d.text((150, 330), "DUMB!", fill=(0, 0, 0))
	img.save(path)
	try:
		img.show()
	except Exception:
		pass
	return path

if __name__ == "__main__":
	try:
		out = make_silly_image()
		print(f"Wrote silly image to {out}")
	except Exception as e:
		print("Couldn't create/display silly image:", e)


##123
