from django.shortcuts import render, redirect, HttpResponse

from enrollment.forms import EnrollForm
from enrollment.models import *
from django.views import View


class EnrollView(View):
    form_class = EnrollForm

    def get(self, request, *args, **kwargs):
        return HttpResponse('method get')

    def post(self, request, *args, **kwargs):
        enroll_form = self.form_class(request.POST)
        enroll_stu = request.POST.get('enrollment_for')
        enroll_obj = CustomUser.objects.get(id = enroll_stu)
        if enroll_obj.user_type == 'student':
            enroll_form = EnrollForm(request.POST)
            if enroll_form.is_valid():
                enroll_form.save()
                return HttpResponse(" enrolled")
            else:
                return HttpResponse('Not enrolled')
        else:
            return HttpResponse('not a student')
        
        return render(request, self.template_name, {"enroll_form" : enroll_form })
