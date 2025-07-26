# 12-1. datetime 객체 활용하기
1. datetime 라이브러리 불러오기
```python
from datetime import datetime
```
2. datetime 객체의 now() 메서드를 사용하여 현재 날짜와 시간 정보를 확인할 수 있다.
```python
now = datetime.now()
print(now)
```
📝 실행결과
```
2025-07-26 01:47:26.798880
```

3. 원하는 날짜와 시간으로 datetime 객체를 생성할 수도 있다.
```python
t1 = datetime.now()
t2 = datetime(1970,1,1)
print(t1)
print(t2)
```
📝 실행결과
```
2025-07-25 23:48:49.464421
1970-01-01 00:00:00
```

4. datetime 객체는 수학 연산자로 시간 차이를 계산할 수 있는 기능을 제공
```python
diff = t1-t2
print(diff)
```
📝 실행결과
```
20294 days, 23:48:49.464421
```
5. datetime 객체를 사용하여 계산한 시간의 차이는 timedelta 객체로 표현된다
```python
print(type(diff))
```
📝 실행결과
```
<class 'datetime.timedelta'>
```

# 12-2. datetime으로 변환하기
1. 에볼라 데이터셋 불러오기
```
ebola.iloc[:5,:5]
         Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
0    1/5/2015  289        2776.0            NaN            10030.0
1    1/4/2015  288        2775.0            NaN             9780.0
2    1/3/2015  287        2769.0         8166.0             9722.0
3    1/2/2015  286           NaN         8157.0                NaN
4  12/31/2014  284        2730.0         8115.0             9633.0
```

2. info() 메서드로 이 날짜 정보가 어떤 자료형인지 확인
```python
print(ebola.info())
```
📝 실행결과
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 18 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   Date                 122 non-null    object  # 날짜 정보는 object형이다.
 1   Day                  122 non-null    int64  
 2   Cases_Guinea         93 non-null     float64
 3   Cases_Liberia        83 non-null     float64
 4   Cases_SierraLeone    87 non-null     float64
 5   Cases_Nigeria        38 non-null     float64
 6   Cases_Senegal        25 non-null     float64
 7   Cases_UnitedStates   18 non-null     float64
 8   Cases_Spain          16 non-null     float64
 9   Cases_Mali           12 non-null     float64
 10  Deaths_Guinea        92 non-null     float64
 11  Deaths_Liberia       81 non-null     float64
 12  Deaths_SierraLeone   87 non-null     float64
 13  Deaths_Nigeria       38 non-null     float64
 14  Deaths_Senegal       22 non-null     float64
 15  Deaths_UnitedStates  18 non-null     float64
 16  Deaths_Spain         16 non-null     float64
 17  Deaths_Mali          12 non-null     float64
dtypes: float64(16), int64(1), object(1)
memory usage: 17.3+ KB
None
```

3. to_datetime() 함수를 사용하려 Date 열의 값을 datetime형으로 변환하여 새로운 열 date_dt로 저장
```python
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
```

4. 매개변수 format으로 데이터를 datetime 객체로 변환하는 방법을 좀 더 명확하게 지정할 수 있다.
```python
ebola['date_dt'] = pd.to_datetime(ebola['Date'], format = '%m/%d/%Y')
```

5. info()를 사용하여 새로 생성한 date_dt 열의 자료형을 확인
```python
print(ebola.info())
```
📝 실행결과
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 19 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   Date                 122 non-null    object        
 1   Day                  122 non-null    int64         
 2   Cases_Guinea         93 non-null     float64       
 3   Cases_Liberia        83 non-null     float64       
 4   Cases_SierraLeone    87 non-null     float64       
 5   Cases_Nigeria        38 non-null     float64       
 6   Cases_Senegal        25 non-null     float64       
 7   Cases_UnitedStates   18 non-null     float64       
 8   Cases_Spain          16 non-null     float64       
 9   Cases_Mali           12 non-null     float64       
 10  Deaths_Guinea        92 non-null     float64       
 11  Deaths_Liberia       81 non-null     float64       
 12  Deaths_SierraLeone   87 non-null     float64       
 13  Deaths_Nigeria       38 non-null     float64       
 14  Deaths_Senegal       22 non-null     float64       
 15  Deaths_UnitedStates  18 non-null     float64       
 16  Deaths_Spain         16 non-null     float64       
 17  Deaths_Mali          12 non-null     float64       
 18  date_dt              122 non-null    datetime64[ns]  #datetime 형으로 바뀐 것을 확인
dtypes: datetime64[ns](1), float64(16), int64(1), object(1)
memory usage: 18.2+ KB
None
```
* 31-0-2014와 같이 일이 먼저 나오는 형식으로 하고 싶다면 매개변수 dayfirst를 True로 설정
* 2014-03-31과 같이 연도가 먼저 나오는 형식으로 하고 싶다면 매개변수 yearfirst를 True로 설정

