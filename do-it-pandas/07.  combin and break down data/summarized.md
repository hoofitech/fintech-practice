# 07-1. 데이터 묶어 계산하기
* 관측 단위별로 정리한 다양한 표를 결합하여 데이터셋을 만들고 분석을 진행한다
* 연관이 깊은 데이터끼리 모아서 표를 구성하므로 데이터를 묶어 필요한 데이터를 만드는 과정이 필요하다.
* 하나의 데이터셋을 여러부분으로 분할하여 관리할 때도 있다.

# 07-2. 데이터 연결하기
* 데이터를 결합하는 가장 쉬운 방법은 데이터를 연결하는 것이다.
1. 데이터 연결하기 예제
```python
import pandas as pd

df1 = pd.read_csv('concat_1.csv')
df2 = pd.read_csv('concat_2.csv')
df3 = pd.read_csv('concat_3.csv')
print(df1)
print(df2)
print(df3)
```
📝 실행결과
```
    A   B   C   D
0  a0  b0  c0  d0
1  a1  b1  c1  d1
2  a2  b2  c2  d2
3  a3  b3  c3  d3
    A   B   C   D
0  a4  b4  c4  d4
1  a5  b5  c5  d5
2  a6  b6  c6  d6
3  a7  b7  c7  d7
     A    B    C    D
0   a8   b8   c8   d8
1   a9   b9   c9   d9
2  a10  b10  c10  d10
3  a11  b11  c11  d11
```

## 데이터프레임 살펴보기
```python
#1. index로 데이터프레임 왼쪽에 있는 행 번호 참조하기
print(df1.index)
#2. columns로 열의 이름 알아보기
print(df1.columns)
#3. values로 값으로 구성된 넘파이 배열 반환하기
print(df1.values)
```
📝 실행결과
```
RangeIndex(start=0, stop=4, step=1)
Index(['A', 'B', 'C', 'D'], dtype='object')
[['a0' 'b0' 'c0' 'd0']
 ['a1' 'b1' 'c1' 'd1']
 ['a2' 'b2' 'c2' 'd2']
 ['a3' 'b3' 'c3' 'd3']]
```

## 행 연결하기
### 행 방향 연결하기
1. 연결할 모든 데이터프레임을 concat() 함수에 리스트로 전달
```python
row_concat = pd.concat([df1, df2, df3])
print(row_concat)
```
📝 실행결과
```
     A    B    C    D
0   a0   b0   c0   d0
1   a1   b1   c1   d1
2   a2   b2   c2   d2
3   a3   b3   c3   d3
0   a4   b4   c4   d4
1   a5   b5   c5   d5
2   a6   b6   c6   d6
3   a7   b7   c7   d7
0   a8   b8   c8   d8
1   a9   b9   c9   d9
2  a10  b10  c10  d10
3  a11  b11  c11  d11
```
2. 연결한 데이터프레임의 원하는 데이터 추출하기
```python
print(row_concat.iloc[3,:]) # 네 번째 행 추출하기
```
📝 실행결과
```
A    a3
B    b3
C    c3
D    d3
Name: 3, dtype: object
```

3. 시리즈를 생성하여 데이터 프레임에 연결해보기
```python
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(new_row_series)
```
📝 실행결과
```
0    n1
1    n2
2    n3
3    n4
dtype: object
```

4. new_row_series를 새로운 행으로 추가하려고 concat()을 사용하면 의도와 다른 데이터프레임이 생성됨
```python
print(pd.concat([df1, new_row_series]))
```
📝 실행결과
```
     A    B    C    D    0
0   a0   b0   c0   d0  NaN
1   a1   b1   c1   d1  NaN
2   a2   b2   c2   d2  NaN
3   a3   b3   c3   d3  NaN
0  NaN  NaN  NaN  NaN   n1
1  NaN  NaN  NaN  NaN   n2
2  NaN  NaN  NaN  NaN   n3
3  NaN  NaN  NaN  NaN   n4
```
* 새로운 열에 데이터가 추가되고 결측값으로 나타남
* 시리즈에 데이터프레임과 일치하는 열이 없으므로 시리즈가 새로운 열로 추가됨

5. 이 문제를 해결하려면 시리즈를 데이터프레임으로 바꿔야함
```python
new_row_df = pd.DataFrame(
    data = [['n1', 'n2', 'n3', 'n4']]
    columns = ['A', 'B', 'C', 'D']
)
print(new_row_df)
```
📝 실행결과
```
    A   B   C   D
0  n1  n2  n3  n4
```
6. 생성한 데이터프레임을 df1에 연결한다
```python
print(pd.concat([df1,new_row_df]))
```
📝 실행결과
```
    A   B   C   D
0  a0  b0  c0  d0
1  a1  b1  c1  d1
2  a2  b2  c2  d2
3  a3  b3  c3  d3
0  n1  n2  n3  n4
```

### 새로운 인덱스 설정하기
1. ignorw_index를 사용하면 인덱스 중복 값을 없앨 수 있다
```python
row_concat_i = pd.concat([df1, df2, df3], ignore_index = True)
print(row_concat_i)
```
📝 실행결과
```
      A    B    C    D
0    a0   b0   c0   d0
1    a1   b1   c1   d1
2    a2   b2   c2   d2
3    a3   b3   c3   d3
4    a4   b4   c4   d4
5    a5   b5   c5   d5
6    a6   b6   c6   d6
7    a7   b7   c7   d7
8    a8   b8   c8   d8
9    a9   b9   c9   d9
10  a10  b10  c10  d10
11  a11  b11  c11  d11
```

## 열 연결하기
### 열 방향 연결하기
* 매개변수 axis에 1 또는 columns를 지정해주면 됨
1. df1, df2, df3 를 열방향으로 연결
```python
col_concat = pd.concat([df1, df2, df3], axis = "columns")
print(col_concat)

print(col_concat["A"])
```
📝 실행결과
```
    A   B   C   D   A   B   C   D    A    B    C    D
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11

    A   A    A
0  a0  a4   a8
1  a1  a5   a9
2  a2  a6  a10
3  a3  a7  a1
```
* 단순히 행 인덱스가 그대로 덧붙여짐
* A 열을 추출하면 같은 이름의 모든 열을 추출함
