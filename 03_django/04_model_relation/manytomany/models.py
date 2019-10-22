from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients') # 중개모델을 통해서 의사로 접근
    # patient(manytomanyfield를 가짐)만이 _set 없이 직접 참조 가능

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델 추가
# Doctor, Patient와 각각 1:N의 관계
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'