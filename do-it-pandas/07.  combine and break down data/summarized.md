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

2. 데이터프레임에 열을 추가하려면 새 열 이름을 대괄호 사이에 넣어 리스트를 할당해주면 된다
```python
col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
print(col_concat)
```
📝 실행결과
```
    A   B   C   D   A   B   C   D    A    B    C    D new_col_list
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8           n1
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9           n2
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10           n3
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11           n4
```

3. 비슷한 방법으로 시리즈를 추가할 수도 있다.
```python
col_concat['new_col_series'] = pd.Series(['n1', 'n2', 'n3', 'n4])
print(col_concat)
```
📝 실행결과
```
    A   B   C   D   A   B   C   D    A    B    C    D new_col_list  \
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8           n1   
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9           n2   
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10           n3   
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11           n4   

  new_col_series  
0             n1  
1             n2  
2             n3  
3             n4
```

4. 매개변수 ignore_index에 인수로 True를 대입하면 열 이름이 중복되지 않게 다시 설정할 수 있다
```python
print(pd.concat([df1, df2, df3], axis = 'columns', ignore_index = True)
```
📝 실행결과
```
   0   1   2   3   4   5   6   7    8    9    10   11
0  a0  b0  c0  d0  a4  b4  c4  d4   a8   b8   c8   d8
1  a1  b1  c1  d1  a5  b5  c5  d5   a9   b9   c9   d9
2  a2  b2  c2  d2  a6  b6  c6  d6  a10  b10  c10  d10
3  a3  b3  c3  d3  a7  b7  c7  d7  a11  b11  c11  d11
```

## 인덱스나 열 이름이 다른 데이터 연결하기
### 열 이름이 다른 데이터 행 방향 연결하기
1. 연결하려는 데이터의 열 이름이 서로 다르도록 df1, df2, df3의 열 이름을 바꾸기
```python
df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']
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

    E   F   G   H
0  a4  b4  c4  d4
1  a5  b5  c5  d5
2  a6  b6  c6  d6
3  a7  b7  c7  d7

     A    C    F    H
0   a8   b8   c8   d8
1   a9   b9   c9   d9
2  a10  b10  c10  d10
3  a11  b11  c11  d11
```

2. concat() 함수를 사용하여 데이처를 연결하면 열을 자동으로 정렬하고 결측값은 NaN으로 채운다
```python
row_concat = pd.concat([df1, df2, df3])
print(row_concat)
```
📝 실행결과
```
     A    B    C    D    E    F    G    H
0   a0   b0   c0   d0  NaN  NaN  NaN  NaN
1   a1   b1   c1   d1  NaN  NaN  NaN  NaN
2   a2   b2   c2   d2  NaN  NaN  NaN  NaN
3   a3   b3   c3   d3  NaN  NaN  NaN  NaN
0  NaN  NaN  NaN  NaN   a4   b4   c4   d4
1  NaN  NaN  NaN  NaN   a5   b5   c5   d5
2  NaN  NaN  NaN  NaN   a6   b6   c6   d6
3  NaN  NaN  NaN  NaN   a7   b7   c7   d7
0   a8  NaN   b8  NaN  NaN   c8  NaN   d8
1   a9  NaN   b9  NaN  NaN   c9  NaN   d9
2  a10  NaN  b10  NaN  NaN  c10  NaN  d10
3  a11  NaN  b11  NaN  NaN  c11  NaN  d11
```

3. 연결할 객체 사이에 공통인 열만 유지시켜 결측값 없애기
* 매개변수 join에 inner를 인수로 설정하면 공통인 열만 유지됨
```python
print(pd.concat([df1, df2, df3], join = 'inner'))
```
📝 실행결과
```
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
```
* 이번 예제에서 공통인 열은 없으므로 'inner'설정하면 빈데이터프레임만 남음

4. df1과 df3은 A와 C열이 공통이므로 두 데이터프레임을 join = 'inner'로 연결하면 공통된 열만 나타남
```python
print(pd.concat([df1, df3], ignore_index = False, join = 'inner'))
```
📝 실행결과
```
     A    C
0   a0   c0
1   a1   c1
2   a2   c2
3   a3   c3
0   a8   b8
1   a9   b9
2  a10  b10
3  a11  b11
```

