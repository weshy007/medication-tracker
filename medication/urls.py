from django.urls import path

from . import views

urlpatterns = [
    path('medications/', views.MedicationListView.as_view(), name='medication-list'),
    path('medications/create/', views.MedicationCreateView.as_view(), name='medication-create'),
    path('medications/<int:pk>/update/', views.MedicationUpdateView.as_view(), name='medication-update'),
    path('medications/<int:pk>/delete/', views.MedicationDeleteView.as_view(), name='medication-delete'),
    path('medication_logs/', views.MedicationLogView.as_view(), name='medication-log'),
    path('medication_logs/create/', views.MedicationLogCreateView.as_view(), name='medication-log-create'),
    path('reminders/create/', views.ReminderCreateView.as_view(), name='reminder-create'),
]
