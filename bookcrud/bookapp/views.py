from django.shortcuts import render,HttpResponse,redirect
from bookapp.models import Book          

# Create your views here.
def homepage(request):
    #feching the data
    data=Book.objects.all()            
    context={}
    context['books']=data          
    return render(request,'home.html',context)

def addbook(request):
    if request.method=='GET':
        return render(request,'addbook.html')
    else:
        #fetch data
        t=request.POST['title']
        a=request.POST['author']
        p=request.POST['price']


        #insert the row in database
        b=Book.objects.create(title=t,author=a,price=p)
        b.save()
        print(t,a,p)
        #return render(request,'home.html')
        #we need to execute homepage fun but we cant
        return redirect('/home')                      

def deletebook(request,bookid):
    #print("delete book id ",bookid)
    b=Book.objects.filter(id = bookid)                                                    #where(condition)=(id=bookid)
    b.delete()
    #return render(request,'home.html')
    return redirect('/home')

def updatebook(request,bookid):
   if request.method=='GET':
       print("update book id : ",bookid)
       b=Book.objects.filter(id=bookid)
       print(b[0].title)
       context={}
       context['book']=b[0]
       return render(request,'updatebook.html',context)
   else:
       #fetch data
        t=request.POST['title']
        a=request.POST['author']
        p=request.POST['price']
        b=Book.objects.filter(id=bookid)   #fetch the book object based on id
        b.update(title=t,author=a,price=p)  #update will update all the books in b with new t,a,p
        return redirect('/home')
   
    
    
    