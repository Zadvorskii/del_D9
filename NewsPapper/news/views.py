from .models import *
from django.shortcuts import render
from .filters import PostFilter
from django.views.generic import *
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required



class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()



class PostView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    ordering = ['-heading']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        context['category'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        # берём значения для нового товара из POST-запроса, отправленного на сервер
        heading = request.POST['heading']
        #quantity = request.POST['quantity']
        #category = request.POST['category']
        #price = request.POST['price']

        post = Post(name=heading)  # создаём новый товар и сохраняем
        post.save()
        return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


@login_required
def subscribe(request, **kwargs):
    user = request.user
    cat_id = kwargs['pk']
    category = Category.objects.get(pk=int(cat_id))

    if user not in category.subscribers.all():
        category.subscribers.add(user)

    else:
        category.subscribers.remove(user)

    return redirect(request.META.get('HTTP_REFERER', '/'))

"""def Post_list(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'post.html', {'filter': f})"""
