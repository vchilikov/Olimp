s = '\n'.join(input() for _ in range(int(input()))).replace('OO', '++', 1)
print('YES\n' + s if s.find('++') >= 0 else 'NO')
