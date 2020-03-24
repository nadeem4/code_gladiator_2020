n = int(input())

req_qty = str(input()).split(" ")

qty =  str(input()).split(" ")

powerpuffgirl_cnt = []

for i in range(0, n):
    powerpuffgirl_cnt.append( int(qty[i])//int(req_qty[i]))

print(min(powerpuffgirl_cnt))
