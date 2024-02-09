import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import warnings; warnings.filterwarnings(action = 'once')
import plotly.express as px
import plotly.subplots as sp
from plotly import graph_objects as go
from pandas.plotting import register_matplotlib_converters

data_raw = pd.read_excel(r'C:\Users\b.darzhaniya\Desktop\Jupyter Notebook\Свод.xlsx')

fig = px.area(data_raw, x='Date', y='Нагрузка, чел', color='Проект')

fig.update_layout(
    
    title_text='Распределение рабочей нагрузки',
    
    title_font=dict(
        color='black',
        family='Brutal Type',
        size=18
    ),

    font=dict(
        color='black',
        family='Brutal Type',
        size=14
    ),

    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='middle',

    showlegend=False,
    autosize=True,

    paper_bgcolor='white',
    plot_bgcolor='#fff',

    autotypenumbers='convert types',
    
    modebar=dict(
        activecolor='black',
        orientation='h',
        # bgcolor='',
        # color=''
    ),

    hovermode='closest',
    clickmode='event',
    dragmode='zoom',
    selectdirection='any'





)
 

fig.show()
