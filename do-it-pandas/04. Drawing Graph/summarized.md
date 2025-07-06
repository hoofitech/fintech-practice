## 04-1. 데이터 시각화란?
1. '앤스컴 콰르텟'(Anscombe's quartet): 4개의 데이터셋으로 이루어진 데이터셋 예제로 평균, 분산, 상관관계, 회귀선이 모두 같아서
   같은 데이터셋으로 보일 수도 있지만 시각화하면 모두 경향이 다름
2. seaborn 라이브러리에 속해 있기 때문에 import seaborn as sns로 seaborn 라이브러리를 호출 후
   sns.load_dataset("anscombe")으로 불러올 수 있음

## 04-2. matplotlib 라이브러리란?
1. matplotlib는 널리 사용하는 파이썬 시각화 라이브러리이다. 하위 패키지인 pyplot을 블러오면 라이브러리의 다양한 시각화 기능을 사용할 수 있다.
   import matplotlib.pyplot as plt로 호출
2. plt.plot(x벡터, y벡터): 대부분의 기본 그래프를 그릴 수 있다.
3. plt.show(): 그래프를 호출할 수 있다.
4. plt.plot(x벡터, y벡터, 'o'): 인수로 'o'를 전달하면 점 그래프 형식으로 리턴함

### 그림 영역과 하위 그래프 이해하기
1. matplotlib은 하나의 그림 영역(Figure 객체)에 여러 개의 하위 그래프(Axes 객체)를 그리는 기능을 제공
```python 
     fig = plt.figure() # 그림 영역 Figure 객체 생성 
     axes1 = fig.add_subplot(2,2,1) # add_subplot(행,열,위치) 메서드로 하위 객체 Axes 생성 
     axes2 = fig.add_subplot(2,2,2)
     axes3 = fig.add_subplot(2,2,3)
     axes4 = fig.add_subplot(2,2,4)
```

2. axes.set_title(): 각 하위 그래프 axes의 이름을 지정할 수 있다.
3. fig.suptitle(): 그림객체 figure에 이를을 지정할 수 있다.
4. fig.set_tight_layout(True): 하위 그래프 사이에 제목을 삽입할 공간을 확보합니다.

📊 Anscombe's Quartet 시각화
![Anscombe plot](Vizualizations/Anscombe_plot.png)

## 04-3. matplotlib으로 그래프그리기
1. axes.set_xlabel: Axes 객체의 x축 이름을 설정
2. axes.set_ylabel: Axes 객체의 y축 이름을 설정
### 일변량 그래프 그리기
#### 히스토그램 그리기
axes.hist(data=데이터셋, x= '분석할 데이터열', bins= x축의 구간 개수) : 히스토그램 생성하는 메서드
```python
히스토그램 예제
fig = plt.figure() #figure 객체로 그림 영역 생성
axes1 = fig.add_subplot(1,1,1) #하위그래프 1개 생성

axes1.hist(data=tips, x='total_bill', bins=10) #tips 데이터의 total_bill열의 데이터를 히스토그램의 나타냄

axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Frequency')

plt.show()
```
📊 Histogram by matplotlib 시각화
![histogram by matplotlib](Vizualizations/Histogram_plt.png)

### 이변량 그래프 그리기
#### 산점도 그래프 그리기
axes.scatter(x축의 값, y축의 값): 산점도그래프 생성하는 메서드
```python
산점도 그래프 예제
scatter_plot = plt.figure() #figure 그림 객체 생성
axes1 = scatter_plot.add_subplot(1,1,1) #하위 그래프 생성

axes1.scatter(tips['total_bill'], tips['tip']) #산점도 그래프를 생성하는 scatter() 메서드, total bill과 tip의 상관 관계 비교

axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

plt.show()
```
📊 Scatterplot by matplotlib 시각화
![Scatterplot by matplotlib](Vizualizations/Scatterplot_plt.png)
#### 박스 그래프 그리기
axes.boxplot(x=[데이터1, 데이터2], labels=[데이터이름]): 박스형 그래프로 두가지 변수를 비교함
```python
박스 그래프 예제
boxplot = plt.figure()
axes1 = boxplot.add_subplot(1,1,1)

axes1.boxplot(
    x=[
        tips[tips['sex'] == 'Female']['tip'],
        tips[tips['sex'] == 'Male']['tip']
    ], labels = ['Female', 'Male']
)
#이산 변수: 성별
#연속변수: tip의 분산
axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')

plt.show()
```
📊 Boxplot by matplotlib 시각화
![Boxplot by matplotlib](Vizualizations/Boxplot_plt.png)

### 다변량 그래프 그리기
1. 3개 이상의 변수를 나타내려면 산점도 그래프에서 점의 색깔 or 크기로 나타내는 방법이 있음
2. 사람은 크기 차이보다 색상 차이를 더 쉽게 구분함
3. 점의 크기 차이가 실제 값의 차이를 반영하는지도 확인해야함, 반지름이 r인 원의 넓이는 πr^2이므로 제곱을 반영함

#### 변수가 여러개인 그래프 그리기
-scatter()의 매개변수
1. 매개변수 s: 점의 크기를 지정할 수 있음
2. 매개변수 c: 점의 색상을 나타냄
3. alpha: 점의 투명도를 0~1 사이로 나타냄
4. *series.map(): 시리즈의 각 값에 함수를 적용하는 메서드. 파이썬의 map과는 다름
```python
변수가 여러개인 그래프 예제
colors = {"Female" : "#f1a340", "Male" : "#998ec3"} #성별로 색깔 지정

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1,1,1)

axes1.scatter(data=tips,
             x = 'total_bill',
             y = 'tip',
             s=tips['size']**2*10, #점의 크기를 나타내는 매개변수를 s, size를 제곱한 사이즈에 10을 곱하여 원 크기로 나타냄
             c = tips['sex'].map(colors), # 색상을 나타내는 매개변수 c, 성별에 따른 색상
             alpha = 0.5) #alpha는 점의 투명도를 0~1 사이의 값으로 표현, 많이 겹치면 더 진해짐

axes1.set_title('Colored by Sex and Sized by Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

scatter_plot.suptitle('Total Bill vs Tip')

plt.show()
```
📊 Total_billvsTip 시각화

![Total_billvsTip](Vizualizations/TotalbillvsTip.png)

## 04-4. seaborn으로 그래프 그리기
seaborn 라이브러리는 matplotlib에 기반을 둔 통계 그래프의 특화된 라이브러리이다.
### 다양한 그래프 그려 보기
#### 일변량 그래프 그리기
##### 1. 히스토그램 그리기
1. plt.subplot(): seaborn에서는 그림 객체와 하위 그래프 객체를 한 줄에 출력할 수 있음
2. sns.histplot(data=데이터셋, x='분석할 데이터열', ax=ax): 매개변수 ax에는 하위 그래프 객체를 지정한다.
```python
seaborn으로 히스토그램 그리기 예제
hist, ax = plt.subplots() #maplotlib과 다르게 그림 영역과 하위 그래프 객체를 한 번에 생성

sns.histplot(data= tips, x= 'total_bill', ax=ax) #ax에는 생성한 하위 그래프 객체를 지정
ax.set_title('Total Bill Histogram')

plt.show()
```
📊 Histogram by seaborn 시각화
![Histogram by seaborn](Vizualizations/Histgram_sns.png)
##### 2. 밀도 분포 그래프 그리기
1. 밀도 분포 그래프: 각 값을 중심으로 정규 분포를 그리고 곡선 아래 넓이가 1이 되도록 겹친 그래프를 매끄럽게 만든것,
  커널 밀도 추정(kernel density estimation)이라고도 함
2. sns.kdeplot(data=데이터셋, x='분석할 데이터열', ax=ax): 밀도 분포 그래프를 그리는 메서드
   
##### 3. 러그 그래프 그리기
1. 
