# 05-1. 깔끔한 데이터란?
1. 깔끔한 데이터는 데이터셋을 구조화하는 프레임워크로써 깔끔한 데이턴는 데이터셋을 분석하고 시각화하기 쉽다.
2. 깔끔한 데이터의 조건
   * 변수는 열로 나타내야 한다
   * 관측값은 행으로 나타내야 한다.
   * 값은 셀로 나타내야 한다.

# 05-2. 열 이름이 값일 때
## 하나의 열만 남기기
### 넓은 데이터 확인하기
```python
넓은 데이터인 pew 불러오기
import pandas as pd
pew = pd.read_csv('pew.csv')
print(pew.iloc[:,0:5])
```
📝실행결과
```
                   religion  <$10k  $10-20k  $20-30k  $30-40k
0                  Agnostic     27       34       60       81
1                   Atheist     12       27       37       52
2                  Buddhist     27       21       30       34
3                  Catholic    418      617      732      670
4        Don’t know/refused     15       14       15       11
5          Evangelical Prot    575      869     1064      982
6                     Hindu      1        9        7        9
7   Historically Black Prot    228      244      236      238
8         Jehovah's Witness     20       27       24       24
9                    Jewish     19       19       25       25
10            Mainline Prot    289      495      619      655
11                   Mormon     29       40       48       51
12                   Muslim      6        7        9       10
13                 Orthodox     13       17       23       32
14          Other Christian      9        7       11       13
15             Other Faiths     20       33       40       46
16    Other World Religions      5        2        3        4
17             Unaffiliated    217      299      374      365
```
1. 위 데이터 셋을 살펴보면 religion을 제외한 모든 열은 소득 범위를 나타내고 해당하는 사람 수를 값으로 설정함
2. 이와같이 하나의 변수를 여러 개의 열로 표현한 데이터를 '넓은 데이터(wide data)'라고 부름
3. 하나의 변수를 한 열로 표현한 긴 데이터 형식의 깔끔한 데이터로 바꾸려면 데이터프레임을 변환하는 피벗 되돌리기(unpivot)가 필요함

|melt()메서드의 매개변수|설명|
|:---------:|:---------------------------------------------------------------:|
| id_vars   |그대로 유지할 변수를 나타내는 컨테이너(리스트, 튜플, ndarray)다.|
| value_vars|피벗 되돌리기 할 열을 나타냄. 기본적으로 id_vars에 지정하지 않은 모든 열이 피벗 되돌리기 대상으로 지정된|
|var_name|value_vars의 열을 피벗 되돌리기 하여 구성할 새 열의 이름으로 설정할 문자열. 기본값은 'variable'|
|value_name| var_name 열의 값을 나타내는 새로운 열 이름 문자열 입니다. 기본 값은 'value'|

### 긴 데이터로 만들기
1. 매개변수 id_vars에 'religion'을 지정해서 이외의 모든 열을 피벗 되돌리기를 실행한다
```python
religion 열을 제외한 모든 열을 피벗 되돌리기
pew_long = pew.melt(id_vars='religion') 
print(pew_long)
```
📝실행결과
```
                  religion            variable  value
0                 Agnostic               <$10k     27
1                  Atheist               <$10k     12
2                 Buddhist               <$10k     27
3                 Catholic               <$10k    418
4       Don’t know/refused               <$10k     15
..                     ...                 ...    ...
175               Orthodox  Don't know/refused     73
176        Other Christian  Don't know/refused     18
177           Other Faiths  Don't know/refused     71
178  Other World Religions  Don't know/refused      8
179           Unaffiliated  Don't know/refused    597

[180 rows x 3 columns]
```
2.피벗 되돌리기 한 열의 이름을 매개변수 id_vars와 var_name 설정한다.
```python
피벗 되돌리기 한 열의 이름 설정
pew_long = pew.melt(id_vars="religion", var_name = "income", value_name = "count")
print(pew_long)
```
📝실행결과
```
                  religion              income  count
0                 Agnostic               <$10k     27
1                  Atheist               <$10k     12
2                 Buddhist               <$10k     27
3                 Catholic               <$10k    418
4       Don’t know/refused               <$10k     15
..                     ...                 ...    ...
175               Orthodox  Don't know/refused     73
176        Other Christian  Don't know/refused     18
177           Other Faiths  Don't know/refused     71
178  Other World Religions  Don't know/refused      8
179           Unaffiliated  Don't know/refused    597

[180 rows x 3 columns]
```

