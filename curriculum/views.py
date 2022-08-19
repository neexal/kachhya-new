from multiprocessing import context
from urllib import request, response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from django.urls import reverse


from base.views import lobby
from .models import Assignment, Standard, Subject, Lesson, Comment, Submission
#  WorkingDays, TimeSlots
from django.urls import reverse_lazy
from .forms import AssignmentForm, CommentForm,ReplyForm, LessonForm, SubmissionForm
from django.http import HttpResponseRedirect

# import base


# def videos(request):
#     return render(request, base/lobby.html)

#for api
from rest_framework.decorators import api_view
from rest_framework.response import Response



class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'

class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/subject_list_view.html'

class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'

class LessonDetailView(DetailView, FormView,):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'
    form_class = CommentForm
    second_form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(request=self.request)
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)
        # print("the form name is : ", form)
        # print("form name: ", form_name)
        # print("form_class:",form_class)

        if form_name=='form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            print("reply form is returned")
            return self.form2_valid(form)


    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_detail',kwargs={'standard':standard.slug,
                                                             'subject':subject.slug,
                                                             'slug':self.object.slug})
    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())



class LessonCreateView(CreateView):
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = LessonForm
    context_object_name = 'subject'
    model= Subject
    template_name = 'curriculum/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,
                                                             'slug':self.object.slug})


    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class LessonUpdateView(UpdateView):
    fields = ('name','position','video','ppt','Notes')
    model= Lesson
    template_name = 'curriculum/lesson_update.html'
    context_object_name = 'lessons'

class LessonDeleteView(DeleteView):
    model= Lesson
    context_object_name = 'lessons'
    template_name = 'curriculum/lesson_delete.html'

    def get_success_url(self):
        print(self.object)
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,'slug':subject.slug})

def viewAssignment(request):
    context = {
        'assignment' : Assignment.objects.all(),
    }
    return render(request, 'curriculum/assignment.html', context)

# class AssignmentListView(DetailView):
#     context_object_name = 'lessons'
#     model = Assignment
#     template_name = 'curriculum/assignment.html'

def viewAssignmentById(request, id):
	context = {
		 'assignment': Assignment.objects.filter(lesson_id = id),
	}
	return render(request, 'curriculum/assignment.html', context)

def createAssignment(request, id):
    # context = {
    #     'id' : id
    # }
    lesson=Lesson.objects.get(lesson_id=id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            new_data=form.save(commit=False)
            new_data.lesson=lesson
            new_data.save()
            # return HttpResponse("<h1>"+"Questions Created"+"</h1>")
            return HttpResponseRedirect("/curriculum")
    else:
            form = AssignmentForm()
            # return HttpResponseRedirect('createAssignment')
        # title = request.POST('title')
        # description = request.POST('description')
        # lesson = id
        # file = request.FILES('fileUpload')
        
        # new_data = Assignment.objects.create(title=title, description=description,lesson=lesson, file=file.url)
        # new_data.save()

    
    return render(request, 'curriculum/createAssignment.html',{'form': form})




def submitAssignment(request, id):
    # context = {
    #     'id' : id
    # }
    assignment=Assignment.objects.get(id=id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            new_data=form.save(commit=False)
            new_data.assignment=assignment
            new_data.save()
            return HttpResponseRedirect("/curriculum")
    else:
            form = SubmissionForm()
            
    return render(request, 'curriculum/submitAssignment.html',{'form': form})









# def createAssignment(request, id):
#     context = {
#         'id' : id
#     }
#     if request.method == 'POST':
#         form = AssignmentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('curriculum/createAssignment.html', context)
#         # else:
#         #     form = AssignmentForm()
#         # return render(request, 'curriculum/createAssignment.html', {
#         # 'form': form
#     # })
#     return render(request, 'curriculum/createAssignment.html', context)

# class CreateAssignment(CreateView):
#     form_class = AssignmentForm
#     context_object_name = 'assignment'
#     extra_context={'lesson': Lesson.objects.filter(lesson_id=id)}
#     model= Assignment
#     template_name = 'curriculum/createAssignment.html'

#     def form_valid(self, form):
#         # lesson = self.kwargs['lesson']
#         # self.object = self.get_object()
#         # 
#         context = {
#                 'id' : id
#         }   
#         fm = form.save(commit=False)
#         # fm.lesson = lesson
#         # fm.lesson = self.object.lesson
#         fm.save()
#         # return HttpResponseRedirect('createAssignment')
#         return render(request, 'curriculum/createAssignment.html', context),

# class SubmitAssignment(CreateView):
#     form_class = SubmissionForm
#     context_object_name = 'submission'
#     model= Submission
#     template_name = 'curriculum/submitAssignment.html'

#     def form_valid(self, form):
#         # assignment = Assignment.objects.get(id=id)
#         # self.object = self.get_object()
#         fm = form.save(commit=False)
#         # fm.assignment=assignment
#         fm.save()
#         return HttpResponseRedirect('submitAnswer')
#         # return render(request, 'curriculum/submitAssignment.html'),


# def search(request):
# 	query = request.GET['query']
# 	context ={
# 		'lessons' : Lesson.objects.filter(name__icontains=query)
# 	}
# 	return render(request, 'curriculum/search.html', context)


