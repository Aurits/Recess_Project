from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import InstructorForm
from .models import StudentDetails
from .forms import FacilityForm
from .models import FacilityFeedback
from .models import InstructorFeedback
from .models import CourseFeedback
from .forms import CourseFeedbackForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg





def home(request):
    return render(request, 'index.html')

def start(request):
    return render(request, 'start.html')

def thankyou(request):
    return render(request, 'thankyou.html')


def recommend(request):
    students = StudentDetails.objects.all()
    course_items = CourseFeedback.objects.all()
    facilities = FacilityFeedback.objects.all()
    instructors = InstructorFeedback.objects.all()


    context = {
        'course_items': course_items,
        'facilities': facilities,
        'instructors': instructors,
        'students': students,
        }

    return render(request, 'dashboard/pages/recommend.html', context)


def course(request):
    if request.method == 'POST':
        form = CourseFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor')
    else:
        form = CourseFeedbackForm()

    return render(request, 'course.html', {'courseForm': form})


def instructor(request):
    return render(request, 'instructor.html')




def dashboard(request):
    students = StudentDetails.objects.all()
    course_items = CourseFeedback.objects.all()
    facilities = FacilityFeedback.objects.all()
    instructors = InstructorFeedback.objects.all()

    # Calculate the feedback counts for each category and aspect
    knowledge_counts = [InstructorFeedback.objects.filter(knowledge=i).count() for i in range(1, 6)]
    communication_counts = [InstructorFeedback.objects.filter(communication=i).count() for i in range(1, 6)]
    teaching_style_counts = [InstructorFeedback.objects.filter(teachingStyle=i).count() for i in range(1, 6)]
    responsiveness_counts = [InstructorFeedback.objects.filter(responsiveness=i).count() for i in range(1, 6)]

        # Calculate the average ratings for each category
    avg_course_effectiveness = CourseFeedback.objects.aggregate(Avg('effectiveness'))['effectiveness__avg']
    avg_course_interest = CourseFeedback.objects.aggregate(Avg('interest'))['interest__avg']

    avg_instructor_knowledge = InstructorFeedback.objects.aggregate(Avg('knowledge'))['knowledge__avg']
    avg_instructor_communication = InstructorFeedback.objects.aggregate(Avg('communication'))['communication__avg']
    avg_instructor_teaching_style = InstructorFeedback.objects.aggregate(Avg('teachingStyle'))['teachingStyle__avg']
    avg_instructor_responsiveness = InstructorFeedback.objects.aggregate(Avg('responsiveness'))['responsiveness__avg']

    avg_facility_accessibility = FacilityFeedback.objects.aggregate(Avg('facility_accessibility'))['facility_accessibility__avg']
    avg_facility_cleanliness = FacilityFeedback.objects.aggregate(Avg('cleanliness'))['cleanliness__avg']
    avg_facility_maintenance = FacilityFeedback.objects.aggregate(Avg('maintenance'))['maintenance__avg']
    avg_facility_safety = FacilityFeedback.objects.aggregate(Avg('safety'))['safety__avg']
    avg_facility_resource_availability = FacilityFeedback.objects.aggregate(Avg('resource_availability'))['resource_availability__avg']
    avg_facility_rating = FacilityFeedback.objects.aggregate(Avg('facility_rating'))['facility_rating__avg']

    context = {
        'course_items': course_items,
        'facilities': facilities,
        'instructors': instructors,
        'students': students,
        'poor_knowledge': knowledge_counts[0],
        'fair_knowledge': knowledge_counts[1],
        'good_knowledge': knowledge_counts[2],
        'very_good_knowledge': knowledge_counts[3],
        'excellent_knowledge': knowledge_counts[4],
        'poor_communication': communication_counts[0],
        'fair_communication': communication_counts[1],
        'good_communication': communication_counts[2],
        'very_good_communication': communication_counts[3],
        'excellent_communication': communication_counts[4],
        'poor_teaching_style': teaching_style_counts[0],
        'fair_teaching_style': teaching_style_counts[1],
        'good_teaching_style': teaching_style_counts[2],
        'very_good_teaching_style': teaching_style_counts[3],
        'excellent_teaching_style': teaching_style_counts[4],
        'poor_responsiveness': responsiveness_counts[0],
        'fair_responsiveness': responsiveness_counts[1],
        'good_responsiveness': responsiveness_counts[2],
        'very_good_responsiveness': responsiveness_counts[3],
        'excellent_responsiveness': responsiveness_counts[4],
        'avg_course_effectiveness': avg_course_effectiveness,
        'avg_course_interest': avg_course_interest,
        'avg_instructor_knowledge': avg_instructor_knowledge,
        'avg_instructor_communication': avg_instructor_communication,
        'avg_instructor_teaching_style': avg_instructor_teaching_style,
        'avg_instructor_responsiveness': avg_instructor_responsiveness,
        'avg_facility_accessibility': avg_facility_accessibility,
        'avg_facility_cleanliness': avg_facility_cleanliness,
        'avg_facility_maintenance': avg_facility_maintenance,
        'avg_facility_safety': avg_facility_safety,
        'avg_facility_resource_availability': avg_facility_resource_availability,
        'avg_facility_rating': avg_facility_rating,
    }

    return render(request, 'dashboard/pages/dashboard.html', context)