## 여러 개의 열 남기기
```python
billboard.csv 데이터셋을 불러옴\오기
billboard = pd.read_csv('billboars_csv')
print(billboars.iloc[0:5,0:16])
```
📝실행결과
```
   year        artist                    track  time date.entered  wk1   wk2  \ 
0  2000         2 Pac  Baby Don't Cry (Keep...  4:22   2000-02-26   87  82.0   
1  2000       2Ge+her  The Hardest Part Of ...  3:15   2000-09-02   91  87.0   
2  2000  3 Doors Down               Kryptonite  3:53   2000-04-08   81  70.0   
3  2000  3 Doors Down                    Loser  4:24   2000-10-21   76  76.0   
4  2000      504 Boyz            Wobble Wobble  3:35   2000-04-15   57  34.0   

    wk3   wk4   wk5   wk6   wk7   wk8   wk9  wk10  wk11  
0  72.0  77.0  87.0  94.0  99.0   NaN   NaN   NaN   NaN  
1  92.0   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  
2  68.0  67.0  66.0  57.0  54.0  53.0  51.0  51.0  51.0  
3  72.0  69.0  67.0  65.0  55.0  59.0  62.0  61.0  61.0  
4  25.0  17.0  17.0  31.0  36.0  49.0  53.0  57.0  64.0
```
1. 위 데이터의 wk는 한 주를 뜻함
2. 넓은 데이터에 문제가 있는 것이 아니다. 직관적으로 이해하기 쉽다는 장점도 있지만 필요에 따라 긴 데이터로 바꾸는 것이다.

```python
billboard_long = bilboard.melt(
    id_vars=["year", "artist", "track", "time", "date.entered"
    var_name="week"
    value_name= "rating"
)
print(billboard_long)
```
📝실행결과
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

# 05-3 열 이름에 변수가 여러 개일 때
## 열 이름이 여러 가지 뜻 일때
### 깔끔한 데이터 만들기 ①
```python
country_timeseries.csv 불러오기
ebola = pd.read_csv('country_timeseries.csv')

print(ebola.iloc[:5,[0,1,2,10]]
```
📝실행결과
```
         Date  Day  Cases_Guinea  Deaths_Guinea
0    1/5/2015  289        2776.0         1786.0
1    1/4/2015  288        2775.0         1781.0
2    1/3/2015  287        2769.0         1767.0
3    1/2/2015  286           NaN            NaN
4  12/31/2014  284        2730.0         1739.0
```
* 위 데이터는 Cases_Guinea와 Deaths_Guniea는 국가 이름과 각각 확진 사례, 사망자수로 두 가지 변수를 포함한다.

```python
Date와 Day 열을 제외한 열을 피벗 되돌리기를 수행
ebola_long = ebola.melt(id_vars=['Date', 'Day'])
print(ebola_long)
```
📝실행결과
```
            Date  Day      variable   value
0       1/5/2015  289  Cases_Guinea  2776.0
1       1/4/2015  288  Cases_Guinea  2775.0
2       1/3/2015  287  Cases_Guinea  2769.0
3       1/2/2015  286  Cases_Guinea     NaN
4     12/31/2014  284  Cases_Guinea  2730.0
...          ...  ...           ...     ...
1947   3/27/2014    5   Deaths_Mali     NaN
1948   3/26/2014    4   Deaths_Mali     NaN
1949   3/25/2014    3   Deaths_Mali     NaN
1950   3/24/2014    2   Deaths_Mali     NaN
1951   3/22/2014    0   Deaths_Mali     NaN

[1952 rows x 4 columns]
```
* 밑줄을 기준으로 앞은 사례를 나타내는 열로, 뒤는 국가를 나타내는 열로 표현하려면 split('_')으로 나눠주면 됨
* 문자열 객체의 메서드에 접근하려면 str속성을 사용해야 한다
* str은 접근자라고 불리는 특수한 유형의 속성임

## 열 이름을 분할하고 새로운 열로 할당하기
### 깔끔한 데이터 만들기 ②
```python
_을 기준으로 열이름을 분할하기
variable_split = ebola_long.variable.str.split('_')
print(variable_split[:5])
```
📝실행결과
```
0    [Cases, Guinea]
1    [Cases, Guinea]
2    [Cases, Guinea]
3    [Cases, Guinea]
4    [Cases, Guinea]
Name: variable, dtype: object
```
* variable_split의 타입은 시리즈이다
* split 메서드는 분할한 문자열을 리스트로 반환한다

```python
str 속성의 get()메서드로 분할한 문자열 리스트의 각 값에 접근하여 새로운 열로 할당시키기
status_values = variable_split.str.get(0)
country_values = variable.str.get(1)

ebola_long['status'] = status_values
ebola_long['country'] = country_values
```
📝 실행결과

