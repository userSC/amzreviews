##
data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count%1000 == 0:  ###取餘數
			print(len(data))
print('讀取完成，共有',len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len+=len(d)
print('平均為',sum_len/len(data))

new = []
for d in data:
	if len(d)<100:
		new.append(d)
print('共有',len(new),'筆留言長度小於100')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆留言含good')
print(good[0])

good = [1 for d in data if 'good' in d]
print(good)
bad =['bad' in d for d in data]
print(bad)
