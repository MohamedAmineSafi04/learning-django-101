# from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView, FormView
from .forms import PostForm
from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"
    def form_valid(self, form):
        # Create new Post
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        # print(form.cleaned_data['text'])
        return super().form_valid(form)