### 인덱스가 다른 데이터 열 방향 연결하기
1. 데이터프레임 3개가 서오 다른 인덱스가 되도록 수정
```python
df1.index = [0,1,2,3]
df2.index = [4,5,6,7]
df3.index = [0,2,5,7]
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

    E   F   G   H
4  a4  b4  c4  d4
5  a5  b5  c5  d5
6  a6  b6  c6  d6
7  a7  b7  c7  d7

     A    C    F    H
0   a8   b8   c8   d8
2   a9   b9   c9   d9
5  a10  b10  c10  d10
7  a11  b11  c11  d11
```

2. axis = 'columns'로 연결하여 데이터프레임을 열 방향으로 연결, 인덱스가 같은 행끼리 연결
```python
col_concat = pd.concat([df1, df2, df3], axis = 'columns')
print(col_concat)
```
📝 실행결과
```
     A    B    C    D    E    F    G    H    A    C    F    H
0   a0   b0   c0   d0  NaN  NaN  NaN  NaN   a8   b8   c8   d8
1   a1   b1   c1   d1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
2   a2   b2   c2   d2  NaN  NaN  NaN  NaN   a9   b9   c9   d9
3   a3   b3   c3   d3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
4  NaN  NaN  NaN  NaN   a4   b4   c4   d4  NaN  NaN  NaN  NaN
5  NaN  NaN  NaN  NaN   a5   b5   c5   d5  a10  b10  c10  d10
6  NaN  NaN  NaN  NaN   a6   b6   c6   d6  NaN  NaN  NaN  NaN
7  NaN  NaN  NaN  NaN   a7   b7   c7   d7  a11  b11  c11  d11
```

3. 마찬가지로 join = 'inner'를 지정하면 인덱스가 공통인 데이터만 연결한다.
```python
print(pd.concat([df1, df3], axis = 'columns', join = 'inner'))
```
📝 실행결과
```
    A   B   C   D   A   C   F   H
0  a0  b0  c0  d0  a8  b8  c8  d8
2  a2  b2  c2  d2  a9  b9  c9  d9
```

# 07-3. 분할된 데이터 연결하기
### 여러 개의 파일로 분할된 데이터 연결하기
1. 파이썬 내장 pathlib 모듈을 사용하여 특정 파일 이름 규칙의 모든 파일을 불러오기
```python
import panda as pd
from pathlib import Path

billboard_data_files = (
    Path(".")
    .glob("billboard-*.csv") # billboard-로 시작하는 모든 csv 파일을 불러온다
)

billboard_data_files = sorted(list(billboard_data_files))
print(billboard_data_files)
```

2. billboard_data_files는 제너레이터이다. 한 번 사용하면 내용이 사라진다. 그러므로 전체 파일 목록을 확인하고 싶다면 리스트로 변환
```python
billboard_data_files = list(billboard_data_files)
```

3. 파일 이름 리스트를 구했으므로 각 파일을 데이터프레임으로 불러오기
```python
billboard01 = pd.read_csv(billboard_data_files[0])
billboard02 = pd.read_csv(billboard_data_files[1])
billboard03 = pd.read_csv(billboard_data_files[2])
```
4. shape 속성으로 데이터 확인하기
```python
print(billboard01.shape)
print(billboard02.shape)
print(billboard03.shape)
```
📝 실행결과
```
(317, 7)
(317, 7)
(317, 7)
```
5. concat() 함수로 데이터를 연결 후 shape로 데이터 확인하기
```python
billboard = pd.concat([billboard01, billboard02, billboard03])
print(billboard.shape)
```
📝 실행결과
```
(951, 7)
```
* 317 * 3 = 951 이므로 같다. 다만, 분할한 데이터가 많을수록 번거롭기 때문에 루프 구문이나 리스트 컴프리헨션을 사용하는 것이 좋다.

