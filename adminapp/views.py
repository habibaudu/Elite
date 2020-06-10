import jwt
from django.conf import settings
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED)
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password
from adminapp.models import (Admin)
from adminapp.serializer import (LoginSerializer, UsersDetailsSerializer)
from utils.helpers import format_response
from django.utils import timezone
from adminapp.permissions import IsAdmin
from users_app.models import (User)
from datetime import datetime, date,  timedelta
from dateutil.relativedelta import relativedelta

class AdminLoginViewSet(viewsets.ViewSet):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return format_response(error=serializer.errors,
                                   status=HTTP_400_BAD_REQUEST)

        password = serializer.data['password']
        username = serializer.data['username']

        admin = Admin.objects.filter(username=username).first()

        if not admin:
            return format_response(error="Invalid username or password",
                                   status=HTTP_401_UNAUTHORIZED)

        valid_password = check_password(password,admin.password)

        if not valid_password:
            return format_response(error="invalid username or password",
                                    status=HTTP_401_UNAUTHORIZED)

        admin.last_login =timezone.now()

        token =jwt.encode(
            {
                "uid":admin.id,
                "iat":settings.JWT_SETTINGS["ISS_AT"](),
                "exp":settings.JWT_SETTINGS["EXP_AT"]()
            },settings.SECRET_KEY)

        return format_response(
                               token=token,
                               message="Your login was successful",
                               role=admin.role.name,
                               status=HTTP_200_OK)

class ViewUserViewSet(viewsets.ViewSet):
    serializer_class = UsersDetailsSerializer
    permission_classes = (IsAdmin,)
    today = timezone.now()
    this_month = {}
    last_three_month = {}
    this_year = {}
    m = datetime.now().month
    y = datetime.now().year
    d = datetime.now().day

    def list(self,request):
        period = request.query_params.get("period")
        if period == 'this_month':
            
            d1 = date(self.y, self.m, 1)
            d2 = date(self.y, self.m, self.d)
            delta = d2 - d1

            dates_in_this_month=[(d1 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]
            
            query_set = User.objects.all()
            query_for_this_month = User.objects.filter(created_at__year=self.today.year,
                                            created_at__month = self.today.month)
            print(dates_in_this_month)
            for dt in dates_in_this_month:
                counter = 0
                for q in query_for_this_month:
                    if str(dt) == str(q.created_at.date()):
                        counter +=1
                self.this_month[dt]=counter

            serializer = self.serializer_class(query_for_this_month,many=True)
            return format_response(data=serializer.data,
                                message="All users for the month retrieved",
                                this_month=self.this_month,
                                status=HTTP_200_OK)

        if period == 'this_year':
            query_set = User.objects.filter(created_at__year=self.today.year)
            d1 = date(self.y, 1, 1)
            d2 = date(self.y, self.m, self.d)
            delta = d2 - d1
            dates_since_this_year = \
                [(d1 + timedelta(days = i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]
            for dt in dates_since_this_year:
                counter = 0
                for q in query_set:
                    if str(dt) == str(q.created_at.date()):
                        counter +=1
                self.this_year[dt]=counter
            serializer = self.serializer_class(query_set,many=True)
            return format_response(data=serializer.data,
                                   message="All users for the year retrieved",
                                   this_year = self.this_year,
                                   status=HTTP_200_OK)

        if period =="three_months":
            today = self.today
            three_months = relativedelta(months=3)
            last_three_months= today - three_months
            query_set = User.objects.filter(created_at__gte=last_three_months)

            d1 = date(self.y,self.m,self.d)
            if self.m - 3 == 0:
                d2 = date(self.y-1,12,self.d)
            elif self.m-3 == -1:
                d2 = date(self.y-1,11,self.d)

            elif self.m -3 == -2:
                d2 = date(self.y-1,10,self.d)
            else: 
                d2 = date(self.y,self.m-3,self.d)
            delta = d1 - d2
            last_three_months_data = \
                [(d2 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]
            
            for dt in last_three_months_data:
                counter = 0
                for q in query_set:
                    if str(dt) == str(q.created_at.date()):
                        counter += 1
                self.last_three_month[dt]=counter
            serializer = self.serializer_class(query_set, many=True)
            return format_response(data=serializer.data,
                                   message="users registered for the last three month retrieved",
                                   last_three_month=self.last_three_month,
                                   status=HTTP_200_OK)
