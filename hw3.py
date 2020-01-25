def unification(query,standard):
	unify = {}
	disjunct = query.split("|")
	##print(disjunct)
	for i in range(len(disjunct)):
			pos = disjunct[i].index('(')
			pred = disjunct[i][:pos]
			if pred[0] == '~':
				pred = pred[1:]
			else:
				pred = '~' + pred
			##print(pred)
			for j in range(len(standard)):
				if pred in standard[j]:
					if i not in unify:
						unify[i] = [j]
					else:
						unify[i].append(j)
	return unify


def resolution(sentence1,sentence2,predicate):
	answerf1 = ""
	answerf2 = ""
	finalans = ""
	newlist1 = []
	newlist2 = []
	flag = True
	u = {}
	predicate = predicate.strip()
	res1 = []
	res2 = []
	s1 = sentence1.split("|")
	s2 = sentence2.split("|")
	if '(' in predicate:
		predicate = predicate[:predicate.index('(')]
	if predicate[0] == '~':
		npredicate = predicate[1:]
	else:
		npredicate = '~' + predicate
	#print(predicate, npredicate)
	for i in range(len(s1)):
		if npredicate == s1[i][:s1[i].index('(')]:
			res1.append(i)
	for j in range(len(s2)):
		if predicate == s2[j][:s2[j].index('(')]:
			res2.append(j)

	#print(res1,res2)
	combined = [(r1,r2) for r1 in res1 for r2 in res2]
	##print(combined)
	for i,j in combined:
		##print(i,j)
		##print(s1[i],s2[j])
		
		xx = s1[i].index('(')
		answer1 = s1[i][:xx+1]
		yy = s1[i][xx+1:-1]
		xxx = s2[j].index('(')
		yyy = s2[j][xxx+1:-1]

		answer2 = s2[j][:xxx+1]
		##print(yy,yyy)
		yy = yy.split(",")
		yyy = yyy.split(",")
				
		if len(yy) != len(yyy):
			return {}
		else:

			for k in range(len(yy)):

				if yy[k] not in u and yy[k][0].islower() and not yyy[k][0].islower():
					#yy[i] = yyy[i]
					u[yy[k]] = yyy[k]

				elif (yy[k] in u and u[yy[k]] == yyy[k]) or (yyy[k] in u and u[yyy[k]] == yy[k]):
					pass

				
				elif yyy[k] not in u and yyy[k][0].islower() and not yy[k][0].islower():
					#yyy[i] = yy[i]
					u[yyy[k]] = yy[k]
				
				elif not yy[k][0].islower()	and not yyy[k][0].islower() and yy[k] == yyy[k]:
					pass

				elif yy[k][0].islower() and yyy[k][0].islower():
					if yy[k] in u and u[yy[k]].islower() == False:
						u[yyy[k]] = u[yy[k]]
					elif yy[k] in u and u[yy[k]].islower():
						u[yy[k]] = yyy[k]
					elif yy[k] not in u:
						u[yy[k]] = yyy[k]
					else:
						flag = False
						break
				else:
					flag = False
					break
					
				##print(yy,yyy)
			
			##print(u)
			if flag == True:
				##print("hi")

				s1.pop(i)
				s2.pop(j)
				##print(s1)
				##print(s2)
				
				
				for l in range(len(s1)):
					index1 = s1[l].index('(')
					answer1 = s1[l][:index1+1]
					s1[l] = s1[l][index1 + 1:-1]
					s1[l] = s1[l].split(",")

					for m in range(len(s1[l])):
						if s1[l][m] in u:
							s1[l][m] = u[s1[l][m]]
							answer1+= s1[l][m]
							if m < len(s1[l]) - 1:
								answer1 += ','
							else:
								answer1 += ')'

						else:
							answer1+= s1[l][m]
							if m < len(s1[l]) - 1:
								answer1 += ','
							else:
								answer1 += ')'

					answerf1 += answer1 + "|"	

				for l in range(len(s2)):
					index2 = s2[l].index('(')
					answer2 = s2[l][:index2+1]
					s2[l] = s2[l][index2 + 1:-1]
					s2[l] = s2[l].split(",")

					for m in range(len(s2[l])):
						if s2[l][m] in u:
							s2[l][m] = u[s2[l][m]]
							answer2+= s2[l][m]
							if m < len(s2[l]) - 1:
								answer2 += ','
							else:
								answer2 += ')'

						else:
							answer2+= s2[l][m]
							if m < len(s2[l]) - 1:
								answer2 += ','
							else:
								answer2 += ')'

					answerf2 += answer2 + "|"			

				if len(s2) == 0:
					finalans = answerf1[:-1]
				else:
					finalans = answerf1 + answerf2[:-1]


				return finalans
						
				
					#if k in s2[x]:
						#newlist2 = [w.replace(k, u[k]) for w in s2]
				##print(s1)
				##print(newlist2)
				#mystring = "|".join(newlist1)
				##print(mystring)

















