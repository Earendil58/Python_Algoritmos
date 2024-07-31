v = [4,2,7,9,11,5]
n = len(v)


print(f'El vector al principio: {v}')

i = 0

for j in range(i+1, n):
    print(f'Esto es v[i]: {v[i]} y esto es v[j]: {v[j]}')
    if v[i] > v[j]:
        v[i], v[j] = v[j], v[i]
        print(f'Esto es v[i]: {v[i]} y esto es v[j]: {v[j]} - entrada en if')




print(f'El vector al final: {v}')