# 12-3. 시계열 데이터 불러오기
* read_csv() 함수는 parse_dates, inher_datetime_format, keep_date_col, date_parser_dayfirst, cache_dates처럼 시계열 데이터를 처리하는 다양한 매개변수 제공
1. 데이터의 Date 열을 매개변수 Parse_dates에 전달하여 바로 datetime형으로 변환
```python
ebola = pd.read_csv('country_timeseries.csv', parse_dates = ['Date'])
print(ebola.info())
```
📝 실행결과
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 18 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   Date                 122 non-null    datetime64[ns] #datetime으로 바로 변환된 것을 확인
 1   Day                  122 non-null    int64         
 2   Cases_Guinea         93 non-null     float64       
 3   Cases_Liberia        83 non-null     float64       
 4   Cases_SierraLeone    87 non-null     float64       
 5   Cases_Nigeria        38 non-null     float64       
 6   Cases_Senegal        25 non-null     float64       
 7   Cases_UnitedStates   18 non-null     float64       
 8   Cases_Spain          16 non-null     float64       
 9   Cases_Mali           12 non-null     float64       
 10  Deaths_Guinea        92 non-null     float64       
 11  Deaths_Liberia       81 non-null     float64       
 12  Deaths_SierraLeone   87 non-null     float64       
 13  Deaths_Nigeria       38 non-null     float64       
 14  Deaths_Senegal       22 non-null     float64       
 15  Deaths_UnitedStates  18 non-null     float64       
 16  Deaths_Spain         16 non-null     float64       
 17  Deaths_Mali          12 non-null     float64       
dtypes: datetime64[ns](1), float64(16), int64(1)
memory usage: 17.3 KB
None
```

# 12-4. 시간 정보 추출하기
* datetime 객체에서 연,월,일과 같은 시간 정보 요소를 따로 추출할 수 있다.
* to_datetime()에 일시를 나타내는 문자열을 전달하면 Timestamp 객체를 반환한다.
1. '2021-12-14'를 to_datetime()에 전달하여 Timestamp 객체를 생성하고 연, 월, 일을 추출
```python
d = pd.to_datetime('2021-12-14')
print(d)
print(type(d))
```
📝 실행결과
```
2021-12-14 00:00:00
<class 'pandas._libs.tslibs.timestamps.Timestamp'> #timestamp 객체인 것을 확인
```

2. 연, 월, 일을 각각 year, month, day 속성으로 추출
```python
print(d.year)
print(d.month)
print(d.day)
```
📝 실행결과
```
2021
12
14
```

3. 에볼라 데이터셋의 Date 열을 datetime으로 변환하여 date_dt 열에 저장
```python
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola[['Date', 'date_dt']])
```
📝 실행결과
```
          Date    date_dt
0   2015-01-05 2015-01-05
1   2015-01-04 2015-01-04
2   2015-01-03 2015-01-03
3   2015-01-02 2015-01-02
4   2014-12-31 2014-12-31
..         ...        ...
117 2014-03-27 2014-03-27
118 2014-03-26 2014-03-26
119 2014-03-25 2014-03-25
120 2014-03-24 2014-03-24
121 2014-03-22 2014-03-22

[122 rows x 2 columns]

```

4. dt 속성을 사용하면 전체 열을 대상으로 datetime 객체의 메서드를 적용할 수 있다. year로 연도 추출하여 새로운 열에 저장
```python
ebola['year'] = ebola['date_dt'].dt.year
print(ebola[['Date', 'date_dt', 'year']])
```
📝 실행결과
```
          Date    date_dt  year
0   2015-01-05 2015-01-05  2015
1   2015-01-04 2015-01-04  2015
2   2015-01-03 2015-01-03  2015
3   2015-01-02 2015-01-02  2015
4   2014-12-31 2014-12-31  2014
..         ...        ...   ...
117 2014-03-27 2014-03-27  2014
118 2014-03-26 2014-03-26  2014
119 2014-03-25 2014-03-25  2014
120 2014-03-24 2014-03-24  2014
121 2014-03-22 2014-03-22  2014

