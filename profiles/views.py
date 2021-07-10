from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from .models import Profile, Post, Comment
from django.urls import reverse_lazy
from .forms import RegisterUserForm, ChangeUserInfoForm, PostForm, UserCommentForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def home(request):
    all_posts = Post.objects.all()
    return render(request, 'layout/basic.html', {'all_posts': all_posts})


class MoonLoginView(LoginView):
    template_name = 'main/login.html'


class RegisterUserView(CreateView):
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user.pk)
    return render(request, 'main/profile.html', {'posts': posts})


class MoonLogoutView(LogoutView, LoginRequiredMixin):
    template_name = 'main/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


@login_required
def profile_post_add(request):
    erorr = ''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:profile')
        else:
            erorr = 'Не верно введеные даные'
    else:
        form = PostForm(initial={'author': request.user.pk})
    context = {'form': form, 'erorr': erorr}
    return render(request, 'main/profile_post_add.html', context)


def alluser(request):
    search_query = request.GET.get('search', '')
    if search_query:
        all_user = Profile.objects.filter(username=search_query)
    else:
        all_user = Profile.objects.all()
    return render(request, 'main/alluser.html', {'all_user': all_user})


def detail(request, post_pk, author):
    authorr = Profile.objects.get(username=author)
    post = Post.objects.filter(id=post_pk)
    comments = Comment.objects.filter(post_id=post_pk)
    erorr = ''
    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Комментарий добавлен')
        else:
            erorr = 'Не верно введеные даные'
    else:
        form = UserCommentForm(initial={'post': post_pk, 'author': request.user.pk})
    context = {'form': form, 'erorr': erorr, 'post': post, 'authorr': authorr, 'comments': comments}
    return render(request, 'main/detail.html', context)


def main_for_all(request, pk):
    userr = Profile.objects.filter(id=pk)
    posts = Post.objects.filter(author_id=pk)
    return render(request, 'main/main_for_all.html', {'posts': posts,'userr': userr})
