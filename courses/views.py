

from django.shortcuts import render, HttpResponse
from django.views import View
from courses.forms import LectureForm

from users.models import CustomUser
from courses.models import Lecture


# Create your views here.


class LectureView(View):
    form_class = LectureForm
    template_name = "courses/courses.html"

    def get(self, request, *args, **kwargs):
        lecture_form = self.form_class()
        return render(request, self.template_name, {'lecture_form' : lecture_form})
    
    def post(self, request, *args, **kwargs):

        lecture_form = self.form_class(request.POST)

        uploader = request.POST.get('upload_by')
        uploader_obj = CustomUser.objects.get(id = uploader)

        if uploader_obj.user_type == 'instructor':
            lecture_form = LectureForm(request.POST, request.FILES)
            if lecture_form.is_valid():
                lecture_form.save()
                return render(request, self.template_name, {'lecture_form' : lecture_form})
            else:
                return HttpResponse('not added')
        else:
            return HttpResponse('not instructor')
        

class ShowLectureView(View):
    template_name = "courses/lectures.html"

    def get(self, request, *args, **kwargs):
        upload_video = Lecture.objects.all()
        return render(request, self.template_name, {'upload_video' : upload_video})