def courses(request):
    course_items = CourseFeedback.objects.all()
    course_ratings = list(CourseFeedback.objects.values_list('effectiveness', flat=True))
    course_rating_counts = [course_ratings.count(rating) for rating in range(1, 6)]

    context = {
        'course_items': course_items,
        'course_rating_counts': course_rating_counts, }
    return render(request, 'dashboard/pages/courses.html', context)


def delete_course_feedback(request, feedback_id):
    feedback = get_object_or_404(CourseFeedback, pk=feedback_id)
    if request.method == 'POST':
        feedback.delete()
        return redirect('courses')
    return render(request, 'dashboard/pages/delete_course_feedback.html', {'feedback': feedback})


def facilities(request):
    facilities = FacilityFeedback.objects.all()
    facility_ratings = list(FacilityFeedback.objects.values_list('facility_rating', flat=True))
    facility_rating_counts = [facility_ratings.count(rating) for rating in range(1, 6)]

    context = {
        'facilities': facilities,
        'facility_rating_counts': facility_rating_counts,
    }
    return render(request, 'dashboard/pages/facilities.html', context)


def instructors(request):
    feedbacks = InstructorFeedback.objects.all()
    instructor_ratings = list(InstructorFeedback.objects.values_list('knowledge', flat=True))
    instructor_rating_counts = [instructor_ratings.count(rating) for rating in range(1, 6)]
    
    # Prepare the rating labels to be passed to the template
    rating_labels = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']

    context = {
        'feedbacks': feedbacks,
        'instructor_rating_counts': instructor_rating_counts,
        'rating_labels': rating_labels,
    }
    return render(request, 'dashboard/pages/instructors.html', context)


def delete_instructor_feedback(request, feedback_id):
    feedback = get_object_or_404(InstructorFeedback, id=feedback_id)
    if request.method == 'POST':
        feedback.delete()
        return redirect('instructors')
    return render(request, 'dashboard/pages/delete_instructor_feedback.html', {'feedback': feedback})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/pages/profile.html')
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('sign_in')