[122 rows x 3 columns]
```

5. 마찬가지의 방법으로 월과 일도 추출하여 month, day 열에 저장
```python
ebola = ebola.assign(
    month = ebola["date_dt"].dt.month,
    day = ebola["date_dt"].dt.day
)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']])
```
6. info() 메서드로 새로 생성한 세 열의 자료형을 살펴본다.
```python
print(ebola.info())
```
📝 실행결과
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 22 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   Date                 122 non-null    datetime64[ns]
 1   Day                  122 non-null    int64         
 2   Cases_Guinea         93 non-null     float64       
 3   Cases_Liberia        83 non-null     float64       
 4   Cases_SierraLeone    87 non-null     float64       
 5   Cases_Nigeria        38 non-null     float64       
 6   Cases_Senegal        25 non-null     float64       
 7   Cases_UnitedStates   18 non-null     float64       
 8   Cases_Spain          16 non-null     float64       
 9   Cases_Mali           12 non-null     float64       
 10  Deaths_Guinea        92 non-null     float64       
 11  Deaths_Liberia       81 non-null     float64       
 12  Deaths_SierraLeone   87 non-null     float64       
 13  Deaths_Nigeria       38 non-null     float64       
 14  Deaths_Senegal       22 non-null     float64       
 15  Deaths_UnitedStates  18 non-null     float64       
 16  Deaths_Spain         16 non-null     float64       
 17  Deaths_Mali          12 non-null     float64       
 18  date_dt              122 non-null    datetime64[ns]
 19  year                 122 non-null    int32          # 추출한 요소는 datetime형이 아니라 int32형이다.
 20  month                122 non-null    int32         
 21  day                  122 non-null    int32         
dtypes: datetime64[ns](2), float64(16), int32(3), int64(1)
memory usage: 19.7 KB
None
```

# 12-5. 시간 간격 계산하기
1. 데이터셋의 왼쪽 아래에 있는 5개의 행, 열 데이터 살펴보기
```python
print(ebola.iloc[-5:,:5])
```
📝 실행결과
```
          Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
117 2014-03-27    5         103.0            8.0                6.0
118 2014-03-26    4          86.0            NaN                NaN
119 2014-03-25    3          86.0            NaN                NaN
120 2014-03-24    2          86.0            NaN                NaN
121 2014-03-22    0          49.0            NaN                NaN
```

2. date_dt 열에서 min() 메서드를 호출하여 가장 오래된 날짜를 구한다.
```python
print(ebola['date_dt'].min())
```
📝 실행결과
```
2014-03-22 00:00:00
```

3. date_dt 열에서 이 값을 빼면 며칠이 지난 데이터인지 계산하여 새로운 열에 계산한 값을 넣는다.
```python
ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
print(ebola[['Date', 'Day', 'outbreak_d']])
```
📝 실행결과
```
          Date  Day outbreak_d  # Day열과  outbreak_d 열이 같다.
0   2015-01-05  289   289 days   
1   2015-01-04  288   288 days
2   2015-01-03  287   287 days
3   2015-01-02  286   286 days
4   2014-12-31  284   284 days
..         ...  ...        ...
117 2014-03-27    5     5 days
118 2014-03-26    4     4 days
119 2014-03-25    3     3 days
120 2014-03-24    2     2 days
121 2014-03-22    0     0 days

[122 rows x 3 columns]
```

4. info()로 oubreak_d 열의 자료형을 확인한 결과 timedelta형이다.
```python
print(ebola.info())
```
📝 실행결과
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 23 columns):
 #   Column               Non-Null Count  Dtype          
---  ------               --------------  -----          
 0   Date                 122 non-null    datetime64[ns] 
 1   Day                  122 non-null    int64          
 2   Cases_Guinea         93 non-null     float64        
 3   Cases_Liberia        83 non-null     float64        
 4   Cases_SierraLeone    87 non-null     float64        
 5   Cases_Nigeria        38 non-null     float64        
 6   Cases_Senegal        25 non-null     float64        
 7   Cases_UnitedStates   18 non-null     float64        
 8   Cases_Spain          16 non-null     float64        
 9   Cases_Mali           12 non-null     float64        
 10  Deaths_Guinea        92 non-null     float64        
 11  Deaths_Liberia       81 non-null     float64        
 12  Deaths_SierraLeone   87 non-null     float64        
 13  Deaths_Nigeria       38 non-null     float64        
 14  Deaths_Senegal       22 non-null     float64        
 15  Deaths_UnitedStates  18 non-null     float64        
 16  Deaths_Spain         16 non-null     float64        
 17  Deaths_Mali          12 non-null     float64        
 18  date_dt              122 non-null    datetime64[ns] 
 19  year                 122 non-null    int32          
 20  month                122 non-null    int32          
 21  day                  122 non-null    int32          
 22  outbreak_d           122 non-null    timedelta64[ns]
