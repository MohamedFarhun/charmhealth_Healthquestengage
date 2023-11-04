from django.shortcuts import render, redirect
from .models import Question, AnswerOption,UserOtherInfo,UserOtherInfoDoctor,AppointmentDetails,UserProfileScore,IntakeForm,ReportDetails,DoctorDetails,DoctorMoodDiary,predictions
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
import random
from datetime import date
from .forms import predictionsForm
import pandas as pd


def home(request):
    if request.method=='POST':
        user_type=request.POST['userType']
        username=request.POST['userId']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password,is_staff=user_type)
        if user is not None:
            auth.login(request,user)
            if request.user.is_authenticated:
                if request.user.is_staff==1:
                    return redirect("doctordashboard")
                else:
                    return redirect("patientdashboard")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/')
    return render(request,'home.html')

def questionnaire(request):
    if request.method == 'POST':
        # Retrieve question IDs from the session
        question_ids = request.session.get('question_ids', [])
        questions = Question.objects.filter(id__in=question_ids)

        # print(request.POST)
        user = User.objects.get(id=request.user.id)
        scores = 0

        # Check if all presented questions have been answered
        unanswered_questions = []
        for q in questions:
            if not request.POST.get(f'question_{q.id}') and q.question_type not in ['MRQ']:
                unanswered_questions.append(q)
            elif q.question_type == 'MRQ' and not request.POST.getlist(f'question_{q.id}'):
                unanswered_questions.append(q)
        if unanswered_questions:
            print(f"Unanswered Questions IDs: {unanswered_questions}")
            return render(request, 'questionnaire.html', {'questions': questions, 'error_message': 'Please answer all the questions before submitting.'})
        
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if question.question_type == 'MCQ' or question.question_type == 'TF':
                correct_option = AnswerOption.objects.filter(question=question, is_correct=True).first()
                if correct_option and str(correct_option.id) == user_answer:
                    scores += 1
            elif question.question_type == 'MRQ':
                user_answers = request.POST.getlist(f'question_{question.id}')  # Retrieves multiple selections as a list
                correct_options = AnswerOption.objects.filter(question=question, is_correct=True)
                
                # Check if all the selected answers are correct
                if all(str(option.id) in user_answers for option in correct_options) and len(user_answers) == len(correct_options):
                    scores += 1

        # Update or create the user's score in the database
        user_profile_score, created = UserProfileScore.objects.get_or_create(user_id=user)
        user_profile_score.scores = scores
        user_profile_score.last_checkup_date = date.today()
        user_profile_score.save()

        # Redirect or render as per your requirement
        return redirect('patientdashboard')  # Replace 'some_view_name' with your desired view

    else:
        # For GET request, select a new set of 20 random questions
        all_questions = list(Question.objects.all())
        random.shuffle(all_questions)
        questions = all_questions[:20]
        
        # Store question IDs in the session for later retrieval during POST
        request.session['question_ids'] = [q.id for q in questions]

    return render(request, 'questionnaire.html', {'questions': questions})

def patientdashboard(request):
    user_info = None
    doctor_info = None
    doctor_other_info=None
    lastdetails=None
    allappointments=None
    intake_details=None
    user_profile_score=None
    user_info = UserOtherInfo.objects.get(user_id=request.user.id)
    doctor_info = User.objects.get(id=user_info.Primarycare)
    doctor_other_info = UserOtherInfoDoctor.objects.get(user_id=doctor_info.id)
    allappointments=AppointmentDetails.objects.filter(user_id=request.user.id).all()
    if request.method == 'POST':
         user = User.objects.get(id=request.user.id)
         details=AppointmentDetails.objects.create(Age=request.POST['Age'],Height=request.POST['Height'],Weight=request.POST['Weight'],BMI=request.POST['BMI'],Issue=request.POST['Issue'],Date=request.POST['Date'],Start_time=request.POST['Start_time'],End_time=request.POST['End_time'],Comment=request.POST['Comment'],user_id=user)
         details.save()
         messages.success(request,'Appointment Added Successfully.')
         return redirect('patientdashboard')
    else:
         lastdetails=AppointmentDetails.objects.filter(user_id=request.user.id).last()
         intake_details=IntakeForm.objects.filter(user_id=request.user.id).last()
         user_profile_score = UserProfileScore.objects.get(user_id=request.user.id)
         context = {
        'user_info': user_info,
        'doctor_info': doctor_info,
        'doctor_other_info':doctor_other_info,
        'lastdetails':lastdetails,
        'allappointments':allappointments,
        'intake_details':intake_details,
        'user_profile_score':user_profile_score
    }
    return render(request, 'patientdashboard.html', context)

