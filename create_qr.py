
import qrcode

img = qrcode.make('https://zeno.fm/noti-importa/')
f = open("qr_gibaloshouse.png",'wb')
img.save(f)
f.close()
