from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category, Faculty
from .forms import PostForm,EditForm
from django.urls import reverse_lazy


def contextGenerator(request, *args, **kwargs):
    
    data = {
        'faculties' : Faculty.objects.all(),
    }
    
        
    
    for a in args:
        data[a] = a
    
    for k in kwargs:
        data[k] = kwargs[k]
    
    return data      
    

    
    

class tazelikView(ListView):
    model = Post
    template_name = 'engine/post_list.html'
    ordering = ['-post_date']
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'engine/article_detail.html'
    

class addView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'engine/add_post.html'
    #fields = '__all__'
    
class addcategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'engine/add_category.html'
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'engine/update_post.html'
    #fields = ['title','body']
    
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'engine/delete_post.html'
    success_url = reverse_lazy('engine:tazelik')
    
    
class BlogSearchView(ListView):
    model = Post
    template_name = 'engine/post_list.html'
    ordering = ['-post_date']
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(title__icontains = query).order_by('-post_date')
        
    

def homeView(request):
    return render(request,'engine/index.html', contextGenerator(request))

def navbarView(request):
    return render(request,'engine/navbar.html',contextGenerator(request))

def sideView(request):
    return render(request,'engine/sidebar.html',contextGenerator(request))

def dashboardView(request):
    
    return render(request,'engine/dashboard.html', contextGenerator(request))

def aboutView(request):
    return render(request,'engine/about.html',contextGenerator(request))

def yaglarView(request):
    return render(request,'engine/yaglar.html',contextGenerator(request))

def aspiranturaView(request):
    return render(request,'engine/aspirant.html',contextGenerator(request))

def hunarmenView(request):
    return render(request,'engine/hunarmen.html',contextGenerator(request))

def bakalawr(request):
    return render(request,'engine/bakalawr.html',contextGenerator(request))

def maslahatlar(request):
    return render(request,'engine/maslahat.html',contextGenerator(request))


def reyting(request):
    return render(request,'engine/reyting.html',contextGenerator(request))

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category = cats.replace('-',' '))
    return render(request,'engine/categories.html', contextGenerator(request, cats = cats.title().replace('-',' '), category_posts = category_posts))

def HabarlasmakView(request):
    return render(request,'engine/habarlasmak.html',contextGenerator(request))

def faculty_details(request, ID):
    faculty = Faculty.objects.get(id = ID)
    return render(request,'engine/faculty.html',contextGenerator(request, faculty = faculty))
    