def doctordashboard(request):
    alldoctordetails=None
    lastdetails=None
    doctormooddiary=None
    doctor_other_info=None
    doctor_info=None
    doctor_info = User.objects.get(id=request.user.id)
    doctor_other_info = UserOtherInfoDoctor.objects.get(user_id= doctor_info.id)
    alldoctordetails=DoctorDetails.objects.filter(user_id=request.user.id).all()
    predicted_health = predictions.objects.all()
    if request.method == 'POST':
         user = User.objects.get(id=request.user.id)
         doctordetails=DoctorDetails.objects.create(user_id=user,Age=request.POST['Age'],Height=request.POST['Height'],Weight=request.POST['Weight'],Experience=request.POST['Experience'])       
         doctordetails.save()
         return redirect('doctordashboard')
    else:
         lastdetails=DoctorDetails.objects.filter(user_id=request.user.id).last()
         doctormooddiary=DoctorMoodDiary.objects.filter(user_id=request.user.id).last()
         context = {
        'alldoctordetails': alldoctordetails,
        'lastdetails': lastdetails,
        'doctor_info': doctor_info,
        'doctor_other_info': doctor_other_info,
        'doctormooddiary':doctormooddiary,
        'predicted_health': predicted_health,
         }
         return render(request, 'doctordashboard.html',context)

def patientregistration(request):
    if request.method == 'POST':
        user_type=request.POST['userType']
        username=request.POST['username']
        password=request.POST['password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken')
            return redirect('patientregistration')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email ID already taken')
            return redirect('patientregistration')
        else:
            user=User.objects.create_user(username=username,password=password,is_staff=user_type,email=email,first_name=firstname,last_name=lastname)
            user.save()
            n = UserOtherInfo.objects.create(user_id=user, MiddleName=request.POST['middlename'],PhoneNumber=request.POST['phone'],DateofBirth=request.POST['dob'],gender=request.POST['gender'],Address=request.POST['address'],City=request.POST['cities'],Pincode=request.POST['pincode'],Primarycare=request.POST['physician'],KnownAllergies=request.POST['allergies'],CurrentMedications=request.POST['Medication'],MedicalConditions=request.POST['Conditions'])
            n.save()
            return render(request,'home.html')
    else:
         doctors=None
         doctors=User.objects.filter(is_staff=True)
         context={
                'doctors':doctors,
            }
    return render(request,'patientregistration.html',context)

def doctorregistration(request):
    if request.method == 'POST':
        user_type=request.POST['userType']
        username=request.POST['username']
        password=request.POST['password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken')
            return redirect('doctorregistration')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email ID already taken')
            return redirect('doctorregistration')
        else:
            user=User.objects.create_user(username=username,password=password,is_staff=user_type,email=email,first_name=firstname,last_name=lastname)
            user.save()
            n = UserOtherInfoDoctor.objects.create(user_id=user, MiddleName=request.POST['middlename'],PhoneNumber=request.POST['phone'],DateofBirth=request.POST['dob'],gender=request.POST['gender'],Address=request.POST['address'],City=request.POST['city'],Pincode=request.POST['pincode'],Experience=request.POST['experience'],Specialist=request.POST['specialist'],Degrees=request.POST['degrees'],NeetMarks=request.POST['neet'])
            n.save()
            print("User Created")
            return render(request,'home.html')
    else:
      return render(request,'doctorregistration.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')

