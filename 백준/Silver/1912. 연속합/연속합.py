n = int(input())
hap_list = list(map(int, input().split()))

for i in range(1, n):
    hap_list[i]  = max(hap_list[i], hap_list[i] + hap_list[i-1])
    
print(max(hap_list))