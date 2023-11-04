from django.db import models
from django.contrib.auth.models import User
import joblib

class Question(models.Model):
    Question_no = models.IntegerField(default=0)
    QUESTION_TYPES = [
        ('MCQ', 'Multiple Choice Question'),
        ('MRQ', 'Multiple Responses Question'),
        ('TF', 'True/False Question'),
    ]
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES, default='MCQ')
    option_count = models.IntegerField(default=4)

class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    choice_number = models.PositiveIntegerField()
    is_correct = models.BooleanField(default=False)

class UserProfileScore(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    last_checkup_date = models.DateField(null=True, blank=True)

class UserOtherInfo(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    MiddleName=models.CharField(max_length=200,blank=True)
    PhoneNumber=models.BigIntegerField()
    DateofBirth=models.DateField()
    class gender(models.TextChoices):
        Male="Male",("Male")
        Female="Female",("Female")
    gender=models.CharField(max_length=200,choices=gender.choices)
    Address=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Pincode=models.IntegerField()
    Primarycare=models.IntegerField()
    class KnownAllergies(models.TextChoices):
        KnownAllergy1="Peanut Allergy",("Peanut Allergy")
        KnownAllergy2="Dairy Allergy",("Dairy Allergy")
        KnownAllergy3="Gluten Intolerance",("Gluten Intolerance")
    KnownAllergies=models.CharField(max_length=200,choices=KnownAllergies.choices)
    class CurrentMedications(models.TextChoices):
        CurrentMedication1="Tablets",("Tablets")
        CurrentMedication2="Inhalers",("Inhalers")
        CurrentMedication3="Injections",("Injections")
    CurrentMedications=models.CharField(max_length=200,choices=CurrentMedications.choices)
    class MedicalConditions(models.TextChoices):
        MedicalCondition1="COVID-19",("COVID-19")
        MedicalCondition2="Common Cold",("Common Cold")
        MedicalCondition3="Asthma Attack",("Asthma Attack")
    MedicalConditions=models.CharField(max_length=200,choices=MedicalConditions.choices)

class UserOtherInfoDoctor(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    MiddleName=models.CharField(max_length=200,blank=True)
    PhoneNumber=models.BigIntegerField()
    DateofBirth=models.DateField()
    class gender(models.TextChoices):
        Male="Male",("Male")
        Female="Female",("Female")
    gender=models.CharField(max_length=200,choices=gender.choices)
    Address=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Pincode=models.IntegerField()
    class Experience(models.TextChoices):
        Year1="Less than 1 Year",("Less than 1 Year")
        Year2="One to two Years",("One to two Years")
        Year3="Three to five Years",("Three to five Years")
        Year4="More than 5 Years",("More than 5 years")
    Experience=models.CharField(max_length=200,choices=Experience.choices)
    Specialist=models.CharField(max_length=200)
    class Degrees(models.TextChoices):
        Degree1="Bachelor of Medicine and Bachelor of Surgery",("Bachelor of Medicine and Bachelor of Surgery")
        Degree2="Bachelor of Dental Surgery",("Bachelor of Dental Surgery")
        Degree3="Bachelor of Ayurvedic Medicine and Surgery",("Bachelor of Ayurvedic Medicine and Surgery")
    Degrees=models.CharField(max_length=200,choices=Degrees.choices)
    NeetMarks=models.IntegerField()

class AppointmentDetails(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Age=models.IntegerField()
    Height=models.IntegerField()
    Weight=models.IntegerField()
    BMI=models.IntegerField()
    Issue=models.CharField(max_length=200)
    Date=models.DateField()
    Start_time=models.TimeField()
    End_time=models.TimeField()
    Comment=models.TextField()

class IntakeForm(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    occupation = models.CharField(max_length=255)
    Employer_Name = models.CharField(max_length=255)
    insurance = models.CharField(max_length=255)
    marital_CHOICES = [('single', 'single'), ('married', 'married')]
    marital = models.CharField(max_length=255, choices=marital_CHOICES)
    live = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    therapy_CHOICES = [('therapy1', 'therapy1'), ('therapy2', 'therapy2'), ('therapy3', 'therapy3'), ('therapy4', 'therapy4')]
    therapy = models.CharField(max_length=255, choices=therapy_CHOICES)
    concern = models.CharField(max_length=255)
    goals = models.CharField(max_length=255)
    surgeries_CHOICES = [('surgeries_yes', 'surgeries_yes'), ('surgeries_no', 'surgeries_no')]
    surgeries = models.CharField(max_length=255, choices=surgeries_CHOICES)
    hospitalizations_CHOICES = [('hospitalizations_yes', 'hospitalizations_yes'), ('hospitalizations_no', 'hospitalizations_no')]
    hospitalizations = models.CharField(max_length=255, choices=hospitalizations_CHOICES)
    allergies_CHOICES = [('allergies_yes', 'allergies_yes'), ('allergies_no', 'allergies_no')]
    allergies = models.CharField(max_length=255, choices=allergies_CHOICES)
    prescribed = models.CharField(max_length=255)
    supplements = models.CharField(max_length=255)
    providers = models.CharField(max_length=255)
    Health_CHOICES = [('Health_Excellent', 'Health_Excellent'), ('Health_Good', 'Health_Good'), ('Health_Moderate', 'Health_Moderate'), ('Health_Bad', 'Health_Bad')]
    Health = models.CharField(max_length=255, choices=Health_CHOICES)
    cholesterol_CHOICES = [('cholesterol_yes', 'cholesterol_yes'), ('cholesterol_no', 'cholesterol_no')]
    cholesterol = models.CharField(max_length=255, choices=cholesterol_CHOICES)
    Pap_smear_CHOICES = [('Pap_smear_yes', 'Pap_smear_yes'), ('Pap_smear_no', 'Pap_smear_no')]
    Pap_smear = models.CharField(max_length=255, choices=Pap_smear_CHOICES)
    abnormal_Pap_CHOICES = [('abnormal_Pap_yes', 'abnormal_Pap_yes'), ('abnormal_Pap_no', 'abnormal_Pap_no')]
    abnormal_Pap = models.CharField(max_length=255, choices=abnormal_Pap_CHOICES)
    mammogram_CHOICES = [('mammogram_yes', 'mammogram_yes'), ('mammogram_no', 'mammogram_no')]
    mammogram = models.CharField(max_length=255, choices=mammogram_CHOICES)
    bone_CHOICES = [('bone_yes', 'bone_yes'), ('bone_no', 'bone_no')]
    bone = models.CharField(max_length=255, choices=bone_CHOICES)
    reaction_CHOICES = [('reaction_yes', 'reaction_yes'), ('reaction_no', 'reaction_no')]
    reaction = models.CharField(max_length=255, choices=reaction_CHOICES)
    asleep_CHOICES = [('asleep_yes', 'asleep_yes'), ('asleep_no', 'asleep_no')]
    asleep = models.CharField(max_length=255, choices=asleep_CHOICES)
    uninterrupted_CHOICES = [('uninterrupted_yes', 'uninterrupted_yes'), ('uninterrupted_no', 'uninterrupted_no')]
    uninterrupted = models.CharField(max_length=255, choices=uninterrupted_CHOICES)
    refreshed_CHOICES = [('refreshed_yes', 'refreshed_yes'), ('refreshed_no', 'refreshed_no')]
    refreshed = models.CharField(max_length=255, choices=refreshed_CHOICES)
    aids_CHOICES = [('aids_yes', 'aids_yes'), ('aids_no', 'aids_no')]
    aids = models.CharField(max_length=255, choices=aids_CHOICES)
    preferences = models.CharField(max_length=255)
    Breakfast = models.CharField(max_length=255)
    Lunch = models.CharField(max_length=255)
    Dinner = models.CharField(max_length=255)
    Snacks = models.CharField(max_length=255)
    Drinks = models.CharField(max_length=255)
    water = models.CharField(max_length=255)
    current_CHOICES = [('current_yes', 'current_yes'), ('current_no', 'current_no')]
    current = models.CharField(max_length=255, choices=current_CHOICES)
    alcohol_CHOICES = [('alcohol_yes', 'alcohol_yes'), ('alcohol_no', 'alcohol_no')]
    alcohol = models.CharField(max_length=255, choices=alcohol_CHOICES)
    caffeine_CHOICES = [('caffeine_yes', 'caffeine_yes'), ('caffeine_no', 'caffeine_no')]
    caffeine = models.CharField(max_length=255, choices=caffeine_CHOICES)
    tobacco_CHOICES = [('tobacco_yes', 'tobacco_yes'), ('tobacco_no', 'tobacco_no')]
    tobacco = models.CharField(max_length=255, choices=tobacco_CHOICES)
    Recreational_CHOICES = [('Recreational_yes', 'Recreational_yes'), ('Recreational_no', 'Recreational_no')]
    Recreational = models.CharField(max_length=255, choices=Recreational_CHOICES)
    exercise_CHOICES = [('exercise_Daily', 'exercise_Daily'), ('exercise_Monthly', 'exercise_Monthly'), ('exercise_Weekly', 'exercise_Weekly'), ('exercise_Yearly', 'exercise_Yearly')]
    exercise = models.CharField(max_length=255, choices=exercise_CHOICES)
    Fatigue_CHOICES = [('Fatigue_yes', 'Fatigue_yes'), ('Fatigue_no', 'Fatigue_no')]
    Fatigue = models.CharField(max_length=255, choices=Fatigue_CHOICES)
    Insomnia_CHOICES = [('Insomnia_yes', 'Insomnia_yes'), ('Insomnia_no', 'Insomnia_no')]
    Insomnia = models.CharField(max_length=255, choices=Insomnia_CHOICES)
    Appetite_CHOICES = [('Appetite_yes', 'Appetite_yes'), ('Appetite_no', 'Appetite_no')]
    Appetite = models.CharField(max_length=255, choices=Appetite_CHOICES)
    Unexplained_weight_CHOICES = [('Unexplained_weight_yes', 'Unexplained_weight_yes'), ('Unexplained_weight_no', 'Unexplained_weight_no')]
    Unexplained_weight = models.CharField(max_length=255, choices=Unexplained_weight_CHOICES)
    Fevers_CHOICES = [('Fevers_yes', 'Fevers_yes'), ('Fevers_no', 'Fevers_no')]
    Fevers = models.CharField(max_length=255, choices=Fevers_CHOICES)
    Cold_CHOICES = [('Cold_yes', 'Cold_yes'), ('Cold_no', 'Cold_no')]
    Cold = models.CharField(max_length=255, choices=Cold_CHOICES)
    Heat_CHOICES = [('Heat_yes', 'Heat_yes'), ('Heat_no', 'Heat_no')]
    Heat = models.CharField(max_length=255, choices=Heat_CHOICES)
    flashes_CHOICES = [('flashes_yes', 'flashes_yes'), ('flashes_no', 'flashes_no')]
    flashes = models.CharField(max_length=255, choices=flashes_CHOICES)
    sweats_CHOICES = [('sweats_yes', 'sweats_yes'), ('sweats_no', 'sweats_no')]
    sweats = models.CharField(max_length=255, choices=sweats_CHOICES)
    sweats_too_CHOICES = [('sweats_yes', 'sweats_yes'), ('sweats_no', 'sweats_no')]
    sweats_too = models.CharField(max_length=255, choices=sweats_too_CHOICES)
    Headaches_CHOICES = [('Headaches_yes', 'Headaches_yes'), ('Headaches_no', 'Headaches_no')]
    Headaches = models.CharField(max_length=255, choices=Headaches_CHOICES)
    Migraines_CHOICES = [('Migraines_yes', 'Migraines_yes'), ('Migraines_no', 'Migraines_no')]
    Migraines = models.CharField(max_length=255, choices=Migraines_CHOICES)
    Dizziness_CHOICES = [('Dizziness_yes', 'Dizziness_yes'), ('Dizziness_no', 'Dizziness_no')]
    Dizziness = models.CharField(max_length=255, choices=Dizziness_CHOICES)
    Injury_CHOICES = [('Injury_yes', 'Injury_yes'), ('Injury_no', 'Injury_no')]
    Injury = models.CharField(max_length=255, choices=Injury_CHOICES)
    Hives_CHOICES = [('Hives_yes', 'Hives_yes'), ('Hives_no', 'Hives_no')]
    Hives = models.CharField(max_length=255, choices=Hives_CHOICES)
    Eczema_CHOICES = [('Eczema_yes', 'Eczema_yes'), ('Eczema_no', 'Eczema_no')]
    Eczema = models.CharField(max_length=255, choices=Eczema_CHOICES)
    Acne_CHOICES = [('Acne_yes', 'Acne_yes'), ('Acne_no', 'Acne_no')]
    Acne = models.CharField(max_length=255, choices=Acne_CHOICES)
    Dry_CHOICES = [('Dry_yes', 'Dry_yes'), ('Dry_no', 'Dry_no')]
    Dry = models.CharField(max_length=255, choices=Dry_CHOICES)
    Itchy_eyes_CHOICES = [('Itchy_yes', 'Itchy_yes'), ('Itchy_no', 'Itchy_no')]
    Itchy_eyes = models.CharField(max_length=255, choices=Itchy_eyes_CHOICES)
    Itchy_skin_CHOICES = [('Itchy_yes', 'Itchy_yes'), ('Itchy_no', 'Itchy_no')]
    Itchy_skin = models.CharField(max_length=255, choices=Itchy_skin_CHOICES)
    Dandruff_CHOICES = [('Dandruff_yes', 'Dandruff_yes'), ('Dandruff_no', 'Dandruff_no')]
    Dandruff = models.CharField(max_length=255, choices=Dandruff_CHOICES)
    Warts_CHOICES = [('Warts_yes', 'Warts_yes'), ('Warts_no', 'Warts_no')]
    Warts = models.CharField(max_length=255, choices=Warts_CHOICES)
    Skin_CHOICES = [('Skin_yes', 'Skin_yes'), ('Skin_no', 'Skin_no')]
    Skin = models.CharField(max_length=255, choices=Skin_CHOICES)
    thinning_CHOICES = [('thinning_yes', 'thinning_yes'), ('thinning_no', 'thinning_no')]
    thinning = models.CharField(max_length=255, choices=thinning_CHOICES)
    nails_CHOICES = [('nails_yes', 'nails_yes'), ('nails_no', 'nails_no')]
    nails = models.CharField(max_length=255, choices=nails_CHOICES)
    Cuts_CHOICES = [('Cuts_yes', 'Cuts_yes'), ('Cuts_no', 'Cuts_no')]
    Cuts = models.CharField(max_length=255, choices=Cuts_CHOICES)
    foot_CHOICES = [('foot_yes', 'foot_yes'), ('foot_no', 'foot_no')]
    foot = models.CharField(max_length=255, choices=foot_CHOICES)
    eyes_CHOICES = [('eyes_yes', 'eyes_yes'), ('eyes_no', 'eyes_no')]
    eyes = models.CharField(max_length=255, choices=eyes_CHOICES)
    Blurred_CHOICES = [('Blurred_yes', 'Blurred_yes'), ('Blurred_no', 'Blurred_no')]
    Blurred = models.CharField(max_length=255, choices=Blurred_CHOICES)
    excessively_CHOICES = [('excessively_yes', 'excessively_yes'), ('excessively_no', 'excessively_no')]
    excessively = models.CharField(max_length=255, choices=excessively_CHOICES)
    sensitive_CHOICES = [('sensitive_yes', 'sensitive_yes'), ('sensitive_no', 'sensitive_no')]
    sensitive = models.CharField(max_length=255, choices=sensitive_CHOICES)
    bloodshot_CHOICES = [('bloodshot_yes', 'bloodshot_yes'), ('bloodshot_no', 'bloodshot_no')]
    bloodshot = models.CharField(max_length=255, choices=bloodshot_CHOICES)
    Night_CHOICES = [('Night_yes', 'Night_yes'), ('Night_no', 'Night_no')]
    Night = models.CharField(max_length=255, choices=Night_CHOICES)
    Glaucoma_CHOICES = [('Glaucoma_yes', 'Glaucoma_yes'), ('Glaucoma_no', 'Glaucoma_no')]
    Glaucoma = models.CharField(max_length=255, choices=Glaucoma_CHOICES)
    Cataracts_CHOICES = [('Cataracts_yes', 'Cataracts_yes'), ('Cataracts_no', 'Cataracts_no')]
    Cataracts = models.CharField(max_length=255, choices=Cataracts_CHOICES)
    Ear_CHOICES = [('Ear_yes', 'Ear_yes'), ('Ear_no', 'Ear_no')]
    Ear = models.CharField(max_length=255, choices=Ear_CHOICES)
    discharge_CHOICES = [('discharge_yes', 'discharge_yes'), ('discharge_no', 'discharge_no')]
    discharge = models.CharField(max_length=255, choices=discharge_CHOICES)
    Ringing_CHOICES = [('Ringing_yes', 'Ringing_yes'), ('Ringing_no', 'Ringing_no')]
    Ringing = models.CharField(max_length=255, choices=Ringing_CHOICES)
    Changes_CHOICES = [('Changes_yes', 'Changes_yes'), ('Changes_no', 'Changes_no')]
    Changes = models.CharField(max_length=255, choices=Changes_CHOICES)
    loss_CHOICES = [('loss_yes', 'loss_yes'), ('loss_no', 'loss_no')]
    loss = models.CharField(max_length=255, choices=loss_CHOICES)
    hearing_aid_CHOICES = [('hearing_aid_yes', 'hearing_aid_yes'), ('hearing_aid_no', 'hearing_aid_no')]
    hearing_aid = models.CharField(max_length=255, choices=hearing_aid_CHOICES)
    Congestion_CHOICES = [('Congestion_yes', 'Congestion_yes'), ('Congestion_no', 'Congestion_no')]
    Congestion = models.CharField(max_length=255, choices=Congestion_CHOICES)
    hayfever_CHOICES = [('hayfever_yes', 'hayfever_yes'), ('hayfever_no', 'hayfever_no')]
    hayfever = models.CharField(max_length=255, choices=hayfever_CHOICES)
    nasal_CHOICES = [('nasal_yes', 'nasal_yes'), ('nasal_no', 'nasal_no')]
    nasal = models.CharField(max_length=255, choices=nasal_CHOICES)
    Nosebleeds_CHOICES = [('Nosebleeds_yes', 'Nosebleeds_yes'), ('Nosebleeds_no', 'Nosebleeds_no')]
    Nosebleeds = models.CharField(max_length=255, choices=Nosebleeds_CHOICES)
    Sinus_CHOICES = [('Sinus_yes', 'Sinus_yes'), ('Sinus_no', 'Sinus_no')]
    Sinus = models.CharField(max_length=255, choices=Sinus_CHOICES)
    mood_CHOICES=[('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),('5', '5'), ('6', '6'),('7', '7'), ('8', '8'),('9', '9'), ('10', '10')]
    mood = models.CharField(choices=mood_CHOICES)
    hours = models.CharField(max_length=255)
    physical_CHOICES = [('yes', 'yes'), ('no', 'no')]
    physical = models.CharField(max_length=255, choices=physical_CHOICES)
    relaxation_CHOICES = [('yes', 'yes'), ('no', 'no')]
    relaxation = models.CharField(max_length=255, choices=relaxation_CHOICES)
    support_CHOICES = [('yes', 'yes'), ('no', 'no')]
    support = models.CharField(max_length=255, choices=support_CHOICES)
    supportive_CHOICES = [('yes', 'yes'), ('no', 'no')]
    supportive = models.CharField(max_length=255, choices=supportive_CHOICES)
    side_effects_CHOICES = [('yes', 'yes'), ('no', 'no')]
    side_effects = models.CharField(max_length=255, choices=side_effects_CHOICES)
    illness_CHOICES = [('yes', 'yes'), ('no', 'no')]
    illness = models.CharField(max_length=255, choices=illness_CHOICES)
    events_CHOICES = [('yes', 'yes'), ('no', 'no')]
    events = models.CharField(max_length=255, choices=events_CHOICES)
    menstrual_CHOICES = [('yes', 'yes'), ('no', 'no')]
    menstrual = models.CharField(max_length=255, choices=menstrual_CHOICES)
    today_CHOICES = [('yes', 'yes'), ('no', 'no')]
    today = models.CharField(max_length=255, choices=today_CHOICES)
    drugs_CHOICES = [('yes', 'yes'), ('no', 'no')]
    drugs = models.CharField(max_length=255, choices=drugs_CHOICES)

class ReportDetails(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    game_CHOICES = [('yes', 'yes'), ('no', 'no'),('maybe','maybe')]
    game = models.CharField(max_length=255, choices=game_CHOICES)
    intake_CHOICES = [('yes', 'yes'), ('no', 'no')]
    intake = models.CharField(max_length=255, choices=intake_CHOICES)
    questionnaire_answered_CHOICES = [('yes', 'yes'), ('no', 'no')]
    questionnaire_answered = models.CharField(max_length=255, choices=questionnaire_answered_CHOICES)

class DoctorDetails(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Age=models.IntegerField()
    Height=models.FloatField()
    Weight=models.FloatField()
    Experience=models.IntegerField()

class DoctorMoodDiary(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    mood_CHOICES=[('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),('5', '5'), ('6', '6'),('7', '7'), ('8', '8'),('9', '9'), ('10', '10')]
    mood = models.CharField(choices=mood_CHOICES)
    hours = models.CharField(max_length=255)
    physical_CHOICES = [('yes', 'yes'), ('no', 'no')]
    physical = models.CharField(max_length=255, choices=physical_CHOICES)
    relaxation_CHOICES = [('yes', 'yes'), ('no', 'no')]
    relaxation = models.CharField(max_length=255, choices=relaxation_CHOICES)
    support_CHOICES = [('yes', 'yes'), ('no', 'no')]
    support = models.CharField(max_length=255, choices=support_CHOICES)
    supportive_CHOICES = [('yes', 'yes'), ('no', 'no')]
    supportive = models.CharField(max_length=255, choices=supportive_CHOICES)
    patients = models.CharField()
    illness_CHOICES = [('yes', 'yes'), ('no', 'no')]
    illness = models.CharField(max_length=255, choices=illness_CHOICES)
    events_CHOICES = [('yes', 'yes'), ('no', 'no')]
    events = models.CharField(max_length=255, choices=events_CHOICES)
    menstrual_CHOICES = [('yes', 'yes'), ('no', 'no')]
    menstrual = models.CharField(max_length=255, choices=menstrual_CHOICES)
    today_CHOICES = [('yes', 'yes'), ('no', 'no')]
    today = models.CharField(max_length=255, choices=today_CHOICES)
    drugs_CHOICES = [('yes', 'yes'), ('no', 'no')]
    drugs = models.CharField(max_length=255, choices=drugs_CHOICES)

class predictions(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Age = models.PositiveIntegerField()
    Weight=models.FloatField()
    Height=models.FloatField()
    BloodPressure=models.PositiveIntegerField()
    Cholesterol=models.PositiveIntegerField()
    ExerciseHours=models.PositiveIntegerField()
    Smoking_CHOICES = [(1, 'Yes'),(0, 'No')]
    Smoking = models.PositiveIntegerField(max_length=255, choices=Smoking_CHOICES)
    AlcoholConsumption_CHOICES = [(1, 'Yes'),(0, 'No')]
    AlcoholConsumption = models.PositiveIntegerField(max_length=255, choices=AlcoholConsumption_CHOICES)
    Diet_CHOICES = [(1, 'Vegetarian'),(0, 'Non-Vegetarian')]
    Diet = models.PositiveIntegerField(max_length=255, choices=Diet_CHOICES)
    SleepHours=models.PositiveIntegerField()
    StressLevel_CHOICES = [(1, 'Medium'),(0, 'Low'),(2,'High')]
    StressLevel = models.PositiveIntegerField(max_length=255, choices=StressLevel_CHOICES)
    predictions_patient = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/health_predict_patients_finalized.joblib')
        self.predictions_patient  = ml_model.predict(
            [[self.Age, self.Weight, self.Height,self.BloodPressure,self.Cholesterol,self.ExerciseHours,self.Smoking,self.AlcoholConsumption,self.Diet,self.SleepHours,self.StressLevel]])
        return super().save(*args, *kwargs)
    
    class Meta:
         ordering = ['-date']
    
    def __str__(self):
        return self.Name