def intake(request):
     if request.method == 'POST':
         user = User.objects.get(id=request.user.id)
         intake=IntakeForm.objects.create(user_id=user,occupation = request.POST['occupation'],Employer_Name = request.POST['Employer_Name'],insurance = request.POST['insurance'],marital = request.POST['marital'],live = request.POST['live'],person = request.POST['person'],about = request.POST['about'],therapy = request.POST['therapy'],concern = request.POST['concern'],goals = request.POST['goals'],surgeries = request.POST['surgeries'],hospitalizations = request.POST['hospitalizations'],allergies = request.POST['allergies'],prescribed = request.POST['prescribed'],supplements = request.POST['supplements'],providers = request.POST['providers'],Health = request.POST['Health'],cholesterol = request.POST['cholesterol'],Pap_smear = request.POST['Pap_smear'],abnormal_Pap = request.POST['abnormal_Pap'],mammogram = request.POST['mammogram'],bone = request.POST['bone'],reaction = request.POST['reaction'],asleep = request.POST['asleep'],uninterrupted = request.POST['uninterrupted'],refreshed = request.POST['refreshed'],aids = request.POST['aids'],preferences = request.POST['preferences'],Breakfast = request.POST['Breakfast'],Lunch = request.POST['Lunch'],Dinner = request.POST['Dinner'],Snacks = request.POST['Snacks'],Drinks = request.POST['Drinks'],water = request.POST['water'],current = request.POST['current'],alcohol = request.POST['alcohol'],caffeine = request.POST['caffeine'],tobacco = request.POST['tobacco'],Recreational = request.POST['Recreational'],exercise = request.POST['exercise'],Fatigue = request.POST['Fatigue'],Insomnia = request.POST['Insomnia'],Appetite = request.POST['Appetite'],Unexplained_weight = request.POST['Unexplained_weight'],Fevers = request.POST['Fevers'],Cold = request.POST['Cold'],Heat = request.POST['Heat'],flashes = request.POST['flashes'],sweats = request.POST['sweats'],sweats_too = request.POST['sweats_too'],Headaches = request.POST['Headaches'],Migraines = request.POST['Migraines'],Dizziness = request.POST['Dizziness'],Injury = request.POST['Injury'],Hives = request.POST['Hives'],Eczema = request.POST['Eczema'],Acne = request.POST['Acne'],Dry = request.POST['Dry'],Itchy_skin= request.POST['Itchy_skin'],Dandruff = request.POST['Dandruff'],Warts = request.POST['Warts'],Skin = request.POST['Skin'],thinning = request.POST['thinning'],nails = request.POST['nails'],Cuts = request.POST['Cuts'],foot = request.POST['foot'],eyes = request.POST['eyes'],Itchy_eyes = request.POST['Itchy_eyes'],Blurred = request.POST['Blurred'],excessively = request.POST['excessively'],sensitive = request.POST['sensitive'],bloodshot = request.POST['bloodshot'],Night = request.POST['Night'],Glaucoma = request.POST['Glaucoma'],Cataracts = request.POST['Cataracts'],Ear = request.POST['Ear'],discharge = request.POST['discharge'],Ringing = request.POST['Ringing'],Changes = request.POST['Changes'],loss = request.POST['loss'],hearing_aid = request.POST['hearing_aid'],Congestion = request.POST['Congestion'],hayfever = request.POST['hayfever'],nasal = request.POST['nasal'],Nosebleeds = request.POST['Nosebleeds'],Sinus = request.POST['Sinus'],mood = request.POST['mood'],hours = request.POST['hours'],physical = request.POST['physical'],relaxation = request.POST['relaxation'],support = request.POST['support'],supportive = request.POST['supportive'],side_effects = request.POST['side_effects'],illness = request.POST['illness'],events = request.POST['events'],menstrual = request.POST['menstrual'],today = request.POST['today'],drugs = request.POST['drugs'])       
         intake.save()
         return redirect('patientdashboard')
     else:
         images_list = None
         images_list = ['puzzle.jpg','puzzle1.jpg','puzzle2.jpg']
         random_image = random.choice(images_list)
         context={
                'random_image':random_image,
            }
         return render(request,'intake.html',context)

def report(request):
    user_info = None
    doctor_info = None
    doctor_other_info=None
    lastdetails=None
    allappointments=None
    intake_details=None
    user_profile_score=None
    user_info = UserOtherInfo.objects.get(user_id=request.user.id)
    doctor_info = User.objects.get(id=user_info.Primarycare)
    doctor_other_info = UserOtherInfoDoctor.objects.get(user_id=doctor_info.id)
    allappointments=AppointmentDetails.objects.filter(user_id=request.user.id).all()
    allreports=ReportDetails.objects.filter(user_id=request.user.id).all()
    if request.method == 'POST':
         user = User.objects.get(id=request.user.id)
         report= ReportDetails.objects.create(game=request.POST['game'],intake=request.POST['intake'],questionnaire_answered=request.POST['questionnaire_answered'],user_id=user)
         report.save()
         messages.success(request,'Report Submitted Successfully.')
         return redirect('report')
    else:
         lastdetails=AppointmentDetails.objects.filter(user_id=request.user.id).last()
         intake_details=IntakeForm.objects.filter(user_id=request.user.id).last()
         user_profile_score = UserProfileScore.objects.filter(user_id=request.user.id).last()
         context = {
        'user_info': user_info,
        'doctor_info': doctor_info,
        'doctor_other_info':doctor_other_info,
        'lastdetails':lastdetails,
        'allappointments':allappointments,
        'intake_details':intake_details,
        'allreports':allreports,
        'user_profile_score':user_profile_score
    }
    return render(request, 'report.html',context)

def application(request):
    if request.method == 'POST':
       user = User.objects.get(id=request.user.id)
       doctormooddiary=DoctorMoodDiary.objects.create(user_id =user, mood = request.POST['mood'],hours = request.POST['hours'],physical = request.POST['physical'],relaxation = request.POST['relaxation'],support = request.POST['support'],supportive = request.POST['supportive'],patients = request.POST['patients'],illness = request.POST['illness'],events = request.POST['events'],menstrual = request.POST['menstrual'],today = request.POST['today'],drugs = request.POST['drugs'])
       doctormooddiary.save()
       return redirect('doctordashboard')
    else:
        doctormooddiary=DoctorMoodDiary.objects.filter(user_id=request.user.id).last()
        context = {
            'doctormooddiary':doctormooddiary,
        }
    return render(request, 'application.html',context)

def doctorheader(request):
    return render(request,'doctorheader.html')

def predictions_patient(request):
    if request.method == 'POST':
        form = predictionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctordashboard')
    else:
        form = predictionsForm()
    context = {
        'form': form,
    }
    print(request.POST)
    return render(request, 'predictions_patient.html', context)
    
    
  