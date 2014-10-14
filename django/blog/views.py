from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def index(request, offset):
    
    if offset:
        offset = int(offset)
        if offset > 0:
            prev_of = offset - 1
        else:
            prev_of = 'no_prev'
        next_of = offset + 1
    else:
        offset = 0
        prev_of = 'no_prev'
        next_of = 1
    
    actual_blogs = Blog.objects.all().order_by("-posted")[(5*offset):(5*offset+5)]
 
    check_length = 1
    if len(actual_blogs) == 5:
        check_length = 0
    else:
        pass
    
    context = {
        'posts': actual_blogs,
        'prev' : prev_of,
        'next' : next_of,
        'check_length' : check_length
    }
    return render(request, 'blog_index.html', context)

def get_all_pics(blog):
    vysl = []
    for att in dir(blog):
        if str(att).find("pic") != -1 and str(att).find("picd_") == -1 and len(att) != 3:
            pic = getattr(blog, att)
            if getattr(blog, "picd_{0}".format(att[-1])) and pic and pic != "":
                vysl.append([pic, getattr(blog, "picd_{0}".format(att[-1]))])
            elif pic != "":
                vysl.append([pic, ""])
    return(vysl)


def view_post(request, slug):   
    context = { 'post': get_object_or_404(Blog, slug=slug),
                'pics': get_all_pics(get_object_or_404(Blog, slug=slug)),
                }
    return render(request, 'view_post.html', context)
