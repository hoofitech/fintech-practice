# 10-1. 자료형 살펴보기
1. tips 데이터 셋의 자료형 살펴보기
```
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
dtype: object
```
* int64 : 소수점이 없는 숫자
* float64 : 소수점이 있는 숫자
* category : 범주형 변수

# 10-2. 자료형 변환하기
### 문자열로 변환하기
* 변수가 숫자여도 문자열로 처리하는 것이 유리할 때가 있음
* 예를 들어, 데이터의 고유번호인 ID열을 평균을 계산하는 등 산술 연산을 적용하는 것이 무의미하다.
1. astype() 메서드에 'str'을 전달하여 자료형을 변환한 결과 열을 새로운 열 sex_str로 저장
```python
tips['sex_str'] = tips['sex'].astype('str')
print(tips.dtypes)
```
📝 실행결과
```
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
```

### 숫자로 변환하기
1. float64형으로 변환할 때는 'float'를 astype() 메서드에 전달
```python
tips['total_bill'] = tips['total_bill'].astype('float')
print(tips.dtypes)
```
📝 실행결과
```
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
```

# 숫자형으로 변환하는 to_numeric() 함수 사용하기
* 변수를 int나 float같은 숫자형으로 변환할 때는 판다스의 to_numeric() 함수를 사용
* 데이터프레임의 각 열은 dtype이 모두 같아야함
* 숫자인 열에 문자열이 일부 있다면 전체 열의 자료형은 숫자형이 아닌 문자열이 된다.
* 숫자열에 NaN이 아닌 'missing' 또는 'null'로 결측값이 표현되어있다면 자료형은 object가 됨
1. tips 데이터셋의 첫 10개 행을 추출하고 total_bill 열의 몇 개 값을 'missing'으로 바꾼다.
```python
tips_sub_miss = tips.head(10).copy() # 새로운 데이터프레임으로 복사
tips_sub_miss.loc[[1,3,5,7], 'total_bill'] = 'missing'

print(tips_sub_miss)
```
📝 실행결과
```
  total_bill   tip     sex smoker  day    time  size sex_str
0      16.99  1.01  Female     No  Sun  Dinner     2  Female
1    missing  1.66    Male     No  Sun  Dinner     3    Male
2      21.01  3.50    Male     No  Sun  Dinner     3    Male
3    missing  3.31    Male     No  Sun  Dinner     2    Male
4      24.59  3.61  Female     No  Sun  Dinner     4  Female
5    missing  4.71    Male     No  Sun  Dinner     4    Male
6       8.77  2.00    Male     No  Sun  Dinner     2    Male
7    missing  3.12    Male     No  Sun  Dinner     4    Male
8      15.04  1.96    Male     No  Sun  Dinner     2    Male
9      14.78  3.23    Male     No  Sun  Dinner     2    Male
```

2. dypes를 출력하면 total_bill 열이 float64형에서 object형으로 변경됨
```python
print(tips_sub_miss.dtypes)
```
📝 실행결과
```
total_bill      object
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
```
3. to_numeric() 메서드를 사용하여 total_bill 열을 다시 float64형으로 변환하려고 하면 오류가 발생
* 판다스는 'missing'이라는 문자열을 부동 소수점으로 변환하는 법을 모르기 때문
```python
pd.to_numeric(tips_sub_miss['total_bill'])
```
📝 실행결과
```
ValueError: Unable to parse string "missing" at position
```
4. to_numeric() 함수에는 숫자로 변환할 수 없는 값이 있을 때 쓰는 매개변수 'errors'가 있다.
* raise: 숫자로 변환할 수 없는 값을 발견하면 오류가 발생, 기본값이다.
* coerce: 변환할 수 없는 값이 있을 때 NaN으로 값을 설정
* ignore: 변환할 수 없는 값이 있을 때 해당 값을 그대로 사용

5. 'ignore'을 매개변수 'errors'에 전달
```python
tips_sub_missing['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill],
                                               errors = 'ignore')
print(tips_sub_miss)
```
📝 실행결과
```
  total_bill   tip     sex smoker  day    time  size sex_str
0      16.99  1.01  Female     No  Sun  Dinner     2  Female
1    missing  1.66    Male     No  Sun  Dinner     3    Male
2      21.01  3.50    Male     No  Sun  Dinner     3    Male
3    missing  3.31    Male     No  Sun  Dinner     2    Male
4      24.59  3.61  Female     No  Sun  Dinner     4  Female
5    missing  4.71    Male     No  Sun  Dinner     4    Male
6       8.77  2.00    Male     No  Sun  Dinner     2    Male
7    missing  3.12    Male     No  Sun  Dinner     4    Male
8      15.04  1.96    Male     No  Sun  Dinner     2    Male
9      14.78  3.23    Male     No  Sun  Dinner     2    Male
```
* 다만, 문자열과 숫자 모두가 있으므로 자료형은 여전히 문자열이다
```
total_bill      object
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
```

