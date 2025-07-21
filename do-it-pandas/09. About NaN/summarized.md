# 09-1. 결측값이란?
1. 넘파이의 결측값에서 유래되었다
2. 결측값은 0, ''과는 다른 개념이며. '같다'라는 개념도 없다
3. NaN, NAN, nan으로 표시할 수 있다
```python
from numpy import NaN, NAN, nan

print(NAN == True)
print(NaN == 0)
print(NaN == '')
print(NaN == NaN)
print(NaN == NAN)
print(NaN == nan)
print(nan == NAN)
```
📝 실행결과
```
False
False
False
False
False
False
False
```
* np.nan이 가장 보편적으로 사용

4. 판다스의 isnull() 메서드로 결측값을 확인할 수 있다.
```python
import pandas as pd
print(pd.isnull(np.nan))
```
📝 출력결과
```
True
```

5. 결측값이 아닌지 검사하는 notnull() 메서드도 있다.
```python
print(pd.notnull(np.nan))
print(pd.notnull(42))
print(pd.notnull('missing'))
```
📝 실행결과
```
False
True
True
```

# 09-2. 결측값은 왜 생길까?
* 판다스는 데이터를 불러올 때 자동으로 빠진 데이터를 NaN으로 대체하여 데이터프레임을 반환
* read_csv() 함수로 불러올 때 3가지 매개변수가 있다

|매개변수| 기능 |
|:---------:|:-------------------------------:|
|na_values| 데이터의 특정값을 결측값 또는 NaN값으로 처리할 수 있다. na_values = [99]와 같이 사용
|keep_default_na| 결측값으로 처리해야 하는 값(na_values로 지정한 값, 빈 문자열)의 종류에 기존 결측값을 포함할지 True, False로 설정. 기본값은 True로, False로 설정하면 na_values에 지정한 값만 결측값으로 처리
|na_filter| 결측값을 처리할지 결정하는 매개변수. 기본값은 True이며 결측값을 NaN으로 대체하겠다는 뜻. na_filter를 False로 설정하면 어떤 값도 결측값으로 처리하지 않는다.

1. read_csv()에 나머지 매개변수는 설정하지 않고 기본값을 사용하여 데이터를 불러옴
```python
visited_file = 'survey_visited.csv'
print(pd.read_csv(visited_file))
```
📝 실행결과
```
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3         NaN
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
```

2. keep_default_na를 False로 설정하여 기본적으로 결측값으로 보는 값을 처리하지 않도록 설정
```python
print(pd.read_csv(visited_file, keep_default_na = False))
```
📝 실행결과
```
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3            
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
```

3. na_values=[""]를 매개변수로 지정하여, 빈 문자열은 결측값으로 처리한다.
```python
print(
    pd.read_csv(visited.file, na_values=[""], keep_default_na = False)
)
```
📝 실행결과
```
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3         NaN
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
```

## 데이터를 연결할 때 생기는 결측값
#1. survey_visited와 survey_survey 데이터셋을 불러온다.
```
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3         NaN
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22
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
#2. 왼쪽 visited 데이터프레임의 ident 열과 survey 데이터프레임의 taken 열을 기준으로 결합
```python
vs = visited.merge(survey, left_on = 'ident', right_on = 'taken')
print(vs)
```
📝 실행결과
```
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
#NaN이 생겼다

## 직접 입력한 결측값
1. 결측값을 포함한 시리즈 만들기
```python
num_legs = pd.Series({'goat': 4, 'amoeba' : np.nan})
print(num_legs)
```
📝 실행결과
```
goat      4.0
amoeba    NaN
dtype: float64
```

2. 결측값을 포함한 데이터프레임 만들기
```python
scientists = pd.DataFrame(
  {
      "Name" : ["Rosaline Franklin", "William Gosset"],
      "Occupation" : ["Chemist", "Statistician"],
      "Born" : ["1920-07-25", "1876-06-13"],
      "Died" : ["1958-04-16", "1937-10-16"],
       missing" : [np.nan, np.nan],
  }
)

print(scientists)
```
📝 실행결과
```
                Name    Occupation        Born        Died  missing
0  Rosaline Franklin       Chemist  1920-07-25  1958-04-16      NaN
1     William Gosset  Statistician  1876-06-13  1937-10-16      NaN
```

3. missing열의 데이터형이 float64이다. 이는 넘파이의 NaN 결측값이 부동 소수점이기 때문이다.
```python
print(scientists.dtypes)
```
📝 실행결과
```
Name           object
Occupation     object
Born           object
Died           object
missing       float64
dtype: object
```

