import numpy as np
import csv

# CSV 파일 생성
data = [
    ["이름", "수학", "영어", "파이썬"],
    ["홍길동", 85, 78, 92],
    ["스텔라", 89, 85, 98],
    ["촬리", 91, 89, 95],
    ["데이비드", 72, 75, 70],
    ["앨리스", 88, 92, 85]
]

filename = 'data.csv'

with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# CSV 파일 읽기
with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# 넘파이 배열로 변환
header = data[0]
data_array = np.array(data[1:])

# 이름과 점수를 추출
names = data_array[:, 0]
scores = data_array[:, 1:].astype(np.float64)

math_scores = scores[:, 0]
english_scores = scores[:, 1]
python_scores = scores[:, 2]

def calculate_statistics(scores):
    return {
        'Mean': np.mean(scores),
        'Std Dev': np.std(scores),
        'Max': np.max(scores),
        'Min': np.min(scores)
    }

math_stats = calculate_statistics(math_scores)
english_stats = calculate_statistics(english_scores)
python_stats = calculate_statistics(python_scores)

def highest_scorer(scores, names):
    return names[np.argmax(scores)]

top_math_student = highest_scorer(math_scores, names)
top_english_student = highest_scorer(english_scores, names)
top_python_student = highest_scorer(python_scores, names)

print("수학 -", math_stats)
print("수학에서 가장 높은 학생:", top_math_student)
print("영어 -", english_stats)
print("영어에서 가장 높은 학생:", top_english_student)
print("파이썬 -", python_stats)
print("파이썬에서 가장 높은 학생:", top_python_student)

# 총점 계산
total_scores = np.sum(scores, axis=1)

# 전체 학생들의 총점 평균 계산
mean_total_score = np.mean(total_scores)

# 총점이 평균보다 높은 학생들 구하기
above_average_mask = total_scores > mean_total_score
students_above_average = names[above_average_mask]

print("전체 점수가 평균보다 높은 학생들:", ', '.join(students_above_average))

# 수학 과목에서 점수가 80점 이상인 학생들 이름과 점수 출력하기 
math_above_80_mask = math_scores >= 80
students_math_above_80 = names[math_above_80_mask]
math_scores_above_80 = math_scores[math_above_80_mask]

print("수학 점수가 80점 이상인 학생들:")
for name, score in zip(students_math_above_80, math_scores_above_80):
    print(f"{name}: {score}")

sorted_indices = np.argsort(total_scores)[::-1]
sorted_names = names[sorted_indices]
sorted_scores = scores[sorted_indices]
sorted_total_scores = total_scores[sorted_indices]

sorted_data = np.column_stack((sorted_names, sorted_scores, sorted_total_scores))

with open('sorted_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['이름', '수학', '영어', '파이썬', '총점'])
    writer.writerows(sorted_data)

print("'sorted_data.csv' 파일에 저장됨.")

# sorted_data.csv 파일 읽고 출력하기
sorted_filename = 'sorted_data.csv'

with open(sorted_filename, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    sorted_data = list(reader)

print("sorted_data.csv 내용:")
for row in sorted_data:
    print(row)