4. 'coerce'를 인수로 전달. 'missing' 문자열이 모두 NaN으로 대체되고 total_bill 자료형이 float64형으로 바뀜
```python
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'],
                                            errors = 'coerce')
print(tips_sub_miss)
```
📝 실행결과
```
   total_bill   tip     sex smoker  day    time  size sex_str
0       16.99  1.01  Female     No  Sun  Dinner     2  Female
1         NaN  1.66    Male     No  Sun  Dinner     3    Male
2       21.01  3.50    Male     No  Sun  Dinner     3    Male
3         NaN  3.31    Male     No  Sun  Dinner     2    Male
4       24.59  3.61  Female     No  Sun  Dinner     4  Female
5         NaN  4.71    Male     No  Sun  Dinner     4    Male
6        8.77  2.00    Male     No  Sun  Dinner     2    Male
7         NaN  3.12    Male     No  Sun  Dinner     4    Male
8       15.04  1.96    Male     No  Sun  Dinner     2    Male
9       14.78  3.23    Male     No  Sun  Dinner     2    Male
```
* 문자를 결측값으로 처리했으므로 float64형이 된다
```
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
sex_str         object
dtype: object
```

# 10-3. 범주형 데이터 알아보기
* 같은 문자열이 반복되러 데이터를 구성할 때는 category형을 사용하면 메모리를 효율적으로 관리하고 데이터를 빠르게 처리할 수 있다.
* 열의 값에 순서가 있다면 category형이 적합
* 통계 모델을 사용하는 등 범주형 데이터를 활용할 때 category 형이 적합하다.
### 범주형으로 변환하기
1. 범주형으로 변환하려면 'category'를 astype() 메서드에 인수로 전달하면 된다.
* tips 데이터셋의 sex열을 문자열로 변환했다가 다시 범주형으로 변환한다. 메모리 사용량도 확인
```python
tips['sex'] = tips['sex'].astype('str')
print(tips.info)
```
📝 실행결과
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype   
---  ------      --------------  -----   
 0   total_bill  244 non-null    float64 
 1   tip         244 non-null    float64 
 2   sex         244 non-null    object  
 3   smoker      244 non-null    category
 4   day         244 non-null    category
 5   time        244 non-null    category
 6   size        244 non-null    int64   
 7   sex_str     244 non-null    object  
dtypes: category(3), float64(2), int64(1), object(2)
memory usage: 10.8+ KB
None
```
* 메모리사용량이 10.8+ KB가 사용된다.

2. astype()에 'category'를 전달하여 sex열의 자료형을 범주형으로 변환
```python
tips['sex'] = tips['sex'].astype('category')
print(tips.info) 
```
📝 실행결과
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype   
---  ------      --------------  -----   
 0   total_bill  244 non-null    float64 
 1   tip         244 non-null    float64 
 2   sex         244 non-null    category
 3   smoker      244 non-null    category
 4   day         244 non-null    category
 5   time        244 non-null    category
 6   size        244 non-null    int64   
 7   sex_str     244 non-null    object  
dtypes: category(4), float64(2), int64(1), object(1)
memory usage: 9.3+ KB
None
```
* 메모리 사용량이 9.3+ KB가 사용되며 메모리 효율성이 좋은 것을 확인했다.

## 범주형 데이터 다루기

| 번호 | 메서드 (API)                                | 설명                      |
| -- | ---------------------------------------- | ----------------------- |
| 1  | `.cat.ordered`                           | 범주의 정렬 여부           |
| 2  | `.cat.categories`                        | 범주형 시리즈의 모든 카테고리 목록 반환  |
| 3  | `.cat.codes`                             | 각 값이 속한 카테고리의 정수 코드 반환  |
| 4  | `.cat.rename_categories(new_categories)` | 카테고리 이름 변경              |
| 5  | `.cat.reorder_categories(new_order)`     | 카테고리 순서 재지정             |
| 6  | `.cat.add_categories(new_categories)`    | 새 카테고리 추가               |
| 7  | `.cat.remove_categories(removals)`       | 지정한 카테고리 제거             |
| 8  | `.cat.remove_unused_categories()`        | 사용되지 않는 카테고리 제거         |
| 9  | `.cat.set_categories(new_categories)`    | 카테고리 목록을 새로운 것으로 완전히 설정 |
| 10 | `.cat.as_ordered()`                      | 범주형을 순서형으로 변환           |
| 11 | `.cat.as_unordered()`                    | 순서형 범주를 비순서형으로 변환       |

⭐ 핵심 포인트
* astype()에 매개변수를 전달하여 데이터의 자료형을 바꿀 수 있다.
* to_numeric()함수로 숫자형으로 바꿀 수 있다. 매개변수로 raise, coerce, ignore가 있다
* 범주형 데이터를 사용하면 메모리가 효율적이다.
