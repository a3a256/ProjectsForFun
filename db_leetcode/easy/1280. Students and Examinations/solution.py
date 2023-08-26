import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    mp = dict()
    dp = dict()
    students.sort_values('student_id', inplace=True)
    subjects.sort_values('subject_name', inplace=True)
    for i, j in zip(students['student_name'].values, students['student_id'].values):
        dp[j] = i
        mp[j] = dict()
        for k in subjects['subject_name'].values:
            mp[j][k] = 0

    for i in range(len(examinations)):
        sid = examinations.iloc[i, 0]
        sub = examinations.iloc[i, 1]
        mp[sid][sub] += 1
    
    dd = {'student_id': [],
            'student_name': [],
            'subject_name': [],
            'attended_exams': []}

    for i in mp:
        for j in mp[i]:
            dd['student_id'] += [i]
            dd['student_name'] += [dp[i]]
            dd['subject_name'] += [j]
            dd['attended_exams'] += [mp[i][j]]
    
    return pd.DataFrame(dd)
