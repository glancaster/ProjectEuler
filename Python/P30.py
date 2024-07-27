
res = []
nums = []
for i in range(2,pow(9,5)*5+1):
	nums.append([int(s) for s in str(i)])


for n in nums:
	sumi = sum([pow(m,5) for m in n])
	i = int("".join([str(l) for l in n]))
	print(sumi,i)
	if sumi == i:
		res.append(i)

print(res)
print(sum(res))

