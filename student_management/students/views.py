from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm  # We'll define this form shortly
from django.urls import reverse

# View to show all students
def student_list(request):
    students = Student.objects.all()  # Get all students from the database
    return render(request, 'students/student_list.html', {'students': students})

# View to add a new student
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new student
            return redirect(reverse('student-list'))  # Redirect to the list of students
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

# View to update an existing student's information
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)  # More efficient, avoids crashes if student doesn't exist
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()  # Save the updated student
            return redirect(reverse('student-list'))  # Redirect to the list of students
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form, 'student': student})

# View to delete a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)  # Use get_object_or_404 for safety
    if request.method == 'POST':  # Make sure that a confirmation is made before deleting
        student.delete()  # Delete the student from the database
        return redirect(reverse('student-list'))  # Redirect to the list of students
    
    return render(request, 'students/student_confirm_delete.html', {'student': student})
