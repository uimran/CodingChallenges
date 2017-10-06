# the list 'students' is a nested list with all the student names with their repsective scores
students=[]
# the list 'scores' holds all the scores of students
scores=[]
# the list 'first_low' holds the first lowest scores
first_low=[]
# the list 'second_low' holds the second lowest scores
second_low=[]
for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    # the name and score of a student are appended as a list in the list students
    students.append([name,score])
    scores.append(score)
for item in students:
# item[1] holds the score value for a student (item[0] holds the name), if it is the lowest in the list scores, it will be added to the first_low list
    if item[1] == min(scores):
        first_low.append(item)
# In order to find the second lowest grade, it is essential to first get rid of the first lowest scores from the lists students and scores. Because once it is removed, it will then consider the lowest from both the lists again (this will actually be the second lowest score now)
for item in first_low:
    del students[students.index(item)]
    del scores[scores.index(item[1])]
for item in students:
# item[1] holds the score value for a student (item[0] holds the name), if it is the lowest in the list scores, it will be added to the second_low list (since first lowest already removed)
    if item[1] == min(scores):
        second_low.append(item)
second_low.sort()
for name in second_low:
    print name[0]
