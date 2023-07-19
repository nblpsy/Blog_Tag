from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import View
from .models import Blog, Category, Comment
from .forms import CommentCreateForm, NewBlogForm
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         queryset = Blog.objects.order_by('-id')
#         return render(request, 'blog/index.html', {
#             'blog': 
#         })


class IndexView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    
    def get_queryset(self):
        queryset = Blog.objects.order_by('-id')
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentCreateForm
        return context


class NewBlogView(CreateView):
    template_name = 'blog/create.html'
    form_class = NewBlogForm
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class CategoryView(ListView):
    model = Blog
    template_name = 'blog/index.html'

    def get_queryset(self):
        category = Category.objects.get(name=self.kwargs['category'])
        queryset = Blog.objects.order_by('-id').filter(category=category)
        return queryset
# categoryの

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_key'] = self.kwargs['category']
        context['comment_form'] = CommentCreateForm
        return context
# contextとしてindex.htmlで{{ category_key }}のように変数として持っていくことができる


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        blog_pk = self.kwargs.get('pk')
        blog = get_object_or_404(Blog, pk=blog_pk)
        comment = form.save(commit=False)
        comment.target = blog
        comment.save()

        return redirect('blog:detail', pk=blog_pk)
