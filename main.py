import pandas as pd
import acp.ACP as acp
import grafice
import grafice as g
import numpy as np


tabel = pd.read_csv('dataIN/dateInProiect.csv', index_col=0)
print(tabel)

varNume = list(tabel.columns)[1:]
print(varNume)
obsNume = list(tabel.index)
print(obsNume)

# extragem matricea asociata valorilor variabilelor cauzale
X = tabel[varNume].values
# print(X)

acp_model = acp.ACP(X)

# salvare matrice X standardizata in fisier CSV
Xstd = acp_model.getXstd()
Xstd_df = pd.DataFrame(data=Xstd, index=obsNume, columns=varNume)
Xstd_df.to_csv('dataOUT/Xstd.csv')

# realizare grafic varianta explicata de componentele principale
valProp = acp_model.getValProp()
g.componentePrincipale(valoriProprii=valProp)


# salvare in fisier CSV a componentelor principale
compPrin = acp_model.getCompPrin()
compPrin_df = pd.DataFrame(data=compPrin, index=obsNume, columns=('C'+str(j+1) for j in range(len(varNume))))
compPrin_df.to_csv('dataOUT/CompPrin.csv')

# corelograma factorilor de corelatie
factoriCorel = acp_model.getFactoriCorelatie()
factoriCorel_df = pd.DataFrame(data=factoriCorel, index=varNume, columns=('C'+str(j+1) for j in range(len(varNume))))
factoriCorel_df.to_csv('dataOUT/FactoriCorelatie.csv')
g.corelagrama(matrice=factoriCorel_df, titlu='Corelograma factorilor de corelatie')


# corelograma scorurilor
scoruri = acp_model.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri, index=obsNume, columns=('C'+str(j+1) for j in range(len(varNume))))
scoruri_df.to_csv('dataOUT/Scoruri.csv')
g.corelagrama(matrice=scoruri_df, titlu='Corelograma scorurilor (componentele principale stadardizate)')


# corelograma calitatii reprezentarii observatiilor pe axele componentelor
calObs = acp_model.getCalObs()
calObs_df = pd.DataFrame(data=calObs, index=obsNume, columns=('C'+str(j+1) for j in range(len(varNume))))
calObs_df.to_csv('dataOUT/CalitateObservatii.csv')
g.corelagrama(matrice=calObs_df, titlu='Corelograma calitatii reprezentarii observatiilor pe axele componentelor')

# corelograma contributiei observatiilor la varianta axelor componentelor
betha = acp_model.getBetha()
betha_df = pd.DataFrame(data=betha, index=obsNume, columns=('C'+str(j+1) for j in range(len(varNume))))
betha_df.to_csv('dataOUT/Betha.csv')
g.corelagrama(matrice=betha_df, titlu='Corelograma contributiei observatiilor la varianta axelor componentelor')


# corelograma comunitatilor (componentele principale regasite in variabilele initale)
comunitati = acp_model.getComun()
comunitati_df = pd.DataFrame(data=comunitati, index=varNume, columns=('C'+str(j+1) for j in range(len(varNume))))
comunitati_df.to_csv('dataOUT/Comunitati.csv')
g.corelagrama(matrice=comunitati_df, titlu='Corelograma comunitatilor (componentele principale regasite in variabilele initale)')


# crearea cercului corelatiilor pentru evidentierea corelatieie dintre variabilele initiale si C1, C2
g.cerculCorelatiilor(matrice=factoriCorel_df, titlu='Corelatia dintre variabilele initiale si C1, C2')

# crearea cercului corelatiilor pentru evidentierea legaturii dintre observatii si C1, C2
maxim_scor = np.max(scoruri)
minim_scor = np.min(scoruri)
print('Maxim scor, folosit ca raza pentru cercul corelatiilor: ', maxim_scor)
g.cerculCorelatiilor(matrice=scoruri_df, raza=maxim_scor, valMin=minim_scor, valMax=maxim_scor,
                     titlu='Distributia observatiilor in spatiul C1, C2')
g.afisare()
