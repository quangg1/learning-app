from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from web_app.serializers import SubmissionSerializer
from web_app.models import Submission, Exercise, User
from dev_core.security.export import (
    MIX_PERMISSION_AUTH, 
    MIX_AUTHEN_TSJ, 
    UNTHENTHROTTLE, 
    MIX_PERMISSION_ANY
)

from .eval_code_dev import GradeCodeSubmission
from utils.res_util import (
    ResUtil
)

class SubmissionAV(APIView):
    permission_classes = MIX_PERMISSION_AUTH
    authentication_classes = MIX_AUTHEN_TSJ
    http_method_names=['post', 'get']
    name_api = 'Submission API View'


    def post(self, request, *args, **kwargs):
        exercise_id = request.data.get('exerciseId')
        try:
            exercise = Exercise.objects.get(id=exercise_id)
        except Exercise.DoesNotExist:
            return Response({'error': 'Exercise not found'}, status=status.HTTP_404_NOT_FOUND)
        
        

        serializer = SubmissionSerializer(data={
            'code': request.data.get('code'),
            'exercise': exercise.id,
            'user': request.user.id
        })
        if serializer.is_valid():
            user = serializer.validated_data['user']
            exercise = serializer.validated_data['exercise']
            # Check for existing submission
            try:
                existing_submission = Submission.objects.get(user=user, exercise=exercise)
                existing_submission.code = serializer.validated_data['code']
                #* Submit code and grade
                result_submit_code = GradeCodeSubmission.grade_code(existing_submission.code, exercise.id)
                if result_submit_code is not None:
                    existing_submission.grade = result_submit_code.get('grade')
                existing_submission.save()
                # print('existing submission')
                return Response(ResUtil.res_success(
                    name_res=self.name_api,
                    data=result_submit_code
                ))
            except Submission.DoesNotExist:
                # Create a new submission if none exists
                submission = serializer.save()
                result_submit_code = GradeCodeSubmission.grade_code(submission.code, exercise.id)
                if result_submit_code is not None:
                    submission.grade = result_submit_code.get('grade')
                submission.save()
                # print('new submission')
                return Response(ResUtil.res_success(
                    name_res=self.name_api,
                    data=result_submit_code
                ))
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        #* Ranking submission
        print('get')
        try:
            return Response(ResUtil.res_success(
                name_res=self.name_api,
                data={
                    'ranking': self.sum_grade_of_all_user()
                }
            ))
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def sum_grade_of_all_user(self):
        try:
            all_users = User.objects.all()
            # print(all_users)
            list_grade = []
            for user in all_users:
                submissions = Submission.objects.select_related('user').filter(user=user)
                sum_grade = 0
                count_exercise = 0
                for submission in submissions:
                    sum_grade += submission.grade
                    if submission.grade == 100:
                        count_exercise += 1
                list_grade.append({
                    'full_name': user.full_name,
                    'username': user.username,
                    'sum_grade': sum_grade,
                    'done_exercise': count_exercise,
                })
            list_grade = sorted(list_grade, key=lambda x: x['sum_grade'], reverse=True)
            # print(list_grade)
            return list_grade
        except Exception as e:
            return {'error': str(e)}

        

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = MIX_PERMISSION_ANY

        return [permission() for permission in self.permission_classes]


    def get_throttles(self):
        if self.request.method == 'POST':
            self.throttle_classes = UNTHENTHROTTLE['POST']
        elif self.request.method == 'GET':
            self.throttle_classes = UNTHENTHROTTLE['GET']

        return [throttle() for throttle in self.throttle_classes]