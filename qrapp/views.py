from django.shortcuts import render
import qrcode


# Create your views here.

def home(request):
    if request.method =='POST':
        link = request.POST.get("link")


        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
        qr.add_data(link)
        qr.make(fit=True)


        img = qr.make_image(fill_color="black", back_color="white")


        img.save('qrcode.png')
        img.show()

    
    return render(request , "index.html")


    


