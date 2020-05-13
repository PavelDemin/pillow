from PIL import Image, ImageDraw, ImageFont
import sys
 
try:
    tatras = Image.open("template.jpg")
except:
    print("Unable to load image")
    sys.exit(1)
    
idraw = ImageDraw.Draw(tatras)
BTC_price = "$8909.11"
BTC_change = "+6.68%"
ETH_price = "$190.43"
ETH_change = "-0.94%"

RIPPLE_price = "$0.25"
RIPPLE_change = "+1.67%"
BINANCE_price = "$18.33"
BINANCE_change = "-12.94%"
 
font = ImageFont.truetype("fonts/Ubuntu-Regular.ttf", size=62)
 
idraw.text((800, 140), BTC_price, font=font)
idraw.text((1200, 140), BTC_change, font=font, fill=(0,190,0,255))
idraw.text((800, 390), ETH_price, font=font)
idraw.text((1200, 390), ETH_change, font=font, fill=(190,0,0,255))
idraw.text((800, 640), RIPPLE_price, font=font)
idraw.text((1200, 640), RIPPLE_change, font=font, fill=(0,190,0,255))
idraw.text((800, 890), BINANCE_price, font=font)
idraw.text((1200, 890), BINANCE_change, font=font, fill=(190,0,0,255))
 
tatras.save('wonwa.jpg')