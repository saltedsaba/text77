#找出班上成績問題 #已完成 #
total = set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
ef = set(['John','Mary','Fiona','Claire','Ben','Bill'])
mf = set(['Mary','Fiona','Claire','Eva','Ben'])

print("英文與數學都及格:",ef & mf)
print("數學不及格:",total - mf)
print("英文及格且數學不及格:",total&ef-mf )