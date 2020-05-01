from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from .models import Staff

def check_academicgroup_staff(request):

    staff = Staff.objects.filter(user=request.user).first()
    group = get_object_or_404(Group, name='Academic Office')
        
    # staff might return None and None has no ID
    if staff:
        #checks if the user belongs to the academic office group
        staff_check = group.staff_set.filter(pk=staff.id).first()
    else:
        staff_check = False
    return staff_check

