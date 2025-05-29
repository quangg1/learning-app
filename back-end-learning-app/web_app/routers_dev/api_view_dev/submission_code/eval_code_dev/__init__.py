from .eval_code import EvalCode
from .test_case import ALL_TEST_CASES_PYTHON_FRESHER_2024


class GradeCodeSubmission:
    

    @staticmethod
    def load_test_case(exercise_id: int):
        return ALL_TEST_CASES_PYTHON_FRESHER_2024.get(str(exercise_id))
    
    @staticmethod
    def grade_code(code: str, exercise_id: int):
        try:
            test_cases = GradeCodeSubmission.load_test_case(exercise_id)
            # print(code, exercise_id)
            if test_cases is not  None:
                _eval = EvalCode(code)
                count_pass = []
                for test_case in test_cases:
                    if test_case['input'] is not None:
                        if _eval.run_func_code(test_case['input']) == test_case['output']:
                            count_pass.append(1)
                        else:
                            count_pass.append(0)
                    else:
                        if _eval.run_func_code() == test_case['output']:
                            count_pass.append(1)
                        else:
                            count_pass.append(0)
                return {
                    'grade': sum(count_pass) / len(test_cases) * 100,
                    'total_test_cases': len(test_cases),
                    'pass_test_cases': count_pass
                }
            return {
                'grade': 0,
                'total_test_cases': 0,
                'pass_test_cases': count_pass
            }
        except Exception as e:
            print(e)
            return {
                'grade': 0,
                'total_test_cases': 0,
                'pass_test_cases': count_pass
            }
                    