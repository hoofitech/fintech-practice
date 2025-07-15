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

2. concat(을 호출하면 데이터를 연결할 수 있다.
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