### 루프 구문으로 여러 개의 파일 불러오기
1. 빈 리스트를 만들고 루프를 사용하여 각 CSV 파일을 순회하면서 판다스 데이터프레임으로 불러온 후 데이터프레임을 리스트에 추가.
```python
from pathlib import Path

billboard_data_files = (
    Path(".")
    .glob("billboard-*.csv")
)

#빈 리스트를 생성
list_billboard_df = []

#csv 파일명 리스트를 순회한다.
for csv_name in billboard_data_files:
    df = pd.read_csv(csv_filename)
    list_billboard_df.append(df)

print(len(list_billboard_df))
```
📝 실행결과
```
76
```

2. list_billboard_df의 첫 번째 요소의 유형은 DataFrame이다
3. concat() 함수로 데이터프레임 리스트 연결하고 shape 속성으로 데이터 확인하기
```python
billboard_loop_concat = pd.concat(list_billboard_df)
print(billboard_loop_concat.shape)
```
📝 실행결과
```
(24092, 7)
```

### 리스트 컴프리헨션으로 여러 개 파일 불러오기
1. CSV 파일을 데이터프레임으로 저장하는 것은 리스트 컴프리헨션으로도 가능하다.
```python
billboard_data_files = (
   Path(".")
   .glob("billboard-*.csv")
)

billboard_dfs = [pd.read_csv(data) for data in billboard_data_files]
```

2. concat()을 호출하면 데이터를 연결할 수 있다.
```python
billboard_concat_comp = pd.concat(billboard_dfs)
print(billboard_concat_comp)
```
📝 실행결과
```
     year            artist                    track  time date.entered  week  \
0    2000             2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26  wk60   
1    2000           2Ge+her  The Hardest Part Of ...  3:15   2000-09-02  wk60   
2    2000      3 Doors Down               Kryptonite  3:53   2000-04-08  wk60   
3    2000      3 Doors Down                    Loser  4:24   2000-10-21  wk60   
4    2000          504 Boyz            Wobble Wobble  3:35   2000-04-15  wk60   
..    ...               ...                      ...   ...          ...   ...   
312  2000       Yankee Grey     Another Nine Minutes  3:10   2000-04-29  wk47   
313  2000  Yearwood, Trisha          Real Live Woman  3:55   2000-04-01  wk47   
314  2000   Ying Yang Twins  Whistle While You Tw...  4:19   2000-03-18  wk47   
315  2000     Zombie Nation            Kernkraft 400  3:30   2000-09-02  wk47   
316  2000   matchbox twenty                     Bent  4:12   2000-04-29  wk47   

     rating  
0       NaN  
1       NaN  
2       NaN  
3       NaN  
4       NaN  
..      ...  
312     NaN  
313     NaN  
314     NaN  
315     NaN  
316     NaN  

[24092 rows x 7 columns]
```

# 07-4. 여러 데이터셋 병합하기
* 2개 이상의 데이터프레임에서 공통된 데이터를 기준으로 연결하고 싶을 때, merge또는 join한다
* join은 인덱스 기준으로 데이터프레임 객체를 병합하지만 merge() 메서드는 훨씬 더 명시적이고 유연한 병합이 가능하다.
1. 관측 데이터셋
```python
print(person)
print(site)
print(visited)
print(survey)
```
📝 실행결과
```
      ident   personal    family
0      dyer    William      Dyer
1        pb      Frank   Pabodie
2      lake   Anderson      Lake
3       roe  Valentina   Roerich
4  danforth      Frank  Danforth

    name    lat    long
0   DR-1 -49.85 -128.57
1   DR-3 -47.15 -126.72
2  MSK-4 -48.87 -123.40

    taken person quant  reading
0     619   dyer   rad     9.82
1     619   dyer   sal     0.13
2     622   dyer   rad     7.80
3     622   dyer   sal     0.09
4     734     pb   rad     8.41
5     734   lake   sal     0.05
6     734     pb  temp   -21.50
7     735     pb   rad     7.22
8     735    NaN   sal     0.06
9     735    NaN  temp   -26.00
10    751     pb   rad     4.35
11    751     pb  temp   -18.50
12    751   lake   sal     0.10
13    752   lake   rad     2.19
14    752   lake   sal     0.09
15    752   lake  temp   -16.00
16    752    roe   sal    41.60
17    837   lake   rad     1.46
18    837   lake   sal     0.21
19    837    roe   sal    22.50
20    844    roe   rad    11.25
```
* 데이터셋은 각 부분이 관측 단위인 여러개로 분할되었다.
* 만약 해당 위치의 위도,경도 정보와 함께 날짜를 확인하고 싶으면 여러 데이터프레임을 결합해야한다.