4. 모든 값이 nan인 열을 할당할 수도 있다.
```python
scientists = pd.DataFrame(
    {
        "Name" : ["Rosaline Franklin", "William Gosset"],
        "Occupation" : ["Chemist", "Statistician"],
        "Born" : ["1920-07-25", "1876-06-13"],
        "Died" : ["1958-04-16", "1937-10-16"],
    }
)

scientist["missing'] = np.nan
print(scientists)
```
📝 실행결과
```
                Name    Occupation        Born        Died  missing
0  Rosaline Franklin       Chemist  1920-07-25  1958-04-16      NaN
1     William Gosset  Statistician  1876-06-13  1937-10-16      NaN
```

## 인덱스를 다시 설정할 때 생기는 결측값
1. 갭마인더 데이터셋의 연도별 평균 기대 수명 구하기
```python
gapminder = pd.read_csv('gapminder.tsv', sep ='\t')

life_exp = gapminder.groupby('year')['lifeExp'].mean()
print(life_exp)
```
📝 실행결과
```
year
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
```
2. 2000년 이후의 데이터만 추출
```python
y2000 = life_exp[life_exp.index>2000]
print(y2000)
```
📝 실행결과
```
year
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
```
3. 2000~2010 데이터로 표현하기 위해 reindex() 메서드를 사용하여 다시 인덱싱
```python
print(y2000.reindex(range(2000,2010)))
```
📝 실행결과
```
year
2000          NaN
2001          NaN
2002    65.694923
2003          NaN
2004          NaN
2005          NaN
2006          NaN
2007    67.007423
2008          NaN
2009          NaN
Name: lifeExp, dtype: float64
```
* 2002년 2007년 이외에는 결측값으로 채워짐

# 09-3 결측값 구하기
## 결측값 처리하기
1. 결측값을 개수를 구하기 위해 결측값이 아닌 값 개수를 구하기
```python
ebola = pd.read_csv('country_timeseries.csv')
print(ebola.count()
```
📝 실행결과
```
Date                   122
Day                    122
Cases_Guinea            93
Cases_Liberia           83
Cases_SierraLeone       87
Cases_Nigeria           38
Cases_Senegal           25
Cases_UnitedStates      18
Cases_Spain             16
Cases_Mali              12
Deaths_Guinea           92
Deaths_Liberia          81
Deaths_SierraLeone      87
Deaths_Nigeria          38
Deaths_Senegal          22
Deaths_UnitedStates     18
Deaths_Spain            16
Deaths_Mali             12
dtype: int64
```
2. 전체 행 개수에서 count()값을 빼서 열별 결측값 개수를 구할 수 있다.
* shape의 첫 번째 값이 행 개수이므로 shape[0]에서 count()를 뺀다.
```python
num_rows = ebola.shape[0]
num_missing = num_rows - ebola.count()
print(num_missing)
```
📝 실행결과
```
Date                     0
Day                      0
Cases_Guinea            29
Cases_Liberia           39
Cases_SierraLeone       35
Cases_Nigeria           84
Cases_Senegal           97
Cases_UnitedStates     104
Cases_Spain            106
Cases_Mali             110
Deaths_Guinea           30
Deaths_Liberia          41
Deaths_SierraLeone      35
Deaths_Nigeria          84
Deaths_Senegal         100
Deaths_UnitedStates    104
Deaths_Spain           106
Deaths_Mali            110
dtype: int64
```
3. 모든 결측값 개수를 구하거나 특정 열의 결측값 개수 구하기.
* isnull() 메서드와 numpy의 count_nonzero() 함수를 조합.
* count_nonzero() 함수는 0(False)이 아닌 값을 센다.
```python
import numpy as np

print(np.count_nonzero(ebola.isnull()))
print(np.count_nonzero(ebola['Cases_Guinea'].isnull()
```
📝 실행결과
```
1214
29
```

4. 시리즈의 value_counts() 메서드를 이용해서 각 값의 빈도수를 구한다.
* 매개변수 dropa=False 로 설정하면 결측값 NaN의 개수도 확인할 수 있다.
```python
cnts = ebola.Cases_Guinea.value_counts(dropna=False)
print(cnts)
```
📝실행결과
```
Cases_Guinea
NaN      29
86.0      3
112.0     2
495.0     2
390.0     2
         ..
143.0     1
122.0     1
127.0     1
103.0     1
49.0      1
Name: count, Length: 89, dtype: int64
```
5. value_counts()가 반환하는 결과 시리즈는 각 값이 인덱스이다.
* 판다스의 isnull() 함수와 loc를 사용하여 NaN의 개수만 확인 할 수도 있다.
```python
print(cnts.loc[pd.isnull(cnts.index)]) #loc속성은 loc[True,False,False,False]이런 식으로도 이용이 가능하다.
```
📝 실행결과
```
Cases_Guinea
NaN    29
Name: count, dtype: int64
```

