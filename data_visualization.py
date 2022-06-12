import matplotlib.pyplot as plt
import plotly.express as px
plt.style.use('ggplot')
import pandas as pd

df = pd.read_csv('220511_monatszahlenmonatszahlen2204_verkehrsunfaelle.csv')
df.info()
df[['MONAT']] = df[['MONAT']].apply(lambda x: x.str[-2:])
#df.drop(['MONATSZAHL','AUSPRAEGUNG','VERAEND_VORJAHRESMONAT_PROZENT','ZWOELF_MONATE_MITTELWERT'],axis=1 ,inplace=True)
df = df[['MONATSZAHL', 'AUSPRAEGUNG','JAHR','MONAT','WERT']]
df = df.dropna()

df['JAHR'] = df['JAHR'].astype(str)
month_description = {"01": "Jan","02": "Feb","03": "Mar","04": "Apr","05": "May","06": "Jun",
                       "07": "Jul","08": "Aug","09": "Sep","10": "Oct","11": "Nov","12": "Dec"}
df['MONAT'] = df['MONAT'].map(month_description)
df['MONAT_JAHR'] = df['MONAT'] + df['JAHR']

plt.title('Number of Accidents per Category', fontsize=20)
plt.xlabel("Date[MONAT]",fontsize=16)
plt.ylabel("Count [WERT]",fontsize=16)

fig = px.histogram(df, x="JAHR", y="WERT")
fig.show()

