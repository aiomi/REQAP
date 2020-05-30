from django.core.exceptions import PermissionDenied
from django.shortcuts import reverse, redirect
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from users.models import Staff


def teacher_required(function):
    '''
    Decorator for views that checks that the logged in user is a teacher,
    redirects to the log-in page if necessary.
    '''
    def wrap(request, *args, **kwargs):
        if not request.user.is_teacher:
            messages.info(request, "Only staffs required")
            return redirect(reverse('login'))
    return wrap

def user_is_student_or_acadoffice_staff(function):
    """
    Checks if a user is a student or a staff in the academic office group.
    academic office group only has the permissions to view and respond to 
    transcript requests except the student who made them
    """
    def wrap(request, *args, **kwargs):
        staff = Staff.objects.filter(user=request.user).first()
        group = get_object_or_404(Group, name='Academic Office')
        
        # staff might return None and None has no ID
        if staff:
            #checks if the user belongs to the academic office group
            staff_check = group.staff_set.filter(pk=staff.id).first()
        else:
            staff_check = False

        if (request.user.is_student or staff_check):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def academic_office_staff_only(function):
    """
    Checks if a user is a staff in the academic office group.
    academic office group only has the permissions to view and respond to 
    transcript requests except the student who made them
    """
    def wrap(request, *args, **kwargs):
        staff = Staff.objects.filter(user=request.user).first()
        group = get_object_or_404(Group, name='Academic Office')
        
        # staff might return None and None has no ID
        if staff:
            #checks if the user belongs to the academic office group
            staff_check = group.staff_set.filter(pk=staff.id).first()
        else:
            staff_check = False

        if staff_check:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
