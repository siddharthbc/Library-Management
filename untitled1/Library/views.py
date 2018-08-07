from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.db import models
from django.db.models import Q
from .models import *
from datetime import datetime
def index(request):
    form = loginForm(request.POST or None)
    all_books = Book.objects.all()
    # template= loader. get_template('dbms/index.html')
    context = {'all_books': all_books, 'form':form}
    # return HttpResponse(template.render(context, request))
    return render(request, 'Library/welcome.html', context)

def book_borrowed(request):
    if not request.user.is_authenticated():
        redirect('login1')
    else:
        book_instances = BookInstance.objects.all()
        return render(request,'Library/borrow.html',{'book_instances':book_instances})

def welcome(request):
    all_books = Book.objects.all()
    for b in all_books:
        book = b
    context = {'all_books': all_books,'book':book}
    return render(request, 'Library/welcome.html', context)
from django.db.models import Avg

from .models import *
def detail(request, isbn):
    books = get_object_or_404(Book, pk=isbn)
    bo_is = book_issue.objects.filter(book= books)
    requested = 0
   # bo_inst = book_issue.objects.get()
    for bo in bo_is:
        if bo.user == request.user:
            requested = 1
            bo_inst = book_issue.objects.get(pk=bo.id)
    user_feedback = feedback.objects.filter(book=books)
    i=0
    num = 0
    for feedbacks in user_feedback:
        i=i+1
        num =num + feedbacks.rating
    if i ==0:
        num = 5
    else:
        num = num / i
    if num < 1:
        num = 1
    if requested:
        if bo_inst.book_issued == "is":
            return render(request, 'Library/detail.html', {'book': books,'borrow':'You borrowed','num':num})
        elif bo_inst.book_issued == "re":
            bo_inst.delete()
            return render(request,'Library/detail.html',{'book':books ,'reject':'Rejected','num':num})
        elif bo_inst.book_issued == "Pe":
            return render(request,'Library/detail.html',{'book':books ,'pending':'pending','num':num})
    else:
        return render(request, 'Library/detail.html', {'book': books,'requested':'Not requested','num':num})



def signup(request):
    form = signupForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = request.POST['first_name']
        emailid = request.POST['email']
        password = request.POST['password']
        #contact_no = request.POST['contact_no']
        user = User.objects.create_user(username=username, email=emailid, password=password)
        user.set_password(password)
        user.save()
        user = authenticate(email=emailid, password=password)
        if user is not None:
            login(request,user)
            all_books=Book.objects.all()
            redirect('login1')
        return redirect('login1')
        #return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'Library/sign.html', context)

def issue_books(request):
    if request.user.is_superuser:
        book = book_issue.objects.filter(book_issued="Pe").distinct()
        if book:
            return render(request,'Library/borrow_approval.html',{ 'book' : book })
        else:
            return render(request,'Library/borrow_approval.html',{ 'error_message':'No books requested' })
    else:
        return redirect('home')


def book_accept(request,isbn):
    book_iss = get_object_or_404(book_issue,pk=isbn)
    book_iss.book_issued = 'is'
    book_iss.book.number_of_books = book_iss.book.number_of_books - 1
    book_iss.book.save()
    book_iss.save()
    return redirect('issue_books')

def book_reject(request,isbn):
    book_iss = get_object_or_404(book_issue,pk=isbn)
    book_iss.book_issued = 're'
    book_iss.save()
    return redirect('issue_books')

def login_user(request):
    err = 'enter'
    form = loginForm(request.POST)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
       # user_type = Users.objects.get(User=request.user)
      #  type = user_type.get_user_type()
        if user is not None:
            if user.is_active:

                login(request, user)
                all_books = Book.objects.all()
                context = {'all_books': all_books}
                # print(request.user.username)
                return redirect('welcome')
            else:
                return render(request, 'Library/login1.html', {'error_message': 'Your account has been disabled'})
        else:
            # print('invalid user')
            return render(request, 'Library/login1.html', {'form': form,'error_message': 'invalid username or password'})
    else:
        context = {
            'form': form,
        }
        return render(request, 'Library/login1.html', context, {'error_message': err})

def logout_user(request):
    logout(request)
    return redirect('home')

