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
    # mail_stat=mailstat.objects.get(user=request.user)
    
    
    subject = request.data.get('subject')
    body = request.data.get('body')
    toAddress = request.data.get('toAddress')
    
    if toAddress == None:
        return Response({'success': False, 'detail': "To Address not provided"})
    print(subject,body, toAddress)
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [toAddress],
        fail_silently=False,
    ) 
    
    # mail_stat.count += 1
    # mail_stat.save()
    
    return Response({'success': True, 'detail': "Mail sent"})