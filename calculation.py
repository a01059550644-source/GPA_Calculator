class GpaManager:
    def __init__(self):
        self.total_credits = 0
        self.total_points = 0.0

    def calculate_future_gpa(self, current_gpa, target_gpa, total_graduation_credits, earned_credits):
        remaining_credits = total_graduation_credits - earned_credits
        
        if remaining_credits <= 0:
            return "이미 졸업 이수 학점을 모두 채우셨거나 초과했습니다."
            
        required_gpa = (target_gpa * total_graduation_credits - current_gpa * earned_credits) / remaining_credits
        
        if required_gpa > 4.5:
            return f"남은 학점 동안 학점 {required_gpa:.2f}점이 필요합니다. (현실적으로 달성 불가능, 목표 수정 필요)"
        elif required_gpa <= 0:
            return f"이미 목표치에 도달할 수 있는 안정권입니다! 지금처럼만 유지하세요."
        else:
            return f"목표 달성을 위해 남은 {remaining_credits}학점 동안 평균 학점 {required_gpa:.2f}점 이상을 받으셔야 합니다."

    def run(self):
        print("========== 학점 계산 시스템 ==========")
        
        while True:
            try:
                user_input = input("과목이 몇 학점인지 입력하세요 (입력을 끝내려면 'q' 입력): ")
                if user_input.lower() == 'q':
                    break
                    
                credit = int(user_input)
                grade_point = float(input("해당 과목의 학점(0.0 ~ 4.5)을 입력하세요: "))
                
                if credit <= 0 or not (0.0 <= grade_point <= 4.5):
                    print("잘못된 범위를 입력하였습니다. 다시 입력해주세요.\n")
                    continue
                
                self.total_credits += credit
                self.total_points += (credit * grade_point)
                print(f"현재 총 {self.total_credits}학점 등록됨\n")
                
            except ValueError:
                print("종료를 원하시면 'q'를 입력해야 합니다.\n")

        if self.total_credits == 0:
            print("입력된 성적 데이터가 없어 프로그램을 종료합니다.")
            return

        current_gpa = self.total_points / self.total_credits

        print("\n-------------------------------------------------------")
        print(f"현재까지의 총 이수 학점: {self.total_credits} 학점")
        print(f"현재 학기 평균 학점: {current_gpa:.2f} / 4.5")
        print("-------------------------------------------------------\n")

        print("======== 졸업 학점 목표 달성 시뮬레이션 ========")
        try:
            target_gpa = float(input("1. 최종 졸업 목표 학점(0.0 ~ 4.5)을 입력하세요: "))
            total_graduation_credits = int(input("2. 졸업에 필요한 총 이수 학점(예: 140)을 입력하세요: "))
            
            if not (0.0 <= target_gpa <= 4.5) or total_graduation_credits <= self.total_credits:
                print("목표 학점이 범위를 벗어났거나, 졸업 총 학점이 현재 이수 학점보다 작습니다.")
                return
        except ValueError:
            print("올바른 숫자를 입력해야 합니다.")
            return

        prediction_result = self.calculate_future_gpa(
            current_gpa, target_gpa, total_graduation_credits, self.total_credits
        )

        print("\n===================== 최종 계산 ======================")
        print(prediction_result)
        print("=======================================================")

manager = GpaManager()
manager.run()
