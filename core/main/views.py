from django.shortcuts import render, redirect
from .models import Header, Home, HomeContent, About, WorkProces, WorkProcessContent, Testimonial, TestimonialContent
from .models import PricingPlan, PricingPlanOffer, PricingPlanContent, BlogEntries, BlogEntriesContent, ContactGet, ContactPost, Footer
from .forms import ContactModelForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            ContactPost.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactModelForm()
    header = Header.objects.all()[0]
    home = Home.objects.all()[0]
    home_content = HomeContent.objects.all()
    about = About.objects.all()[0]
    work_process = WorkProces.objects.all()[0]
    work_process_content = WorkProcessContent.objects.all()
    testimonial = Testimonial.objects.all()[0]
    testimonial_content = TestimonialContent.objects.all()
    pricing_plan = PricingPlan.objects.all()[0]
    pricing_plan_offer = PricingPlanOffer.objects.all()
    pricing_plan_content = PricingPlanContent.objects.all()
    blog_entries = BlogEntries.objects.all()[0]
    blog_entries_content = BlogEntriesContent.objects.all()
    contact_get = ContactGet.objects.all()[0]
    footer = Footer.objects.all()[0]

    return render(request, 'index.html', context={
        'header':header,
        'home':home,
        'home_content':home_content,
        'about':about,
        'work_process':work_process,
        'work_process_content':work_process_content,
        'testimonial':testimonial,
        'testimonial_content':testimonial_content,
        'pricing_plan':pricing_plan,
        'pricing_plan_offer':pricing_plan_offer,
        'pricing_plan_content':pricing_plan_content,
        'blog_entries':blog_entries,
        'blog_entries_content':blog_entries_content,
        'contact_get':contact_get,
        'footer':footer,
    })