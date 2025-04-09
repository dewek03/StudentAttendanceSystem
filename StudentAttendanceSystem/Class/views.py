from django.shortcuts import render

def class_list(request):
    return render(request, 'class_list.html')

def class_detail(request, session_id):
    return render(request, 'class_detail.html')

def create_class(request):
    return render(request, 'create_class.html')

def attendance_list(request, session_id):
    return render(request, 'attendance_list.html')

def mark_attendance(request, session_id):
    return render(request, 'mark_attendance.html')
