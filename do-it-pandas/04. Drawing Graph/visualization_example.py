fig = plt.figure()
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)

axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

axes1.set_title('dataset_1') # 각 axes의 이름을 set_title()메서드로 지정
axes2.set_title('dataset_2')
axes3.set_title('dataset_3')
axes4.set_title('dataset_4')

fig.suptitle("Anscombe Data") # 그림영역 fig의 이름을 suptitle()메서드로 지정
fig.set_tight_layout(True) #데이터와 하위 그래프의 제목이 겹칠 수 있기 때문에 set_tight_layout() 메서드로 제목을 삽입할 공간을 확보
plt.savefig("Anscombe_plot.png")
