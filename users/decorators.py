from django.core.exceptions import PermissionDenied
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from users.models import Staff


def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a teacher,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        #u.is_active no need to check because staffs are set to inactive by default
        lambda u: u.is_teacher, 
        login_url=login_url,
        redirect_field_name=redirect_field_name
        )
    if function:
        return actual_decorator(function)
    return actual_decorator

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