2. 판다스의 merge()메서드로 이 작업을 수행할 수 있다.
* left.merge(right)와 같이 호출한 데이터프레임은 왼쪽에 있는 데이터프레임이 되고, 첫번째 매개변수는 오른쪽에 있는 데이터프레임을 나타낸다

3. **매개변수 how**는 최종결합된 결과의 형태를 결정한다
* left : 왼쪽 테이블의 모든 키를 유지한다
* right : 오른쪽 테이블의 모든 키를 유지한다
* outer : 왼쪽과 오른쪽 테이블의 모든 키를 유지한다
* inner : 왼쪽과 오른쪽 테이블의 공통 키를 유지한다.

4. 매개변수 on은 병합 기준이 되는 열을 지정
* 왼쪽과 오른쪽 데이터프레임의 열 이름이 서로 다르다면 on 대신 매개변수 left_on과 right_on을 사용한다.

### 일대일 병합하기
1. 데이터프레임의 site 열에 중복값이 없도록 일부 데이터만 뗴어 실습
```python
visited_subset = visited.loc[[0,2,6], :]
print(visited_subset)
```
📝 실행결과
```
   ident   site       dated
0    619   DR-1  1927-02-08
2    734   DR-3  1939-01-07
6    837  MSK-4  1932-01-14
```
2. merge()메서드의 매개변수 how의 기본 값은 'inner'이므로 내부 조인을 실행, 데이터프레임 site를 왼쪽으로 인수로 전달한 visited_subset을 오른쪽으로 전달
```python
o2o_merge = site.merge(visited_subset, left_on = "name", right_on = "site")
print(o2o_merge)
```
📝 실행결과
```
    name    lat    long  ident   site       dated
0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
1   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
2  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14
```

### 다대일 병합하기
* visited 데이터프레임 일부가 아닌 전체를 대상으로 병합
* 왼쪽 데이터프레임에 중복된 site 값이 있으므로 다대일 병합이 발생
* 다대일 병합에서는 한쪽 데이터프레임의 키를 여러번 사용
1. visited의 site 열에 있는 중복값 개수 살펴보기
``` python
print(visited["site"].value_counts())
```
📝 실행결과
```
site
DR-3     4
DR-1     3
MSK-4    1
Name: count, dtype: int64
```

2. site 열에 중복값이 있는 visited 데이터프레임과 병합할 때 값을 여러번 반복한다.
```python
m2o_merge = site.merge(visited, left_on = 'name', right_on = 'site')
print(m2o_merge)
```
📝 실행결과
```
    name    lat    long  ident   site       dated
0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
1   DR-1 -49.85 -128.57    622   DR-1  1927-02-10
2   DR-1 -49.85 -128.57    844   DR-1  1932-03-22
3   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
4   DR-3 -47.15 -126.72    735   DR-3  1930-01-12
5   DR-3 -47.15 -126.72    751   DR-3  1930-02-26
6   DR-3 -47.15 -126.72    752   DR-3         NaN
7  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14
```

