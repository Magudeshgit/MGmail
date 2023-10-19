from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

@api_view(('POST',))
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def MGMail(request):
    subject = request.data.get('subject')
    content = request.data.get('content')
    print(subject,content)
    email = send_mail(
        subject,
        content,
        settings.EMAIL_HOST_USER,
        [request.user.email],
        fail_silently=False,
    ) 
    # email = EmailMessage(
    #     subject=subject,
    #     body=content,
    #     from_email=settings.EMAIL_HOST_USER,
    #     to=["hemanthmailaccess@gmail.com"],
    #     reply_to=["hemanthmailaccess@gmail.com"],
    #     headers={'Content-Type': 'text/plain'},
    # )

    return Response({'data': 'success'})