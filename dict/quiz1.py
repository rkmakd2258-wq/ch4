# 키를 결정하는 요소 : 중복X
# 장바구니에서 키는 상품명, 값은 수량
furuits = { '사과':3, '바나나':5, '딸기':2 }

# 딕셔너리[key] = 새로운 value
furuits['사과'] = 10

del furuits['바나나']
print(furuits)


test = {'수학':95}
test['영어'] = 88
test['국어'] = 100
print(test)


cafe = {'아메리카노':2000, '라떼':3000, '케이크':4500}
cafe['아메리카노'] = 2500
del cafe['케이크']
print(cafe)