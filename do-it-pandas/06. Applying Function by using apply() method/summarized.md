# 06-1. 간단한 함수 만들기
### 사용자 함수 만들기
1. 주어진 숫자의 제곱을 반환하는 함수
```python
def my_sq(x):
    return x**2
```
2. 주어진 두 숫자의 평균을 구하는 함수
```python
def my_avg(x,y):
    return (x+y)/2
```
# 06-2. apply() 메서드 사용하기
### 데이터프레임에 함수 적용하기
1. 실습에 사용할 간단한 데이터프레임 만들기
``` python
import pandas as pd

df = pd.DataFrame({"a":[10,20,30],
                   "b":[20,30,40]})
print(df)
```
📝 실행결과
```
    a   b
0  10  20
1  20  30
2  30  40
```
## 시리즈에 함수 적용하기
### 시리즈에 함수 적용하기
1. 앞서 만든 데이터프레임에서 a열의 유형은 Series이다.
2. 데이터프레임의 첫 행 또한 Series 객체이다.
3. 시리즈에는 apply() 메서드를 제공한다. apply()를 활용하면 시리즈의 모든 요소에 지정한 함수를 적용할 수 있다.
```python
sq = df['a'].apply(my_sq) #apply()에 함수를 인수로 전달할 때는 함수를 실행하지 않으므로 소괄호를 붙이지 않는다.
print(sq)
```
📝 실행결과
```
0    100
1    400
2    900
Name: a, dtype: int64
```
### 사용자 함수 만들어 데이터 프레임에 적용하기
1. 두 개의 매개변수를 제곱하는 my_exp()생성
```python
def my_exp(x,e):
    return x ** e
```
2. 이 함수를 사용하려면 두 개의 매개변수를 전달해야함. 한 개만 전달 시 오류 발생
3. Series의 apply() 메서드에 함수를 전달할 때 첫 번째 매개변수에는 데이터 프레임이나 시리즈의 각 요솟값을 전달하지만 그 외의 매개변수에는 키워드 매개변수로 이름과 값을 전달해야함.
```python
ex = df['a'].apply(my_exp, e=2)
print(ex)
```
📝실행결과
```
0    100
1    400
2    900
Name: a, dtype: int64
```
## 데이터 프레임에 함수 적용하기
1. 하나의 값을 전달받아서 그대로 출력하는 함수 생성
```python
def print_me(x):
    print(x)
```
2. apply() 메서드로 함수를 열 단위로 적용하고 싶으면 axis 매개변수에 0 또는 "index"를 지정, 행 단위로 적용하고 싶다면 axis=1 또는 axis = "columns"를 전달
### 열 단위로 함수 적용하기
1. 열 단위로 apply()를 호출할 때 axis=0을 전달
```python
df.apply(print_me, axis =0)
```
📝실행결과
```
0    10
1    20
2    30
Name: a, dtype: int64
0    20
1    30
2    40
Name: b, dtype: int64
0
a	None
b	None
```
2. 세 숫자의 평균을 구하는 avg_3()함수 생성
```python
def avg3(x,y,z):
    return (x+y+z) / 3
```
3. 이 함수를 apply()로 데이터프레임에 적용하려고 하면 오류가 발생, 3개가 인수가 필요하지만 첫 번째 인수로 전체열이 전달됨
4. 전체 열을 첫번째 인수로 받은 후에 함수 안에서 각 값을 추출하도록 수정
```python
def avg_3_apply(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x+y+z) / 3
```
### 행 단위로 함수로 적용하기
1. 행 단위로 apply() 적용하는 법은 axis = 0을 전달하면 됨
2. 행의 전체 값을 받아서 2개의 값을 추출하고 평균을 구해야하므로 avg_3_apply 함수는 적용이 안 됨
3. avg_2_apply로 다시 작성
```python
def avg_2_apply(row):
    x = row.iloc[0]
    y = row.iloc[1]
    return (x+y) /2
```

# 06-3 람다 함수 사용하기
### 데이터프레임에 람다 함수 사용하기
1. 앞서 만든 my_sq() 함수를 다시 사용해도 되지만
```python
def my_sq(x):
    return x**2

df['a_sq'] = df['a'].apply(my_sq)
print(df)
```
2. 간단한 함수는 람다 함수로 정의해도 됨
```python
df['a_sq_lamb'] = df['a'].spply(lambda x: x**2)
print(df)
```

# 06-4 벡터화된 함수 사용하기
### 벡터화된 함수 사용하기
1. 데이터의 각 행 값이 2개이므로 다음과 같은 평균함수를 만들 수 있음
```python
def avg_2(x,y):
    return (x+y)/2
print(avg_2(df['a'], df['b']))
```
* 벡터화된 함수: 입력이 벡터(panda의 Series)여도 자동으로 각 요소별 계산이 되는 함수
* 두 개의 숫자 열에 더하기 연산을 적용하면 판다스와 넘파이 라이브러리가 자동으로 요소별 더하기 수행
* /2에서 2를 스칼라라고 하며 스칼라를 브로드캐스팅하고 각 요소를 스칼라값으로 나누는 방식으로 작동한다.
```
스칼라의 브로드캐스팅에 대한 이해를 위한 예시 그림
브로드캐스팅한다는 것은 스칼라 혹은 작은 배열을 자동으로 큰 배열에 맞춰 연산한다는 의미

벡터: [ a1, a2, a3, a4 ]
스칼라: 2

브로드캐스트: [ 2, 2, 2, 2 ]
연산 결과: [ a1/2, a2/2, a3/2, a4/2 ]

```
2. 벡터화할 수 없는 계산을 수행하는 함수
```python
import numpy as np

def avg_2_mod (x,y):
    if (x == 20):
        return (np.nan)
    else:
      return (x+y) / 2
```
* if문에 벡터가 전달될 수 없는데 전달되므로 오류가 발생함
```
df['a'] == 20
# 결과: [False, True, False] ← 벡터

if df['a'] == 20:
    # ❌ ValueError: The truth value of a Series is ambiguous
파이썬의 if문은 단일 True/False 값만 이용할 수 있는데, 벡터를 넣으면 오류가 발생함
```

## 넘파이와 넘바로 벡터화 하기
### 넘파이로 벡터화하기
1. np.vectorize()에 벡터화하려는 함수를 전달
```python
import numpy as np

avg_2_mod_vec = np.vectorize(avg_2_mod)
print(avg_2_mod_vec(df['a'], df['b']))
```
📝실행 결과
```
[15. nan 35.]
```
2. 파이썬의 데코레이터로 새 함수를 만들지 않고도 함수를 자동으로 벡터화할 수 있음
```python
@np.vectorize
def v_avg_2_mod(x,y):
    if (x==20):
        return np.nan
    else:
        return (x+y) / 2

print(v_avg_2_mod(df['a'],df['b']))
```

###넘바로 벡터화 하기
1. 넘바 라이브러리는 배열에 적용하는 수학 계산을 최적화하도록 설계되었습니다.
```python
import numba
@numba.vectorize
def v_avg_2_numba(x,y):
    if (int(x) == 20): #자료형 정보를 추가해줘야한다.
        return (np.nan)
    else:
        return (x+y) / 2
```
2. numba 라이브러리는 계산 최적화에 특화된 라이브러리이므로 판다스 객체를 처리하는 기능은 없다.
3. 시리즈 객체의 value 속성을 사용하여 데이터를 넘파이 ndarray 배열 형식으로 전당해야한다.
```python
print(v_avg_numba(df['a'].values, df['b'].values))
```

