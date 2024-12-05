

# #1 데이터 시각화
import matplotlib.pyplot as plt
import numpy as np

year=[2000,2005,2010,2015,2020]
GDP=[300,400,500,600,750]

plt.plot(year,GDP,color='b',marker='o',linestyle='--')

plt.xlim(1995,2025)
plt.ylim(200,800)

plt.xlabel("Year")
plt.ylabel("GDP")
plt.title("GDP Graph")
plt.show()


#2 여러개의 데이터 시각화

years=[2000,2005,2010,2015,2020]
kor_GDP=[300,400,500,600,700]
jap_GDP=[500,600,700,800,900]
chi_GDP=[100,200,400,800,1500]

plt.plot(years,kor_GDP,color='r',marker='o',linestyle='--',label='korea')
plt.plot(years,jap_GDP,color='b',marker='*',linestyle='-',label='japen')
plt.plot(years,chi_GDP,color='g',marker='^',linestyle=':',label='china')

plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend()
plt.xticks(years)
plt.title("GDP Comparison")
plt.show()



#3 막대그래프 여러개의 데이터 시각화

year_s=[2000,2005,2010,2015,2020]
kor_p=[45,46,47,48,50]
jap_p=[120,122,124,126,125]
chi_p=[1280,1300,1330,1350,1400]

x_line=np.arange(len(year_s))
width=0.2
plt.bar(x_line+0.0,kor_p,width,color="#ff9999",label='korea')
plt.bar(x_line+0.2,jap_p,width,color="#99ccff",label='japen')
plt.bar(x_line+0.4,chi_p,width,color="#99ff99",label='china')


plt.title("Population Comparison")
plt.legend()
plt.xticks(x_line,year_s)
plt.xlabel('Year')
plt.ylabel('population')
plt.show()
