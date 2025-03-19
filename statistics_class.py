import math  # 수학 함수들을 사용하기 위해 math 모듈을 가져옴


class Statistics:
    # 숫자 리스트로부터 평균, 표준편차, 최대, 최소를 계산하는 클래스
    
    def __init__(self, data):
        """
        클래스가 생성될 때(초기화될 때) 데이터를 받아 저장함
        self.data는 클래스 내부에서 데이터를 계속 사용할 수 있게 해줌
        """

        if not data:
            raise ValueError("데이터 리스트가 비어있습니다.")
        # 데이터가 없을 경우 오류를 발생시켜 잘못된 사용을 방지함

        self.data = data

    def mean(self):
        """
        평균(산술평균)을 계산함
        = 모든 값을 더한 뒤 데이터 개수로 나눔
        """

        return sum(self.data) / len(self.data)

    def std_dev(self):
        """
        표준편차(Standard Deviation)를 계산함
        - 데이터가 평균으로부터 얼마나 떨어져 있는지를 나타내는 값임
        - 공식: √(Σ(x - 평균)^2 / N)
        """

        mean = self.mean() # 먼저 평균을 구함
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        # 분산(variance): 각 값에서 평균을 뺀 값을 제곱한 후 평균을 낸 것
        return math.sqrt(variance) # 표준편차는 분산의 제곱근

    def maximum(self):
        """데이터 중 최댓값을 반환함"""
        return max(self.data)

    def minimum(self):
        """데이터 중 최솟값을 반환함"""
        return min(self.data)

    def summary(self):
        """통계 요약 결과를 딕셔너리 형태로 반환함"""

        return {
            '평균': self.mean(),
            '표준편차': self.std_dev(),
            '최댓값': self.maximum(),
            '최솟값': self.minimum()
        }

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50] # 샘플 데이터
    stats = Statistics(numbers) # Statistics 클래스 객체 생성
    
    print("통계 요약:")
    summary = stats.summary() # 요약값을 딕셔너리로 받음
    for key, value in summary.items():
        print(f"{key}: {value:.2f}") # 소수점 둘째 자리까지 출력
