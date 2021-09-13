
import qrcode

img = qrcode.make('https://patinronin.github.io/my_cv_page/')
f = open("qr_my_git_hub_page.png",'wb')
img.save(f)
f.close()