### 다대다 병합하기
1. persocn의 ident열과 survey의 person 열의 값을 기준으로 두 데이터프레임을 병합하고, visited의 ident 열과 survey의 taken 열의 값을 기준으로 두 데이터프레임을 병합
```python
ps = person.merge(survey, left_on = 'ident', right_on = 'person')
vs = visited.merge(survey, left_on='ident', right_on = 'taken')
print(ps)
print(vs)
```
📝 실행결과
```
  ident   personal   family  taken person quant  reading
0   dyer    William     Dyer    619   dyer   rad     9.82
1   dyer    William     Dyer    619   dyer   sal     0.13
2   dyer    William     Dyer    622   dyer   rad     7.80
3   dyer    William     Dyer    622   dyer   sal     0.09
4     pb      Frank  Pabodie    734     pb   rad     8.41
5     pb      Frank  Pabodie    734     pb  temp   -21.50
6     pb      Frank  Pabodie    735     pb   rad     7.22
7     pb      Frank  Pabodie    751     pb   rad     4.35
8     pb      Frank  Pabodie    751     pb  temp   -18.50
9   lake   Anderson     Lake    734   lake   sal     0.05
10  lake   Anderson     Lake    751   lake   sal     0.10
11  lake   Anderson     Lake    752   lake   rad     2.19
12  lake   Anderson     Lake    752   lake   sal     0.09
13  lake   Anderson     Lake    752   lake  temp   -16.00
14  lake   Anderson     Lake    837   lake   rad     1.46
15  lake   Anderson     Lake    837   lake   sal     0.21
16   roe  Valentina  Roerich    752    roe   sal    41.60
17   roe  Valentina  Roerich    837    roe   sal    22.50
18   roe  Valentina  Roerich    844    roe   rad    11.25

    ident   site       dated  taken person quant  reading
0     619   DR-1  1927-02-08    619   dyer   rad     9.82
1     619   DR-1  1927-02-08    619   dyer   sal     0.13
2     622   DR-1  1927-02-10    622   dyer   rad     7.80
3     622   DR-1  1927-02-10    622   dyer   sal     0.09
4     734   DR-3  1939-01-07    734     pb   rad     8.41
5     734   DR-3  1939-01-07    734   lake   sal     0.05
6     734   DR-3  1939-01-07    734     pb  temp   -21.50
7     735   DR-3  1930-01-12    735     pb   rad     7.22
8     735   DR-3  1930-01-12    735    NaN   sal     0.06
9     735   DR-3  1930-01-12    735    NaN  temp   -26.00
10    751   DR-3  1930-02-26    751     pb   rad     4.35
11    751   DR-3  1930-02-26    751     pb  temp   -18.50
12    751   DR-3  1930-02-26    751   lake   sal     0.10
13    752   DR-3         NaN    752   lake   rad     2.19
14    752   DR-3         NaN    752   lake   sal     0.09
15    752   DR-3         NaN    752   lake  temp   -16.00
16    752   DR-3         NaN    752    roe   sal    41.60
17    837  MSK-4  1932-01-14    837   lake   rad     1.46
18    837  MSK-4  1932-01-14    837   lake   sal     0.21
19    837  MSK-4  1932-01-14    837    roe   sal    22.50
20    844   DR-1  1932-03-22    844    roe   rad    11.25
```

2. ps를 왼쪽 데이터프레임, vs를 오른쪽 데이터프레임으로 하여 quant 열을 기준으로 병합한다면 양쪽 데이터프레임 모두 quant 열에 중복값이 있으므로 다대다 병합이 일어난다.
* 각 데이터프레임의 quant 열에 중복값이 얼마나 있는지 알아보기
```python
print(ps["quant"].value_counts())
print(vs["quant"].value_counts())
```
📝 실행결과
```
2. ps를 왼쪽 데이터프레임, vs를 오른쪽 데이터프레임으로 하여 quant 열을 기준으로 병합한다면?, 양쪽 데이터프레임 모두 quant 열에 중복값이 있으므로 다대다 병합이 일어난다.
* 각 데이터프레임의 quant 열에 중복값이 얼마나 있는지 살펴보기
```python
print(ps["quant"].value_counts())
print(vs["quant"].value_counts())
```
📝실행결과
```
quant
rad     8
sal     8
temp    3
Name: count, dtype: int64
quant
sal     9
rad     8
temp    4
Name: count, dtype: int64
```

3. 다대다 병합을 수행
```python
ps_vs = ps.merge(
    vs,
    left_on = ["quant"],
    right_on = ["quant"],
)

