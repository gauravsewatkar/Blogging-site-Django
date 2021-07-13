from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# my HTML pages
def home(request):
     
    return render (request , 'home/home.html')

def about(request):
    return render (request , 'home/about.html')
 
def contact(request):
    
    if request.method=='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']

        if len(name)<2 or len(phone)<10 or len(email)<5 or len(content)<5:
            messages.error(request,'Fill the form correctly')
        else:    
            contact = Contact(name=name , phone=phone , email = email , content=content)
            contact.save()
            messages.success(request,'Your message has been send successfully')

    return render (request , 'home/contact.html')
 
def search(request):
    query = request.GET['query']
    if len(query) >70:
        allposts = Post.objects.none()
    else:
        #allposts= Post.objects.all()
        allpostsTitle= Post.objects.filter(title__icontains=query)
        allpostContent= Post.objects.filter(content__icontains=query)
        allposts= allpostsTitle.union(allpostContent)
    if allposts.count()==0:
        messages.warning(request,'No search results found. please refine your query')
    params= {'allposts': allposts , 'query':query}
    return render(request,'home/search.html', params) 




        #Auth APIs




#authentication API

def handleSignup(request):
    if request.method == 'POST':
        #GET all parameters
        username  = request.POST['username']
        first_name= request.POST['first_name']  
        last_name = request.POST['last_name']
        email     = request.POST['email']  
        pass1     = request.POST['pass1']    
        pass2     = request.POST['pass2'] 

        #checking errorness

        #under 10 character username
        if len(username) > 10 :
            messages.error(request,'Please enter username under 10 character')
            return redirect('home')

        #username should be alphanumeric
        if not username.isalnum() :
            messages.error(request,'username should contain letters and numbers')
            return redirect('home')
    
        #password confirmation
        if pass1 != pass2 :
            messages.error(request,'Password does not match')
            return redirect('home')
 
        #create user
        myuser = User.objects.create_user(username , email ,pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        messages.success(request,'Your account has been Successfully created')
        return redirect('home')
 
    else:
        return HttpResponse('404 -not found')          
    
 
def handleLogin(request):
    if request.method == 'POST':
        #GET all parameters
        loginusername  = request.POST['loginusername']
        loginpass = request.POST['loginpass']  

        user = authenticate (username= loginusername , 
        password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request,'successfully logged in')
            return redirect ('home')
        else:
            messages.error(request,'invalid credentials') 
            return redirect ('home')    
 
    return HttpResponse('404 -not found')

 
def handleLogout(request): 
    logout(request)
    messages.success(request,'Successfully Log out')
    return redirect('home')  
    return HttpResponse('handleLogout') 



