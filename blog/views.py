from django.shortcuts import render,redirect
from.models import *
# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib import messages




def home(request):
    blogs=blog.objects.all()
    return render(request,'blog/index.html',{'blogs':blogs})


def blog_content(request,slug):
    blog_contents=blog.objects.get(slug=slug)
    profile = blog_contents.user
    catergries=catergry.objects.all()
    commnets=Comments.objects.filter(blog=blog_contents)
    profile.total_view += 1
    profile.save()
    blog_contents.views += 1
    blog_contents.save()
    return render(request,'blog/blog-content.html',{'blog_contents':blog_contents,
                                                    'catergries':catergries,
                                                    'commnets':commnets,})
    

def is_like(request, slug):
    profile=get_object_or_404(Profile,user=request.user)
    blog_contents=blog.objects.get(slug=slug)
    profile = blog_contents.user
    if profile not in blog_contents.likes.all():
        blog_contents.likes.add(profile)
        blog_contents.count_likes += 1
        profile.total_likesr += 1
        profile.save()
        blog_contents.save()
    return redirect('/')
    
    
    
def add_comment(request,slug):
    profile=get_object_or_404(Profile,user=request.user)
    blog_contents=get_object_or_404(blog,slug=slug)
    if 'message' in request.POST:
        message = request.POST['message']
        comment=Comments.objects.create(
                                user=profile,
                                blog=blog_contents,
                                comment=message,
                                )
        comment.save()
        return redirect('/' + blog_contents.slug)
    
    
def blog_user(request,slug):
    profile=get_object_or_404(Profile,slug=slug)
    blogs=blog.objects.filter(user=profile)
    return render(request,'blog/blog-user.html',{'blogs':blogs,
                                                'profile':profile})
    
def is_like_blog(request, slug):
    profile=get_object_or_404(Profile,user=request.user)
    blog_contents=blog.objects.get(slug=slug)
    profile = blog_contents.user
    if profile not in blog_contents.likes.all():
        blog_contents.likes.add(profile)
        blog_contents.count_likes += 1
        profile.total_likesr += 1
        profile.save()
        blog_contents.save()
    return redirect('/blog/' + blog_contents.user.slug)



def add_follow(request, slug):
    profile=get_object_or_404(Profile,user=request.user)
    profile_to_follow=get_object_or_404(Profile,slug=slug)
    profile_to_follow.follower.add(profile.user)
    profile_to_follow.count_follower += 1
    profile_to_follow.save()
    return redirect('/blog/' + profile_to_follow.slug)


def un_follow(request, slug):
    profile=get_object_or_404(Profile,user=request.user)
    profile_to_follow=get_object_or_404(Profile,slug=slug)
    profile_to_follow.follower.remove(profile.user)
    profile_to_follow.count_follower -= 1
    profile_to_follow.save()
    return redirect('/blog/' + profile_to_follow.slug)


def all_user(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.filter(blog__isnull=False).exclude(user=request.user).distinct()
    else:
        profiles = Profile.objects.all()
    return render(request,'blog/all-user.html',{'profiles':profiles,})



from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class Upload_post(LoginRequiredMixin,CreateView):
    model=blog
    fields=['title','text','img','catergryy',]
    template_name='blog/upload_post.html'
    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super(Upload_post,self).form_valid(form)
    def get_success_url(self):
        return reverse_lazy('blog:blog_user', kwargs={'slug': self.kwargs['slug']})