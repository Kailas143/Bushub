from django.shortcuts import get_object_or_404, redirect, render

from .models import Book, Bus, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request, 'busapp/homepage.html')


def findbus(request):
    context = {}
    if request.method == 'POST':
        src_r = request.POST.get('source')
        dest_r = request.POST.get('dest')
        date_r = request.POST.get('date')
        bus_list = Bus.objects.filter(src=src_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request, 'busapp/buslist.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'busapp/findbus.html', context)
    else:
        return render(request, 'busapp/findbus.html')



def booking_list(request):
    context = {}
    if request.method == "POST":
        bus_id = request.POST.get('bus_id')
        no_s = request.POST.get('no_seats')
        bus = get_object_or_404(Bus, id=bus_id)
        if bus:
            if bus.rems > int(no_s):
                bus_name = bus.bus_name
                src_r = bus.src
                dest_r = bus.dest
                date_r = bus.date
                time_r = bus.time
                price_r = bus.price
                nos = no_s
                cost = bus.price * int(no_s)
                user_name = request.user.username
                user_email = request.user.email
                user_id = request.user.id
                rem_r = bus.rems-int(no_s)
                Bus.objects.filter(id=bus_id).update(rems=rem_r)
                booking = Book.objects.create(
                    busid=bus_id,
                    bus_name=bus_name,
                    source=src_r,
                    dest=dest_r,
                    date=date_r,
                    time=time_r,
                    price=price_r,
                    nos=nos,
                    name=user_name, email=user_email, userid=user_id,
                    status='Booked'
                )
                return render(request, 'busapp/bookings.html', locals())
            else:
                context['error'] = 'Sorry seats are not available'
                return render(request, 'busapp/findbus.html', context)
        else:
            context['error'] = 'Bus is not available'
            return render(request, 'busapp/findbus.html', context)
    return render(request, 'busapp/findbus.html')


def seebookings(request, new={}):
    context = {}
    id_r = request.user.id
    booking_list = Book.objects.filter(userid=id_r)
    if booking_list:
        return render(request, 'busapp/bookinglist.html', locals())
    else:
        context['error'] = 'Sorry no bookings'
        return render(request, 'busapp/findbus.html', context)


def cancelling(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('book_id')
        try:
            book = Book.objects.get(id=id_r)
            print(book)
            bus = Bus.objects.get(id=book.busid)
            print(book.nos)
            print(bus.rems)
            rem_r = bus.rems+int(book.nos)
            Bus.objects.filter(id=book.busid).update(rems=rem_r)
            print(bus.rems)
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect('booking:seebookings')
        except Book.DoesNotExist:
            context['error'] = 'Invalid Booking ID'
            return render(request, 'busapp/error.html', context)
    return render(request, 'busapp/findbus.html')


def signup(request):
    context = {}
    if request.method == "POST":
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        number_r = request.POST.get('number')
        if password_r == confirm_password:
            user = User.objects.create(
                username=name_r, password=password_r, email=email_r)
            if user:
                login(request, user)
                return render(request, 'busapp/thank.html')
            else:
                context['error'] = 'Invalid credentials'
                return render(request, 'busapp/signup.html', context)
        else:
            context['error'] = 'Password Mismatch'
            return render(request, 'busapp/signup.html', context)

    return render(request, 'busapp/signup.html')


def signin(request):
    context = {}
    if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user :
                        print(username)
                        login(request, user)
                        return redirect('booking:findbus')
                else:
                        return redirect('booking:signin')
    return render(request,'busapp/login.html',{})



def signout(request):
    context={}
    logout(request)
    context['error']='You are succesfully logged out'
    return render(request,'busapp/login.html',context)