```
            Date  Day      variable   value  status country
0       1/5/2015  289  Cases_Guinea  2776.0   Cases  Guinea
1       1/4/2015  288  Cases_Guinea  2775.0   Cases  Guinea
2       1/3/2015  287  Cases_Guinea  2769.0   Cases  Guinea
3       1/2/2015  286  Cases_Guinea     NaN   Cases  Guinea
4     12/31/2014  284  Cases_Guinea  2730.0   Cases  Guinea
...          ...  ...           ...     ...     ...     ...
1947   3/27/2014    5   Deaths_Mali     NaN  Deaths    Mali
1948   3/26/2014    4   Deaths_Mali     NaN  Deaths    Mali
1949   3/25/2014    3   Deaths_Mali     NaN  Deaths    Mali
1950   3/24/2014    2   Deaths_Mali     NaN  Deaths    Mali
1951   3/22/2014    0   Deaths_Mali     NaN  Deaths    Mali

[1952 rows x 6 columns]
```

## 한 번에 분할하고 합치기
### 깔끔한 데이터 한 번에 만들기
1. split()의 매개변수 expand로 리스트 시리즈 대신 분할 결과를 새로운 열로 만든 데이터 프레임을 반환
```python
ebola_long = ebola.melt(id_vars = ["Date", "day"])
variable_split = ebola_long.variable.str.split('_', expand=True)
print(variable_split)
```
📝 실행결과
```
           0       1
0      Cases  Guinea
1      Cases  Guinea
2      Cases  Guinea
3      Cases  Guinea
4      Cases  Guinea
...      ...     ...
1947  Deaths    Mali
1948  Deaths    Mali
1949  Deaths    Mali
1950  Deaths    Mali
1951  Deaths    Mali

[1952 rows x 2 columns]
```
2. 파이썬과 판다스 다중 할당 기능을 사용하여 새로 분할한 열을 원본 데이터프레임에 바로 할당할 수도 있다.
```python
ebola_long[['status', 'country']] = variable_split
print(ebola_long)
```
📝 실행결과
```
            Date  Day      variable   value  status country
0       1/5/2015  289  Cases_Guinea  2776.0   Cases  Guinea
1       1/4/2015  288  Cases_Guinea  2775.0   Cases  Guinea
2       1/3/2015  287  Cases_Guinea  2769.0   Cases  Guinea
3       1/2/2015  286  Cases_Guinea     NaN   Cases  Guinea
4     12/31/2014  284  Cases_Guinea  2730.0   Cases  Guinea
...          ...  ...           ...     ...     ...     ...
1947   3/27/2014    5   Deaths_Mali     NaN  Deaths    Mali
1948   3/26/2014    4   Deaths_Mali     NaN  Deaths    Mali
1949   3/25/2014    3   Deaths_Mali     NaN  Deaths    Mali
1950   3/24/2014    2   Deaths_Mali     NaN  Deaths    Mali
1951   3/22/2014    0   Deaths_Mali     NaN  Deaths    Mali

[1952 rows x 6 columns]
```

# 05-4. 변수가 행과 열 모두에 있을 때
### 행과 열 모두에 있는 변수 정리하기
1. weather.csv 데이터셋 불러오기
```python
weather = pd.read_csv('weather.csv')
print(weather.iloc[:5,:11]
```

📝 실행결과
```
        id  year  month element  d1    d2    d3  d4    d5  d6  d7
0  MX17004  2010      1    tmax NaN   NaN   NaN NaN   NaN NaN NaN
1  MX17004  2010      1    tmin NaN   NaN   NaN NaN   NaN NaN NaN
2  MX17004  2010      2    tmax NaN  27.3  24.1 NaN   NaN NaN NaN
3  MX17004  2010      2    tmin NaN  14.4  14.4 NaN   NaN NaN NaN
4  MX17004  2010      3    tmax NaN   NaN   NaN NaN  32.1 NaN NaN
```
* 월별 날짜의 최저 기온(tmin)과 최고 기온(tmax)을 포함한다.
* element열은 값이 2개이므로 넓게 피벗을 적용할 수 있으며, 날짜변수는 값으로 피벗 되돌리기 해야함