def signout(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def signin(request):
    if request.user.is_authenticated:
        students = StudentDetails.objects.all()
        course_items = CourseFeedback.objects.all()
        facilities = FacilityFeedback.objects.all()
        instructors = InstructorFeedback.objects.all()

        # Calculate the feedback counts for each category and aspect
        knowledge_counts = [
            InstructorFeedback.objects.filter(knowledge=i).count() for i in range(1, 6)
        ]
        communication_counts = [
            InstructorFeedback.objects.filter(communication=i).count() for i in range(1, 6)
        ]
        teaching_style_counts = [
            InstructorFeedback.objects.filter(teachingStyle=i).count() for i in range(1, 6)
        ]
        responsiveness_counts = [
            InstructorFeedback.objects.filter(responsiveness=i).count() for i in range(1, 6)
        ]


            # Calculate the average ratings for each category
        avg_course_effectiveness = CourseFeedback.objects.aggregate(Avg('effectiveness'))['effectiveness__avg']
        avg_course_interest = CourseFeedback.objects.aggregate(Avg('interest'))['interest__avg']

        avg_instructor_knowledge = InstructorFeedback.objects.aggregate(Avg('knowledge'))['knowledge__avg']
        avg_instructor_communication = InstructorFeedback.objects.aggregate(Avg('communication'))['communication__avg']
        avg_instructor_teaching_style = InstructorFeedback.objects.aggregate(Avg('teachingStyle'))['teachingStyle__avg']
        avg_instructor_responsiveness = InstructorFeedback.objects.aggregate(Avg('responsiveness'))['responsiveness__avg']

        avg_facility_accessibility = FacilityFeedback.objects.aggregate(Avg('facility_accessibility'))['facility_accessibility__avg']
        avg_facility_cleanliness = FacilityFeedback.objects.aggregate(Avg('cleanliness'))['cleanliness__avg']
        avg_facility_maintenance = FacilityFeedback.objects.aggregate(Avg('maintenance'))['maintenance__avg']
        avg_facility_safety = FacilityFeedback.objects.aggregate(Avg('safety'))['safety__avg']
        avg_facility_resource_availability = FacilityFeedback.objects.aggregate(Avg('resource_availability'))['resource_availability__avg']
        avg_facility_rating = FacilityFeedback.objects.aggregate(Avg('facility_rating'))['facility_rating__avg']

        context = {
            'course_items': course_items,
            'facilities': facilities,
            'instructors': instructors,
            'students': students,
            'poor_knowledge': knowledge_counts[0],
            'fair_knowledge': knowledge_counts[1],
            'good_knowledge': knowledge_counts[2],
            'very_good_knowledge': knowledge_counts[3],
            'excellent_knowledge': knowledge_counts[4],
            'poor_communication': communication_counts[0],
            'fair_communication': communication_counts[1],
            'good_communication': communication_counts[2],
            'very_good_communication': communication_counts[3],
            'excellent_communication': communication_counts[4],
            'poor_teaching_style': teaching_style_counts[0],
            'fair_teaching_style': teaching_style_counts[1],
            'good_teaching_style': teaching_style_counts[2],
            'very_good_teaching_style': teaching_style_counts[3],
            'excellent_teaching_style': teaching_style_counts[4],
            'poor_responsiveness': responsiveness_counts[0],
            'fair_responsiveness': responsiveness_counts[1],
            'good_responsiveness': responsiveness_counts[2],
            'very_good_responsiveness': responsiveness_counts[3],
            'excellent_responsiveness': responsiveness_counts[4],
            'avg_course_effectiveness': avg_course_effectiveness,
            'avg_course_interest': avg_course_interest,
            'avg_instructor_knowledge': avg_instructor_knowledge,
            'avg_instructor_communication': avg_instructor_communication,
            'avg_instructor_teaching_style': avg_instructor_teaching_style,
            'avg_instructor_responsiveness': avg_instructor_responsiveness,
            'avg_facility_accessibility': avg_facility_accessibility,
            'avg_facility_cleanliness': avg_facility_cleanliness,
            'avg_facility_maintenance': avg_facility_maintenance,
            'avg_facility_safety': avg_facility_safety,
            'avg_facility_resource_availability': avg_facility_resource_availability,
            'avg_facility_rating': avg_facility_rating,
        }

        return render(request, 'dashboard/pages/dashboard.html', context)


    else:
        # Check to see if logging in
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # Authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged In!")
                return redirect('dashboard')
            else:
                messages.success(request, "There Was An Error Logging In, Please Try Again...")

                return redirect('home')
        else:
            return render(request, 'dashboard/pages/sign_in.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")

            return redirect('dashboard')
    else:
        form = SignUpForm()
        return render(request, 'dashboard/pages/sign_up.html', {'form': form})

    return render(request, 'dashboard/pages/sign_up.html', {'form': form})


def instructor_feedback(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form_data = form.cleaned_data
            feedback = InstructorFeedback(
                instructorName=form_data['instructorName'],
                department=form_data['department'],
                courseUnit=form_data['courseUnit'],
                knowledge=form_data['knowledge'],
                communication=form_data['communication'],
                teachingStyle=form_data['teachingStyle'],
                responsiveness=form_data['responsiveness'],
                additional_comments=form_data['additional_comments']
            )
            feedback.save()

            # Redirect to a success page after successful form submission
            return redirect('facility')
    else:
        form = InstructorForm()

    return render(request, 'instructor.html', {'form': form})


def studentDetails(request):
    if request.method == 'POST':
        name = request.POST['name']
        studentId = request.POST['studentId']
        emailAddress = request.POST['emailAddress']
        year_of_study = request.POST['year_of_study']

        # Save data to the database
        StudentDetails.objects.create(name=name, studentId=studentId, emailAddress=emailAddress,
                                      year_of_study=year_of_study)

        # Set a success message to display on the index.html template
        success_message = "Thank you for signing up!"
        return redirect('start')

    else:
        success_message = None

    return render(request, 'index.html', {'success_message': success_message})





def facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            feedback = FacilityFeedback(
                name=form.cleaned_data['name'],
                facility_college=form.cleaned_data['facility_college'],
                facility_accessibility=form.cleaned_data['facility_accessibility'],
                cleanliness=form.cleaned_data['cleanliness'],
                maintenance=form.cleaned_data['maintenance'],
                safety=form.cleaned_data['safety'],
                resource_availability=form.cleaned_data['resource_availability'],
                facility_rating=form.cleaned_data['facility_rating'],
                comment=form.cleaned_data['comment'],
            )
            feedback.save()
            return redirect('thankyou')  
    else:
        form = FacilityForm()

    return render(request, 'facility.html', {'form': form})


def delete_facility_feedback(request, feedback_id):
    if request.method == 'POST':
        feedback = FacilityFeedback.objects.get(pk=feedback_id)
        feedback.delete()
    return redirect('facilities')