dtypes: datetime64[ns](2), float64(16), int32(3), int64(1), timedelta64[ns](1)
memory usage: 20.6 KB
None
```

# 12-6. datetime 객체의 메서드 활용하기.
1. 파산한 은행 정보의 banklist 데이터셋을 사용
```python
banks = pd.read_csv('banklist.csv')
print(banks.head())
```
📝 실행결과
```
                                           Bank Name                City  ST  \
0                                Fayette County Bank          Saint Elmo  IL   
1  Guaranty Bank, (d/b/a BestBank in Georgia & Mi...           Milwaukee  WI   
2                                     First NBC Bank         New Orleans  LA   
3                                      Proficio Bank  Cottonwood Heights  UT   
4                      Seaway Bank and Trust Company             Chicago  IL   

    CERT                Acquiring Institution Closing Date Updated Date  
0   1802            United Fidelity Bank, fsb    26-May-17    26-Jul-17  
1  30003  First-Citizens Bank & Trust Company     5-May-17    26-Jul-17  
2  58302                         Whitney Bank    28-Apr-17    26-Jul-17  
3  35495                    Cache Valley Bank     3-Mar-17    18-May-17  
4  19328                  State Bank of Texas    27-Jan-17    18-May-17
```

2. read_csv()의 매개변수 parse_dates에 날짜 정보가 담긴 Closing Date, Updated Date 열을 전달하여 두 열을 datetime형으로 불러올 수 있다.
```python
banks = pd.read_csv(
         'banklist.csv', pasrse_dates=["Closing Date", "Updated Date"]
)
print(banks.info())
```
📝 실행결과
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 553 entries, 0 to 552
Data columns (total 7 columns):
 #   Column                 Non-Null Count  Dtype         
---  ------                 --------------  -----         
 0   Bank Name              553 non-null    object        
 1   City                   553 non-null    object        
 2   ST                     553 non-null    object        
 3   CERT                   553 non-null    int64         
 4   Acquiring Institution  553 non-null    object        
 5   Closing Date           553 non-null    datetime64[ns] #datetime 형이 된다
 6   Updated Date           553 non-null    datetime64[ns]
dtypes: datetime64[ns](2), int64(1), object(4)
memory usage: 30.4+ KB
None
```
3. 은행이 파산한 분기와 연도를 기반으로 데이터 분석
```python
banks = banks.assign(
         closing_quarter=banks['Closing Date'].dt.quarter,
         closing_year= banks['Closing Date'].dt.year
)
```

4. 파산한 연도를 나타내는 closing_year 열을 기준으로 그룹화하고 연도별 파산한 은행 개수를 size()로 계산한 시리즈를 closing_year 변수에 저장
```python
closing_year = banks.groupby(['clsoing_year']).size()
print(closing_year)
```
📝 실행결과
```
closing_year
2000      2
2001      4
2002     11
2003      3
2004      4
2007      3
2008     25
2009    140
2010    157
2011     92
2012     51
2013     24
2014     18
2015      8
2016      5
2017      6
dtype: int64
```

5. 매년 각 분기에 파산한 은행이 궁금하다면 closing_year와 closing_quarter를 기준으로 데이터셋을 그룹화하고 size()로 해당하는 은행 개수를 구할 수 있다.
```python
closing_year_q = (
         banks
         .groupby(['closing_year', 'closing_quarter'])
         .size()
)

print(closing_year_q)
```
📝 실행결과
```
closing_year  closing_quarter
2000          4                   2
2001          1                   1
              2                   1
              3                   2
2002          1                   6
              2                   2
              3                   1
              4                   2
2003          1                   1
              2                   1
              4                   1
2004          1                   3
              2                   1
2007          1                   1
              3                   1
              4                   1
2008          1                   2
              2                   2
              3                   9
              4                  12
2009          1                  21
              2                  24
              3                  50
              4                  45
2010          1                  41
              2                  45
              3                  41
              4                  30
2011          1                  26
              2                  22
              3                  26
              4                  18
2012          1                  16
              2                  15
              3                  12
              4                   8
2013          1                   4
              2                  12
              3                   6
              4                   2
2014          1                   5
              2                   7
              3                   2
              4                   4
2015          1                   4
              2                   1
              3                   1
              4                   2
2016          1                   1
              2                   2
              3                   2
2017          1                   3
              2                   3
dtype: int64
```

6. 연도별 분기별 파산한 은행 개수를 시각화
```python
import matplotlib.pyplot as plt

fig,ax = plt.subplots()
ax = closing_year.plot()
plt.show()
```
📝 실행결과
