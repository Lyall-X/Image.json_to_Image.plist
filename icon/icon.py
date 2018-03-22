# coding=utf-8
import os,sys
from PIL import Image

ios = [
	
	{"name": "Icon.png", "size": 57},
    {"name": "Icon@2x.png", "size": 114},
    {"name": "Icon-29.png", "size": 29},
    {"name": "Icon-29@2x.png", "size": 68},
    {"name": "Icon-40@2x.png", "size": 80},
    {"name": "Icon-40pad.png", "size": 40},
    {"name": "Icon-40pad@2x.png", "size": 80},
    {"name": "Icon-50.png", "size": 50},
    {"name": "Icon-50@2x.png", "size": 100},
    {"name": "Icon-60@2x.png", "size": 120},
    {"name": "Icon-72.png", "size": 72},
    {"name": "Icon-72@2x.png", "size": 144},
    {"name": "Icon-76.png", "size": 76},
    {"name": "Icon-76@2x.png", "size": 152},
    {"name": "Icon-1024.png", "size": 1024},
    {"name": "Icon-Small.png", "size": 29},
    {"name": "Icon-Small@2x.png", "size": 58},
	
	# {"name": "Icon.png", "w": 640 ,"h": 1136},
 #    {"name": "Icon@2x.png", "w": 320,"h": 480},
 #    {"name": "Icon-29.png", "w": 640,"h": 960},
    #{"name": "Icon-29@2x.png", "w": 640,"h": 1136},
   # {"name": "Icon-40@2x.png", "w": 768,"h": 1024},
   # {"name": "Icon-40pad.png", "w": 1536,"h": 2048},
]

android = [
    {"path": "drawable-hdpi", "name": "icon.png", "size": 72},
    {"path": "drawable-ldpi", "name": "icon.png", "size": 32},
    {"path": "drawable-mdpi", "name": "icon.png", "size": 48},
    {"path": "drawable-xhdpi", "name": "icon.png", "size": 96},
    {"path": "drawable-xxhdpi", "name": "icon.png", "size": 144},
	
	{"path": "drawable-57", "name": "icon.png", "size": 57},
    {"path": "drawable-58", "name": "icon.png", "size": 58},
    {"path": "drawable-72", "name": "icon.png", "size": 72},
    {"path": "drawable-76", "name": "icon.png", "size": 76},
    {"path": "drawable-80", "name": "icon.png", "size": 80},
	{"path": "drawable-87", "name": "icon.png", "size": 87},
    {"path": "drawable-100", "name": "icon.png", "size": 100},
    {"path": "drawable-114", "name": "icon.png", "size": 114},
    {"path": "drawable-120", "name": "icon.png", "size": 120},
    {"path": "drawable-144", "name": "icon.png", "size": 144},
	 {"path": "drawable-152", "name": "icon.png", "size": 152},
    {"path": "drawable-167", "name": "icon.png", "size": 167},
    {"path": "drawable-16", "name": "icon.png", "size": 16},
	
	{"path": "drawable-256", "name": "icon.png", "size": 256},
]

if __name__ == "__main__":
    if len(sys.argv)>2:
        if sys.argv[1]=="android":
            if not os.path.exists("android"):
	            os.makedirs("android")
        if sys.argv[1]=="android":
            for info in android:
                if not os.path.exists("android/"+info["path"]):
                    os.makedirs("android/"+info["path"])
                img = Image.open(sys.argv[2])
                out = img.resize((info["size"], info["size"]), Image.ANTIALIAS)
                out.save("android/"+info["path"]+"/"+info["name"])
        elif sys.argv[1]=="ios":
            if not os.path.exists("ios"):
		        os.makedirs("ios")
            if sys.argv[1]=="ios":
                for info in ios:
                    img = Image.open(sys.argv[2])
                    out = img.resize((info["size"], info["size"]), Image.ANTIALIAS)
                    out.save("ios/"+info["name"])
