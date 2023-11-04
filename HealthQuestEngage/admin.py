from django.contrib import admin
from .models import Question,AnswerOption,UserOtherInfo,UserOtherInfoDoctor,AppointmentDetails,UserProfileScore,IntakeForm,ReportDetails,DoctorDetails,predictions

class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 0  # set to 0; we'll manage the count dynamically

    def get_formset(self, request, obj=None, **kwargs):
        # Adjust the extra attribute based on the option_count of the Question instance
        if obj:
            self.extra = obj.option_count
        return super(AnswerOptionInline, self).get_formset(request, obj, **kwargs)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerOptionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserOtherInfo)
admin.site.register(UserOtherInfoDoctor)
admin.site.register(AppointmentDetails)
admin.site.register(UserProfileScore)
admin.site.register(IntakeForm)
admin.site.register(ReportDetails)
admin.site.register(DoctorDetails)

class predictionAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Age', 'Weight', 'Height', 'BloodPressure','Cholesterol','ExerciseHours','Smoking','AlcoholConsumption','Diet','SleepHours','StressLevel')
admin.site.register(predictions, predictionAdmin)
