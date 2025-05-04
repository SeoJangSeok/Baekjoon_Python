def solution(rank, attendance):
    student = []
    for i, b in enumerate(attendance):
        if b == True:
            student.append(rank[i])
    student.sort()
    return 10000 * rank.index(student[0]) + 100 * rank.index(student[1]) + rank.index(student[2])