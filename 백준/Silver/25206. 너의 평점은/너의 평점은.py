import sys
input = sys.stdin.readline
grade = {'A+': 4.5, 'A0': 4.0, 
         'B+': 3.5, 'B0': 3.0, 
         'C+': 2.5, 'C0': 2.0,
         'D+': 1.5, 'D0': 1.0, 
         'F': 0.0} # 과목평점점
score = 0 # 학점 * 과목평점
credit_total = 0 # 총 학점
for i in range(20):
    subject, credit, grd = input().split()
    if grd == 'P':
        continue
    score += float(credit) * grade[grd]
    credit_total += float(credit)
print('%.6f' % (score / credit_total))