print(ps_vs.loc[0,:])
```
📝 실행결과
```
ident_x            dyer
personal        William
family             Dyer
taken_x             619
person_x           dyer
quant               rad
reading_x          9.82
ident_y             619
site               DR-1
dated        1927-02-08
taken_y             619
person_y           dyer
reading_y          9.82
Name: 0, dtype: object
```
* 판다스는 병합된 데이터에 중복된 열 이름이 생기면 자동으로 접미사를 추가한다. _x, _y와 같이 추가됨
* 일반적으로 실무에서는 다대다 병합은 하지 않으려고 한다. 모든 키의 곱집합만큼 병합이 일어나기 때문

### assert 문으로 병합 결과 확인하기
* 병합 전후의 결과를 확인하는 방법은 데이터 행 개수를 확인하는 것이다
* 다대다 결합: 병합한 데이터프레임의 모든 행 개수 < 결과 데이터프레임의 행 개수이면 보통은 바람직하지 않은 상황이다
1. ps와 vs와 ps_vs의 shape 살펴보기
```python
print(ps.shape)
print(vs.shape)
print(ps_vs.shape)
```
📝 실행결과
```
(19, 7)
(21, 7)
(148, 13)
```

2. assert 문의 조건으로 의도대로 잘 실행되었는지 않았을 때 오류를 발생시킴
```python
assert ps_vs.shape[0] <= vs.shape[0] #False이면 AssertionError가 발생
```

# 07-5. 데이터 정규화하기
* 정규화 : 중복과 불필요한 데이터를 없애 정보를 재구성하는 과정
1. billboard 데이터셋으로 예제 수행
```
       year            artist                    track  time date.entered  \
0      2000             2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26   
1      2000           2Ge+her  The Hardest Part Of ...  3:15   2000-09-02   
2      2000      3 Doors Down               Kryptonite  3:53   2000-04-08   
3      2000      3 Doors Down                    Loser  4:24   2000-10-21   
4      2000          504 Boyz            Wobble Wobble  3:35   2000-04-15   
...     ...               ...                      ...   ...          ...   
24087  2000       Yankee Grey     Another Nine Minutes  3:10   2000-04-29   
24088  2000  Yearwood, Trisha          Real Live Woman  3:55   2000-04-01   
24089  2000   Ying Yang Twins  Whistle While You Tw...  4:19   2000-03-18   
24090  2000     Zombie Nation            Kernkraft 400  3:30   2000-09-02   
24091  2000   matchbox twenty                     Bent  4:12   2000-04-29   

       week  rating  
0       wk1    87.0  
1       wk1    91.0  
2       wk1    81.0  
3       wk1    76.0  
4       wk1    57.0  
...     ...     ...  
24087  wk76     NaN  
24088  wk76     NaN  
24089  wk76     NaN  
24090  wk76     NaN  
24091  wk76     NaN  

[24092 rows x 7 columns]
```
2. 'Loser'라는 특정 곡 데이터만 추출해 살펴보기
```python
print(billboard_long.loc[billboard_long.track == "Loser"])
```
📝 실행결과
```
       year        artist  track  time date.entered  week  rating
3      2000  3 Doors Down  Loser  4:24   2000-10-21   wk1    76.0
320    2000  3 Doors Down  Loser  4:24   2000-10-21   wk2    76.0
637    2000  3 Doors Down  Loser  4:24   2000-10-21   wk3    72.0
954    2000  3 Doors Down  Loser  4:24   2000-10-21   wk4    69.0
1271   2000  3 Doors Down  Loser  4:24   2000-10-21   wk5    67.0
...     ...           ...    ...   ...          ...   ...     ...
22510  2000  3 Doors Down  Loser  4:24   2000-10-21  wk72     NaN
22827  2000  3 Doors Down  Loser  4:24   2000-10-21  wk73     NaN
23144  2000  3 Doors Down  Loser  4:24   2000-10-21  wk74     NaN
23461  2000  3 Doors Down  Loser  4:24   2000-10-21  wk75     NaN
23778  2000  3 Doors Down  Loser  4:24   2000-10-21  wk76     NaN