6. 파이썬의 True는 정수 1과 같고 False는 정수 0과 같다.
* 이 특징을 이용하여 isnull()의 결과 불리언 벡터와 sum() 메서드를 조합하여 결측값의 개수를 구할 수 있다.
```python
print(ebola.Cases_Guinea.isnull().sum())
```
📝 실행결과
```
29
```

### 결측값 대체하기
1. fillna() 메서드를 사용하여 결측값을 다른 값으로 대체할 수 있다. 결측값을 0으로 기록
```python
print(ebola.fillna(0).iloc[:,0:5])
```
📝 실행결과
```
           Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
0      1/5/2015  289        2776.0            0.0            10030.0
1      1/4/2015  288        2775.0            0.0             9780.0
2      1/3/2015  287        2769.0         8166.0             9722.0
3      1/2/2015  286           0.0         8157.0                0.0
4    12/31/2014  284        2730.0         8115.0             9633.0
..          ...  ...           ...            ...                ...
117   3/27/2014    5         103.0            8.0                6.0
118   3/26/2014    4          86.0            0.0                0.0
119   3/25/2014    3          86.0            0.0                0.0
120   3/24/2014    2          86.0            0.0                0.0
121   3/22/2014    0          49.0            0.0                0.0

[122 rows x 5 columns]
```
### 정방향 채우기
1. 데이터를 위에서 아래로 훑으면서 결측값 직전에 찾은 값으로 결측값을 대체하는 방식
* fillna() 메서드의 매개변수 method에 'ffill'을 전달하여 정방향 채우기를 적용
* 첫 행이 결측값이면 채울 값이 없으므로 해당 데이터는 결측값으로 유지
```python
           Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
0      1/5/2015  289        2776.0            NaN            10030.0
1      1/4/2015  288        2775.0            NaN             9780.0
2      1/3/2015  287        2769.0         8166.0             9722.0
3      1/2/2015  286        2769.0         8157.0             9722.0
4    12/31/2014  284        2730.0         8115.0             9633.0
..          ...  ...           ...            ...                ...
117   3/27/2014    5         103.0            8.0                6.0
118   3/26/2014    4          86.0            8.0                6.0
119   3/25/2014    3          86.0            8.0                6.0
120   3/24/2014    2          86.0            8.0                6.0
121   3/22/2014    0          49.0            8.0                6.0

[122 rows x 5 columns]
```

### 역방향 채우기
* 반대로 데이터를 아래에서 위로 훑으며 결측값 직전에 찾은 값으로 결측값을 대체하는 방식
* 매개변수 method에 'bfill'을 전달
```python
print(ebola.fillna(method='bfill').iloc[:,0:5]
```
📝 실행결과
```
           Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
0      1/5/2015  289        2776.0         8166.0            10030.0
1      1/4/2015  288        2775.0         8166.0             9780.0
2      1/3/2015  287        2769.0         8166.0             9722.0
3      1/2/2015  286        2730.0         8157.0             9633.0
4    12/31/2014  284        2730.0         8115.0             9633.0
..          ...  ...           ...            ...                ...
117   3/27/2014    5         103.0            8.0                6.0
118   3/26/2014    4          86.0            NaN                NaN
119   3/25/2014    3          86.0            NaN                NaN
120   3/24/2014    2          86.0            NaN                NaN
121   3/22/2014    0          49.0            NaN                NaN
```

### 보간법으로 채우기
* 기존 값을 사용하여 기본적으로 결측값의 양쪽값의 중간값으로 채운다.
```python
print(ebola.interpolate().iloc[:,0:5])
```
📝 실행결과
```
           Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
0      1/5/2015  289        2776.0            NaN            10030.0
1      1/4/2015  288        2775.0            NaN             9780.0
2      1/3/2015  287        2769.0         8166.0             9722.0
3      1/2/2015  286        2749.5         8157.0             9677.5
4    12/31/2014  284        2730.0         8115.0             9633.0
..          ...  ...           ...            ...                ...
117   3/27/2014    5         103.0            8.0                6.0
118   3/26/2014    4          86.0            8.0                6.0
119   3/25/2014    3          86.0            8.0                6.0
120   3/24/2014    2          86.0            8.0                6.0
121   3/22/2014    0          49.0            8.0                6.0

[122 rows x 5 columns]
```

### 결측값 삭제하기

* 필요없다면 결측값은 삭제해도 됨. 하지만 무작정 삭제하면 데이터가 편향될 수 있음
* dropna() 메서드를 사용하여 결측값을 삭제할 수 있다.
* 매개변수 how의 행 또는 열 데이터 중 하나라도 결측값일 때 삭제하려면 any로, 모든 값이 결측값일 때만 삭제하려면 all을 지정

1. 실습에 사용할 ebola의 데이터 크기를 확인
```python
print(ebola.shape)
```
📝 실행결과
```
(122, 18)
```

