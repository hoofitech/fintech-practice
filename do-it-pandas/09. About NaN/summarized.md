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
* 
