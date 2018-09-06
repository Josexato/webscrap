import numpy as np
import matplotlib.pyplot as plt

poblacion = np.random.normal(45000, 10000.0, 500000)

#plt.hist(poblacion, 50)
#plt.show()

pob_mean=np.mean(poblacion)
print('media poblacion: '+str(pob_mean))

pob_sdv=np.std(poblacion)
print('desviacion estandar poblacion: '+str(pob_sdv))

mue_lst=list()
mue_mean_lst=[]
mue_var_s_lst=[]
mue_sdv_s_lst=[]
mue_var_i_lst=[]
mue_sdv_i_lst=[]
mue_len=2
res=[]
s=0
i=0
for x in range(0, 1000):
    mue=np.random.choice(poblacion,mue_len,False)
    mue_lst.append(mue)
    tmp_mean=np.mean(mue)
    mue_mean_lst.append(tmp_mean)
    mue_tmp_sumdifsq=0
    for x in np.nditer(mue):
        mue_tmp_sumdifsq = (mue_tmp_sumdifsq + (x - tmp_mean)**2)
    mue_var_s=mue_tmp_sumdifsq / mue_len
    mue_var_i=mue_tmp_sumdifsq / (mue_len-1)
    mue_var_s_lst.append(mue_var_s)
    mue_var_i_lst.append(mue_var_i)
    mue_sdv_s = (mue_var_s)**0.5
    mue_sdv_i = (mue_var_i)**0.5
    mue_sdv_s_lst.append(mue_sdv_s)
    mue_sdv_i_lst.append(mue_sdv_i)
    if(abs(pob_sdv-mue_sdv_s)<abs(pob_sdv-mue_sdv_i)):
        res.append("s")
        s=s+1
    else:
        res.append("i")
        i=i+1


print("promedio de las medias de las muestras")
print(np.mean(mue_mean_lst))


print("promedio de las varianzas sesgadas de las muestras")
print(np.mean(mue_var_s_lst))

print("promedio de las desviaciones estandar sesgadas de las muestras")
print(np.mean(mue_sdv_s_lst))


print("promedio de las varianzas Insesgadas de las muestras")
print(np.mean(mue_var_i_lst))

print("promedio de las desviaciones estandar Insesgadas de las muestras")
print(np.mean(mue_sdv_i_lst))

print(i,s)

mue_mean_s_lst=[]
mue_mean_i_lst=[]

for idx, r in enumerate(res):
    if(r=="i"):
        mue_mean_s_lst.append(mue_mean_lst[idx])
    else:
        mue_mean_i_lst.append(mue_mean_lst[idx])
print("media de medias de las muestras donde la varianza sesgada es más precisa")
print(np.mean(mue_mean_s_lst))


print("media de medias de las muestras donde la varianza insesgada es más precisa")
print(np.mean(mue_mean_i_lst))

print("Varianza de medias de las muestras donde la varianza sesgada es más precisa")
print(np.var(mue_mean_s_lst))


print("Varianza de medias de las muestras donde la varianza insesgada es más precisa")
print(np.var(mue_mean_i_lst))