2. 데이터셋의 날짜 정리하기
```python
weather_melt = weather.melt(
    id_vars = "["id", "year", "month", "element"]
    var_name = "day"
    value_name = "temp"
)
print(weather_melt)
```
📝 실행결과
```
          id  year  month element  day  temp
0    MX17004  2010      1    tmax   d1   NaN
1    MX17004  2010      1    tmin   d1   NaN
2    MX17004  2010      2    tmax   d1   NaN
3    MX17004  2010      2    tmin   d1   NaN
4    MX17004  2010      3    tmax   d1   NaN
..       ...   ...    ...     ...  ...   ...
677  MX17004  2010     10    tmin  d31   NaN
678  MX17004  2010     11    tmax  d31   NaN
679  MX17004  2010     11    tmin  d31   NaN
680  MX17004  2010     12    tmax  d31   NaN
681  MX17004  2010     12    tmin  d31   NaN

[682 rows x 6 columns]
```
3. pivot_table 메서드를 사용하여 element 열에 저장된 변수를 피벗
```python
weather_tidy = weather_melt.pivot_table(
    index=['id', 'year', 'month', 'day']
    columns = 'element',
    values = 'temp'
)
print(weather_tidy)
```
📝 실행결과
```
element                 tmax  tmin
id      year month day            
MX17004 2010 1     d30  27.8  14.5
             2     d11  29.7  13.4
                   d2   27.3  14.4
                   d23  29.9  10.7
                   d3   24.1  14.4
             3     d10  34.5  16.8
                   d16  31.1  17.6
                   d5   32.1  14.2
             4     d27  36.3  16.7
             5     d27  33.2  18.2
             6     d17  28.0  17.5
                   d29  30.1  18.0
             7     d3   28.6  17.5
                   d14  29.9  16.5
             8     d23  26.4  15.0
                   d5   29.6  15.8
                   d29  28.0  15.3
                   d13  29.8  16.5
                   d25  29.7  15.6
                   d31  25.4  15.4
                   d8   29.0  17.3
             10    d5   27.0  14.0
                   d14  29.5  13.0
                   d15  28.7  10.5
                   d28  31.2  15.0
                   d7   28.1  12.9
             11    d2   31.3  16.3
                   d5   26.3   7.9
                   d27  27.7  14.2
                   d26  28.1  12.1
                   d4   27.2  12.0
             12    d1   29.9  13.8
                   d6   27.8  10.5
```
4. reset_index() 메서드를 사용하여 계층 열을 평면화
```python
weather_tidy_flat = weather_tidy.reset_index()
print(weather_tigy_flat)
```
📝 실행결과
```
element       id  year  month  day  tmax  tmin
0        MX17004  2010      1  d30  27.8  14.5
1        MX17004  2010      2  d11  29.7  13.4
2        MX17004  2010      2   d2  27.3  14.4
3        MX17004  2010      2  d23  29.9  10.7
4        MX17004  2010      2   d3  24.1  14.4
5        MX17004  2010      3  d10  34.5  16.8
6        MX17004  2010      3  d16  31.1  17.6
7        MX17004  2010      3   d5  32.1  14.2
8        MX17004  2010      4  d27  36.3  16.7
9        MX17004  2010      5  d27  33.2  18.2
10       MX17004  2010      6  d17  28.0  17.5
11       MX17004  2010      6  d29  30.1  18.0
12       MX17004  2010      7   d3  28.6  17.5
13       MX17004  2010      7  d14  29.9  16.5
14       MX17004  2010      8  d23  26.4  15.0
15       MX17004  2010      8   d5  29.6  15.8
16       MX17004  2010      8  d29  28.0  15.3
17       MX17004  2010      8  d13  29.8  16.5
18       MX17004  2010      8  d25  29.7  15.6
19       MX17004  2010      8  d31  25.4  15.4
20       MX17004  2010      8   d8  29.0  17.3
21       MX17004  2010     10   d5  27.0  14.0
22       MX17004  2010     10  d14  29.5  13.0
23       MX17004  2010     10  d15  28.7  10.5
24       MX17004  2010     10  d28  31.2  15.0
25       MX17004  2010     10   d7  28.1  12.9
26       MX17004  2010     11   d2  31.3  16.3
27       MX17004  2010     11   d5  26.3   7.9
28       MX17004  2010     11  d27  27.7  14.2
29       MX17004  2010     11  d26  28.1  12.1
30       MX17004  2010     11   d4  27.2  12.0
31       MX17004  2010     12   d1  29.9  13.8
32       MX17004  2010     12   d6  27.8  10.5
```

⭐요약
* melt()메서드를 사용하여 넓은 데이터 -> 긴 데이터로 바꿀 수 있다.
* melt()메서드의 매개변수는 id_vars, var_name, value_name가 있고, 모두 깔끔한 데이터를 만드는데 핵심적인 매개변수이다.
* str.split(기준문자열)을 통해서 셀 내용을 나눌 수 있다.
