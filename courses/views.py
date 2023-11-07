

from django.shortcuts import render, HttpResponse
from django.views import View
from courses.forms import LectureForm, EmbedLectureForm, DocumentForm, PdfForm

from users.models import CustomUser
from courses.models import Lecture, EmbedLecture, Document, Pdf, Course
from Sharma_Academy import settings

# Create your views here.


class LectureView(View):

    """ Lecture create for courses """

    form_class = LectureForm
    template_name = "courses/addLecture.html"

    def get(self, request, *args, **kwargs):
        lecture_form = self.form_class()
        return render(request, self.template_name, {'lecture_form' : lecture_form})
    
    def post(self, request, *args, **kwargs):

        lecture_form = self.form_class(request.POST)
        user = request.user

        if user.type == 'instructor':
            lecture_form = LectureForm(request.POST, request.FILES)
            if lecture_form.is_valid():
                lecture_form.save()
                return HttpResponse('added')
            else:
                return HttpResponse('not added')
        else:
            return HttpResponse('not instructor')
        

class EmbedLectureView(View):

    """ EmbedLecture create for courses """

    form_class = EmbedLectureForm
    template_name = "courses/addEmbedLecture.html"

    def get(self, request, *args, **kwargs):
        embed_form = self.form_class()
        return render(request, self.template_name, {'embed_form' : embed_form})
    
    def post(self, request, *args, **kwargs):

        embed_form = self.form_class(request.POST)
        user = request.user

        if user.type == 'instructor':
            embed_form = EmbedLectureForm(request.POST, request.FILES)
            if embed_form.is_valid():
                embed_form.save()
                return HttpResponse('added')
            else:
                return HttpResponse('not added')
        else:
            return HttpResponse('not instructor')

class DocumentView(View):

    """ Documentation create for courses """

    form_class = DocumentForm
    template_name = "courses/addDocument.html"

    def get(self, request, *args, **kwargs):
        document_form = self.form_class()
        return render(request, self.template_name, {'document_form' : document_form})
    
    def post(self, request, *args, **kwargs):

        document_form = self.form_class(request.POST)
        user = request.user

        if user.type == 'instructor':
            document_form = DocumentForm(request.POST, request.FILES)
            if document_form.is_valid():
                document_form.save()
                return HttpResponse('added')
            else:
                return HttpResponse('not added')
        else:
            return HttpResponse('not instructor')


class PdfView(View):

    """ Pdf create for courses """

    form_class = PdfForm
    template_name = "courses/addPdf.html"

    def get(self, request, *args, **kwargs):
        pdf_form = self.form_class()
        return render(request, self.template_name, {'pdf_form' : pdf_form})
    
    def post(self, request, *args, **kwargs):

        pdf_form = self.form_class(request.POST)
        user = request.user

        if user.type == 'instructor':
            pdf_form = PdfForm(request.POST, request.FILES)
            if pdf_form.is_valid():
                pdf_form.save()
                return HttpResponse('added')
            else:
                return HttpResponse('not added')
        else:
            return HttpResponse('not instructor')


class ShowLectureView(View):
    template_name = "courses/showLectures.html"

    def get(self, request, *args, **kwargs):
        upload_video = Lecture.objects.all()
        embed_video = EmbedLecture.objects.all()
        document = Document.objects.all()
        files = Pdf.objects.all()
        return render(request, self.template_name, {'upload_video' : upload_video,
                                                     'embed_video' : embed_video,
                                                     'document' : document,
                                                     'files': files})
    

class ShowCourseView(View):
    template_name = "courses/showCourses.html"

    def get(self, request, *args, **kwargs):
        course = Course.objects.get(id = self.kwargs['pk'])
        stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, self.template_name, {'course' : course, 
                                            'stripe_publishable_key':stripe_publishable_key})
    


        