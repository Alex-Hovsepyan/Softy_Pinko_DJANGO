from django.contrib import admin
from .models import Header, Home, HomeContent, About, WorkProces, WorkProcessContent, Testimonial, TestimonialContent
from .models import PricingPlan, PricingPlanOffer, PricingPlanContent, BlogEntries, BlogEntriesContent, ContactGet, ContactPost, Footer
# Register your models here.

admin.site.register(Header)
admin.site.register(Home)
admin.site.register(HomeContent)
admin.site.register(About)
admin.site.register(WorkProces)
admin.site.register(WorkProcessContent)
admin.site.register(Testimonial)
admin.site.register(TestimonialContent)
admin.site.register(PricingPlan)
admin.site.register(PricingPlanOffer)
admin.site.register(PricingPlanContent)
admin.site.register(BlogEntries)
admin.site.register(BlogEntriesContent)
admin.site.register(ContactGet)
admin.site.register(ContactPost)
admin.site.register(Footer)