2. dropna() 메서드를 사용하여 결측값이 하나도 없는 행만 남기도록 처리.
```python
ebola_dropna = ebola.dropna()
print(ebola_dropna.shape)
```
📝 실행결과
```
(1,18)
```

3. 데이터가 딱 한 행 남았다
```python
print(ebola_dropna)
```
📝 실행결과
```
          Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone  \
19  11/18/2014  241        2047.0         7082.0             6190.0   

    Cases_Nigeria  Cases_Senegal  Cases_UnitedStates  Cases_Spain  Cases_Mali  \
19           20.0            1.0                 4.0          1.0         6.0   

    Deaths_Guinea  Deaths_Liberia  Deaths_SierraLeone  Deaths_Nigeria  \
19         1214.0          2963.0              1267.0             8.0   

    Deaths_Senegal  Deaths_UnitedStates  Deaths_Spain  Deaths_Mali  
19             0.0                  1.0           0.0          6.0
```

## 결측값이 있는 데이터 계산하기
* 데이터에 결측값이 있을 때 계산하면 나오는 결과 알아보기
1. 세 지역의 확진자수를 합한 새로운 열 Cases_multiple 생성
```python
ebola["Cases_multiple"] = (
    ebola["Cases_Guinea"]
    + ebola["Cases_Liberia"]
    + ebola["Cases_SierraLeone"]
)
```
2. 세 지역과 새로 계산한 열의 처음 10개 행을 보며 계산 결과 비교
```python
ebola_subset = ebola.loc[
    :,
    [
        "Cases_Guinea",
        "Cases_Liberia",
        "Cases_SierraLeone",
        "Cases_multiple",
    ],
]

print(ebola_subset.head(n=10))
```
📝 실행결과
```
   Cases_Guinea  Cases_Liberia  Cases_SierraLeone  Cases_multiple
0        2776.0            NaN            10030.0             NaN
1        2775.0            NaN             9780.0             NaN
2        2769.0         8166.0             9722.0         20657.0
3           NaN         8157.0                NaN             NaN
4        2730.0         8115.0             9633.0         20478.0
5        2706.0         8018.0             9446.0         20170.0
6        2695.0            NaN             9409.0             NaN
7        2630.0         7977.0             9203.0         19810.0
8        2597.0            NaN             9004.0             NaN
9        2571.0         7862.0             8939.0         19372.0
```
* 세 지역의 열 중 하나라도 결측값이 있으면 NaN으로 기록.
2. mean()과 sum()의 메서드로 결측값을 무시하도록 설정할 수 있다.
* 매개변수 skipna로 결측값을 건너뛰고 값을 계산하게 할 수 있다.
```python
print(ebola.Cases_Guinea.sum(skipna = True)
print(ebola.Cases_Guinea.sum(skipna = True)
```
📝 실행결과
```
84729.0
nan
```

09-4 판다스 내장 NA 결측값 살펴보기
* 내장 NA값인 pd.NA가 추가되었다.
1. scientist 데이터프레임을 만들고 dtypes로 데이터형 살펴보기
```
scientists
                Name    Occupation        Born        Died  Age
0  Rodaline Franklin       Chemist  1920-07-25  1958-04-16   37
1     William Gosset  Statistician  1876-06-13  1937-10-16   61

Name          object
Occupation    object
Born          object
Died          object
Age            int64
dtype: object
```

2. 데이터형이 int64인 Age와 object인 Name 열의 1번 행을 pd.NA로 변경
```python
scientits.loc[1,"Name"] = pd.NA
scientists.loc[1,"Age"] = pd.NA
print(scientists)
```
📝 실행결과
```
                Name    Occupation        Born        Died   Age
0  Rodaline Franklin       Chemist  1920-07-25  1958-04-16  37.0
1               <NA>  Statistician  1876-06-13  1937-10-16   NaN
```

3. Age의 데이터형이 float64로 변경되었다.
```python
print(scientists.dtypes)
```
📝 실행결과
```
Name           object
Occupation     object
Born           object
Died           object
Age           float64
dtype: object
```
4. 넘파이의 np.NaN으로 설정해도 똑같이 float64형으로 바뀐다.
```python
scientists = pd.DataFrame(
    {
        "Name" : ["Rodaline Franklin", "William Gosset"],
        "Occupation" : ["Chemist", "Statistician"],
        "Born" : ["1920-07-25", "1876-06-13"],
        "Died" : ["1958-04-16", "1937-10-16"],
        "Age" : [37, 61]
    }
)

scientists.loc[1, "Name"] = np.nan
scientists.loc[1, "Age"] = np.nan

print(scientists.dtype)
```
📝 실행결과
```
Name           object
Occupation     object
Born           object
Died           object
Age           float64
dtype: object
```