def borrowed_books(request):
    if request.user.is_authenticated:
        book_is = book_issue.objects.filter(user = request.user).distinct()

        if book_is:
            return render(request,'Library/books.html',{'book_is':book_is})
        else:
            return render(request,'Library/books.html',{'book':'book','error_message':'You have not borrowed any books'})
    else:
        redirect('login1')

def fine(request):
    if request.user.is_authenticated:
        fine = Fine.objects.filter(user=request.user)
        if fine:
            return render(request,'Library/fine.html',{'fine':fine})
        else:
            return render(request,'Library/fine.html',{'error_message':'You have not borrowed any books'})
    else:
        redirect('login1')




def search(request):
    if not request.user.is_authenticated():
        form = loginForm()
        return render(request,'Library/login1.html',{'error_message':'Please Login','form':form})
    else:
        # = Album.objects.filter(user=request.user)
        book_results = Book.objects.all()
        query = request.GET.get("q")
        if query:
            all_books = book_results.filter(
                Q(title__contains=query)
            ).distinct()
            return render(request, 'Library/search.html', { 'all_books': all_books })
        else:
            return redirect('index')

def borrow(request,isbn):
    if request.user.is_authenticated:
        book = get_object_or_404(Book , pk=isbn)
        if book.number_of_books == 0:
            return render(request, 'Library/limit.html',
                          {'error_message': 'Book not available'})
        book.request_user=request.user
        count  = book_issue.objects.filter(user=request.user).count()
        if  count == book.number_of_books :
            return render(request,'Library/limit.html',{'error_message':'Oops you reached your maximum borrow limit'})
        book_bo = book_issue.create()
        book_bo.book = book
        book_bo.user=request.user
        book_bo.datetime = datetime.now()
        book_bo.book_issued="Pe"
        book_bo.save()
        request.session['message'] = True
        return redirect('detail',isbn)
    else:
        redirect('login1')

def book_return(request,isbn):
    book = get_object_or_404(Book, pk=isbn)
    book_is = get_object_or_404(book_issue, book=book)
    a = book_is.calculate()
    book.number_of_books = book.number_of_books + 1
    book.save()
    fine = 10 * a
    actual_date = book_is.datetime
    return_date = datetime.now()
   # if return_date < 13 and return_date > 0:
      #  return_date = return_date
   # elif return_date >12:
    #    return_date = return_date - 12
    #elif return_date == 0:
     #   return_date =12
    #return_date_minute = book_is.datetime.minute + 1
    book_is.delete()
    print (fine)
    if fine == 0:
        form = FeedbackForm(request.POST or None)
        return render(request, 'Library/feedback.html', {'form': form, 'isbn': book.id})

    fine_object = Fine.create()
    fine_object.user = request.user
    fine_object.book = book
    fine_object.fine = fine
    fine_object.save()
    return render(request, 'Library/penalty.html', {
                                                    'return_date': return_date, 'actual_date': actual_date,
                                                    'fine': fine, 'book': book,'fine_object':fine_object,
                                                    })

from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def download(request,fine):
    template = get_template('Library/download.html')



def invoice(reqeuest,isbn):
    feedback_use = get_object_or_404(feedback,pk=isbn)
    return render(reqeuest,'Library/invoice.html',{'feedback_use':feedback_use})

def add_feedback (request,isbn):
    form = FeedbackForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            feedback_a = form.save(commit=False)
            feedback_a.user= request.user
            book = get_object_or_404(Book,pk=isbn)
            feedback_a.book = book
            feedback_a.save()
            return redirect('welcome')
        else:
            return render(request,'Library/feedback.html',{'form':form,'isbn':isbn})
    else:
        return render(request,'Library/feedback.html',{'form':form,'isbn':isbn})

def books_all(request):
    all_books = Book.objects.all()
    return render(request,'Library/all_books.html',{'all_books':all_books})




def home(request):
    return render(request,'Library/home.html')

def create_feedback(request,isbn):
    if not request.user.is_authenticated():
        return render(request, 'Library/login.html',{'error_message':"You must login to give feedback"})
    else:
        form = FeedbackForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            book = get_object_or_404(Book,pk=isbn)
            feedback.book =book
            feedback.save()
            return render(request, 'Library/home.html')
    context = {'form': form}
    return render(request, 'Library/give_feedback.html', context)