queries = []
knowledge_base = []
standard = []
cnf_kb = []
predicate = {}
standard = []



inputfile = open("input.txt")
inputfile_string = inputfile.read().split('\n')
query_no = int(inputfile_string[0])
for i in range(query_no):
	a = inputfile_string[1+i]
	queries.append(a)
##print(query_no)
##print(queries)
kb_size = int(inputfile_string[1+query_no])
##print(kb_size)
for j in range(kb_size):
	b = inputfile_string[2 + query_no + j]
	knowledge_base.append(b)
#print(knowledge_base)
#print('\n\n')
for i in range(len(knowledge_base)):
	if "=>" in knowledge_base[i]:
		##print(knowledge_base[i])
		x = knowledge_base[i].split("=>")
		ans = ""
		xx = x[0].split("&")
		for i in range(len(xx)):
			xx[i] = xx[i].strip()
			if "~" in xx[i]:
				xx[i] = xx[i][1:]
			else:
				xx[i] = '~' + xx[i].strip()
			ans += xx[i] + "|"
		ans += x[1].strip()
		##print(ans)
		cnf_kb.append(ans)
		

	elif "&" in knowledge_base[i]:
		y = knowledge_base[i].split("&")
		for i in range(len(y)):
			cnf_kb.append(y[i].strip())
		

	else:
		cnf_kb.append(knowledge_base[i])
##print(cnf_kb)

#print('\n\n')
for i in range(len(cnf_kb)):
	x = cnf_kb[i].split("|")
	for j in range(len(x)):
		#if x[i][0] == '~':
		#predicate[i].append()
		y = x[j].split("(")[0]
		##print(y)
		if i not in predicate:
			predicate[i] = [y]
		else:
			predicate[i].append(y)
##print(predicate)


for i in range(len(cnf_kb)):
	answer = ""
	xx = cnf_kb[i].split("|")
	##print(xx)
	for j in range(len(xx)):

		#yy = xx.index('(')
		##print(xx[j])
		yy = xx[j].index('(')
		a = xx[j][:yy+1]
		b = xx[j][yy+1:-1]
		b = b.split(",")
		for k in range(len(b)):
			##print(b[k])
			if len(b[k]) == 1 and b[k].islower():
				b[k] = b[k] + str(i+1)
			a+=b[k]
			if k < len(b)-1:
				a += ','
			else:
				a += ')'				
				#result = a + b[k] + 


		answer += a + "|"
	standard.append(answer[:-1])
		#standard.append(a)
#print(standard)
#print('\n\n')
#print('\n\n')

def fn(query, predicate, standard,depth):

	if not query or depth == 0:
		return False

			
	uni = unification(query,predicate)
	for i in range(len(uni)):
		
		for j in range(len(uni[i])):
			#print(uni[i][j], standard[uni[i][j]])
			r = resolution(standard[uni[i][j]],query,query.split('|')[i])
			#print("HI:",r)
			if r == "":
				return True
			else:
				ans = fn(r, predicate, standard,depth - 1)
				if ans == True:
					return True
	return False

hi = []
for x in range(len(queries)):
	if queries[x][0] == '~':
		queries[x] = queries[x][1:]
	else:
		queries[x] = '~' + queries[x]
	new_standard = standard[:]
	new_standard.append(queries[x])
	new_predicate = predicate.copy()
	new_predicate[len(new_predicate)] = [queries[x][:queries[x].index('(')]]	
	hi.append(fn(queries[x], new_predicate, new_standard,len(new_standard)))
#print(hi)
#for i in range(len(hi)):
	#print(str(hi[i]).upper())
	
with open('output.txt','w') as f:
    for i in range(len(hi)):
        if i == len(hi)-1:
            f.write(str(hi[i]).upper())
        else:
            f.write(str(hi[i]).upper()+"\n")