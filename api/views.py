from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from .models import mailstat

@api_view(('POST',))
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def MGMail(request):
    mail_stat=mailstat.objects.get(user=request.user)
    print(mail_stat,mail_stat.count)
    subject = request.data.get('subject')
    content = request.data.get('content')
    email = send_mail(
        subject,
        content,
        settings.EMAIL_HOST_USER,
        [request.user.email],
        fail_silently=False,
    ) 
    mail_stat.count +=1
    mail_stat.save()
    return Response({'data': 'success'})