[76 rows x 7 columns]
```
* 곡 정보만 별도의 데이터 표로 분리하기
* 연도, 가수, 곡, 재생시간, 발표일이 중복되지 않을 수 있다
* 새로운 데이터프레임으로 year열, artist열, track열, time열 date.entered 열로 옮기고 각 곡에 고유한 ID를 할당

3. 새로운 데이터프레임으로 옮길 4개의 열 데이터를 추출, shape로 데이터의 크기 살펴보기
```python
billboard_songs = billboard_long[
    ["year", "artist", "track", "time", "date.entered"]
]
print(billboard_songs.shape)
```
📝 실행결과
```
(24092, 5)
```
4. drop_duplicates() 메서드로 중복된 값을 제거하기
```python
billboard_songs = billboard_songs.drop_duplicates()
print(billboard_songs.shape)
```
📝 실행결과
```
(317, 5)
```
5. 각 데이터 행에 고유한 값을 할당한다.
```python
billboard_songs['id'] = billboard_songs.index +1
print(billboard_songs)
```
📝 실행결과
```
     year            artist                    track  time date.entered   id
0    2000             2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26    1
1    2000           2Ge+her  The Hardest Part Of ...  3:15   2000-09-02    2
2    2000      3 Doors Down               Kryptonite  3:53   2000-04-08    3
3    2000      3 Doors Down                    Loser  4:24   2000-10-21    4
4    2000          504 Boyz            Wobble Wobble  3:35   2000-04-15    5
..    ...               ...                      ...   ...          ...  ...
312  2000       Yankee Grey     Another Nine Minutes  3:10   2000-04-29  313
313  2000  Yearwood, Trisha          Real Live Woman  3:55   2000-04-01  314
314  2000   Ying Yang Twins  Whistle While You Tw...  4:19   2000-03-18  315
315  2000     Zombie Nation            Kernkraft 400  3:30   2000-09-02  316
316  2000   matchbox twenty                     Bent  4:12   2000-04-29  317

[317 rows x 6 columns
```

6. 데이터플레임의 id열을 사용하여 곡을 주별 순위 정보에 표시한다. merge()를 사용하여 곡 정보와 관련된 4개 열을 기준으로 두 데이터프레임을 병합하면 된다.
```python
billboard_ratings = billboard_long.merge(
    billboard_songs, on = ["year", "artist", "track", "time", date.entered"]
)
print(billboard_ratings)
```
📝 실행결과
```
       year            artist                    track  time date.entered  \
0      2000             2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26   
1      2000           2Ge+her  The Hardest Part Of ...  3:15   2000-09-02   
2      2000      3 Doors Down               Kryptonite  3:53   2000-04-08   
3      2000      3 Doors Down                    Loser  4:24   2000-10-21   
4      2000          504 Boyz            Wobble Wobble  3:35   2000-04-15   
...     ...               ...                      ...   ...          ...   
24087  2000       Yankee Grey     Another Nine Minutes  3:10   2000-04-29   
24088  2000  Yearwood, Trisha          Real Live Woman  3:55   2000-04-01   
24089  2000   Ying Yang Twins  Whistle While You Tw...  4:19   2000-03-18   
24090  2000     Zombie Nation            Kernkraft 400  3:30   2000-09-02   
24091  2000   matchbox twenty                     Bent  4:12   2000-04-29   

       week  rating   id  
0       wk1    87.0    1  
1       wk1    91.0    2  
2       wk1    81.0    3  
3       wk1    76.0    4  
4       wk1    57.0    5  
...     ...     ...  ...  
24087  wk76     NaN  313  
24088  wk76     NaN  314  
24089  wk76     NaN  315  
24090  wk76     NaN  316  
24091  wk76     NaN  317  

[24092 rows x 8 columns]
```

7. 곡 정보와 관련된 열을 제외한 나머지 열만 추출하여 주별 순위 데이터프레임을 완성
```python
billboard_ratings = billboard_ratings[
  ["id", "week", "rating']
]
print(billboard_ratings)
```
📝 실행결과
```
        id  week  rating
0        1   wk1    87.0
1        2   wk1    91.0
2        3   wk1    81.0
3        4   wk1    76.0
4        5   wk1    57.0
...    ...   ...     ...
24087  313  wk76     NaN
24088  314  wk76     NaN
24089  315  wk76     NaN
24090  316  wk76     NaN
24091  317  wk76     NaN

[24092 rows x 3 columns]
```
