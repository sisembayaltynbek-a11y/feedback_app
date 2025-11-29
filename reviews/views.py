from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.views import View
# from .forms import Review_form
from django.views import View
from .models import ReviewTable
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView,DeleteView
from django.http import HttpResponseRedirect

class ReviewView(CreateView):
    model = ReviewTable
    fields = "__all__"    
    template_name = "reviews/index.html"    
    success_url = "/thank"


    # ----------FormView job
    # class ReviewView(FormView):
    # form_class = Review_form
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


    # def get(self, request):
    #     form = Review_form()
    #     model = ReviewTable()
    #     return render(request, "reviews/index.html",{
    #     'form':form,
    #     'model':model
    #     })
    # def post(self,request):
    #     if request.method == "POST":
    #         form = Review_form(request.POST, request.FILES)
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect('/thank/')        
    #     form = Review_form()
    #     model = ReviewTable()
    #     return render(request, "reviews/index.html",{
    #     'form':form,
    #     'model':model
    #     })
        
class ThankYou(TemplateView):
    template_name = "reviews/thanks.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Finished"
        return context

class ListReviews(ListView):
    template_name = "reviews/listreviews.html"
    model = ReviewTable
    context_object_name = "reviews"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["reviews"] = ReviewTable.objects.all()
    #     return context 

class SingleReview(DetailView):
    template_name = "reviews/singlereview.html"
    model = ReviewTable
    context_object_name = 'review'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_id = self.object.id
        liked_id = self.request.session.get('liked_id')
        context['is_liked'] = str(loaded_id) ==liked_id
        # print(context)
        # context['is_active'] = self.object.is_active  # if is_active is a field on your model
        return context


class DeleteReview(DeleteView):
    template_name = "reviews/singlereview.html"
    model = ReviewTable
    context_object_name = 'review'

class AddLikeView(View):
    def post(self,request):
        liked_id = request.POST['liked_id']
        request.session["liked_id"] = liked_id
        return HttpResponseRedirect('/listreviews/'+liked_id)

# ratings = [1,2,3,4,5]
# # Create your views here.
# def index(request):
#     if request.method == "POST":
#         form = Review_form(request.POST)
#         if form.is_valid():
#             form.save()
                # review = ReviewTable(
                #     user_name = form.cleaned_data['user_name'],
                #     review_text = form.cleaned_data['review_text'],
                #     rate = form.cleaned_data['rating']
                # )  # For debugging
#             # review.save()
#             return HttpResponseRedirect('/thanks-page')
#     else:
#         form = Review_form()
#         model = ReviewTable()
#         return render(request, "reviews/index.html",{
#         'form':form,
#         'model':model
#         })
    # ------------------------------------------------------
    #     username = request.POST['username']
    #     if username =="":
    #         return render(request, "reviews/index.html", {
    #             'is_valid':True,
    #             # 'ratings':ratings
    #         })
    #     return HttpResponseRedirect('/thanks-page')
    # return render(request, "reviews/index.html", {
    #     "is_valid":False,
    #     # 'ratings':ratings