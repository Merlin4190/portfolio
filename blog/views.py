from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.text import slugify
from .models import Post, Category, PostImg
from .forms import CommentForm, PostForm, PostImgForm, inlineformset_factory, PostImgFormset

# Create your views here.

@login_required
def post_new(request):
  cats = Category.objects.all()

  if request.method == 'POST':
    post_form = PostForm(request.POST)
    post_img_form = PostImgForm(request.POST, request.FILES, instance=PostImg())

    if post_form.is_valid() and post_img_form.is_valid():
      post = post_form.save(commit=False)
      post.slug = slugify(post.title)
      # post.created_on = timezone.now()
      post.save()
      post_form.save_m2m()

      post_img_form = PostImgForm(request.POST, request.FILES, instance=PostImg())
      post_img = post_img_form.save(commit=False)
      post_img.post = post 
      post_img.save()

      return redirect('post_detail', slug=post.slug)

  else:
    post_form = PostForm()
    post_img_form = PostImgForm()
  return render(request, 'blog/post_form.html', {'post_form':post_form, 'post_img_form':post_img_form, 'categories': cats})

@login_required
def post_edit(request, slug):
  cats = Category.objects.all
  post = get_object_or_404(Post, slug=slug)
  PostImgFormset = inlineformset_factory(Post, PostImg, fields=('image',), extra=0, can_delete=False)
  post_img_form = PostImgForm(request.POST, request.FILES, instance=PostImg())
  if request.method == 'POST':
    post_form = PostForm(request.POST, instance=post)
    post_img_form = PostImgFormset(request.POST, request.FILES, instance=post)
    if post_form.is_valid() and post_img_form.is_valid():
      post = post_form.save(commit=False)
      post.slug = slugify(post.title)
      post.created_on = timezone.now()
      post.save()
      post_form.save_m2m()
      post_img_form.save()

      return redirect('post_detail', slug=post.slug)
  else:
    post_form = PostForm(instance=post)
    post_img_form = PostImgFormset(instance=post)
  return render(request, 'blog/post_form.html', {'post_form':post_form, 'post_img_form':post_img_form, 'categories': cats})

def post_list(request):
  posts = Post.objects.all()
  cats = Category.objects.all()
  # cat_rows = ",".join(str(cat.title) for cat in posts.categories.all())

  context = {'posts': posts[:5], 'categories': cats }
  return render(request, 'blog/index.html', context)

@login_required
def post_draft_list(request):
  cats = Category.objects.all()
  posts = Post.objects.filter(status=0).order_by('created_on')
  return render(request, 'blog/post_draft_list.html', {'posts': posts, 'categories': cats})

@login_required
def post_publish(request, slug):
  post = get_object_or_404(Post, slug=slug)
  post.publish()
  return redirect('post_detail', slug=slug)

def post_detail(request, slug):
  template_name = 'blog/post_detail.html'
  post = get_object_or_404(Post, slug=slug)
  comments = post.comments.filter(active=True)
  new_comment = None

  # Comment posted
  if request.method == 'POST':
    comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
      # Create Comment Object but don't save to datatbase yet
      new_comment = comment_form.save(commit=False)
      # Assign the current post to the comment
      new_comment.post = post
      # Save the comment to the datatbase
      new_comment.save()

  else:
    comment_form = CommentForm()

  return render(request, template_name, {'post': post,
    'comments': comments, 'new_comment': new_comment,
    'comment_form': comment_form, 'categories': Category.objects.all()

  })

@login_required
def post_delete(request, slug):
  post = get_object_or_404(Post, slug=slug)
  post.delete()
  return redirect("")

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def category_list(request, slug):
  posts = Post.objects.filter(
      categories__slug__contains=slug
  ).order_by('-created_on').distinct()

  categories = Category.objects.all()
  cat_row = Category.objects.filter(slug=slug)

  context = {'slug': slug, 'cat': cat_row, 'posts': posts, 'categories': categories }
  return render(request, 'blog/category_detail.html', context)

