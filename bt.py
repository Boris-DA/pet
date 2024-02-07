train_name = '3ТЭ10МК'

def_data = df.loc[df['name']==train_name]
len_list = int(def_data['appointedServiceLifeUntilDepreciation'].item())

table_data = pd.DataFrame()
table_data['Год'] = range(1, len_list+1)
table_data['Пробег, км'] = table_data['Год'] * def_data['averageAnnualMileage'].item()

dynamic_table_left = pd.DataFrame(dict(def_data['dynamicRepairTypes'])[1])
static_table_left = pd.DataFrame(dict(def_data['leftRepairTypes'])[1])

dynamic_list = list(dynamic_table_left['name'])

table_data[list(dynamic_table_left['name'])] = 0
table_data[list(static_table_left['name'])] = 0

if 'ТО-2' in dynamic_list:
    dynamic_list.remove('ТО-2')    

for i in table_data.index:

    var_to4 = int(static_table_left.loc[static_table_left['name'] == 'ТО-4']['interval'].item())
    var_kr = int(static_table_left.loc[static_table_left['name'] == 'КР']['interval'].item())
    var_cr = int(static_table_left.loc[static_table_left['name'] == 'СР']['interval'].item())    
        
    if i == 0:
        table_data.loc[i, 'ТО-4'] = math.floor(table_data.loc[i, 'Пробег, км'] / var_to4)
        table_data.loc[i, 'КР'] = math.floor(table_data.loc[i, 'Пробег, км'] / var_kr) 
        table_data.loc[i, 'СР'] = math.floor(table_data.loc[i, 'Пробег, км'] / var_cr - table_data['КР'][i]) 
            
    else:
        table_data.loc[i, 'ТО-4'] =  math.floor(table_data.loc[i, 'Пробег, км'] / var_to4 - table_data['ТО-4'].cumsum()[i-1])
        table_data.loc[i, 'КР'] =  math.floor(table_data.loc[i, 'Пробег, км'] / var_kr - table_data['КР'].cumsum()[i-1])
        table_data.loc[i, 'СР'] =  math.floor((table_data.loc[i, 'Пробег, км'] / var_cr) - table_data['СР'].cumsum()[i-1] - table_data['КР'].cumsum()[i-1] - table_data.loc[i, 'КР'])

table_data['ТО-5б'] = table_data['КР'] + table_data['СР']
table_data['ТО-5в'] = table_data['КР'] + table_data['СР']        


for i in dynamic_list[::-1]:
    for j in table_data.index:

        dv = int(dynamic_table_left.loc[dynamic_table_left['name'] == i]['interval'].item())
        
        if j == 0:
            table_data.loc[j, i] = math.floor(table_data.loc[j, 'Пробег, км'] / dv)  
            
        else:
            table_data.loc[j, i] = (table_data.loc[j, 'Пробег, км'] / dv)
            table_data.loc[j, i] = math.floor(table_data.loc[j, i] - table_data[i].cumsum()[j-1])

for j in table_data.index:
    a = []
    for i in dynamic_list[::-1]:
        a.append(table_data.loc[j, i])
        table_data.loc[j, i] = table_data.loc[j, i] - a[dynamic_list[::-1].index(i)-1] 

for j in table_data.index:
    a = []
    if 'ТО-2' in table_data.columns:
        if j == 0:
            table_data.loc[j, 'ТО-2'] = math.floor((table_data.loc[j, 'Год'] * 365 * 24) / 72)
        else:
            table_data.loc[j, 'ТО-2'] = math.floor((table_data.loc[j, 'Год'] * 365 * 24) / 72 - table_data['Год'].cumsum()[j-1])
        
table_data[dynamic_list] = table_data[dynamic_list].astype(int)        
        
table_data['ТОиТР'] = 22855.86
table_data['СР_total'] = table_data['СР'] * 79352.208
table_data['КР_total'] = table_data['КР'] * 93259.662
table_data['ТО-4_total'] = table_data['ТО-4'] * 205.984
table_data['ТО-5б_total'] = table_data['ТО-5б'] * 720.799
table_data['ТО-5в_total'] = table_data['ТО-5в'] * 2442.204
table_data['НР_total'] = (table_data['ТОиТР'] + table_data['ТО-4_total'] + table_data['ТО-5б_total'] + table_data['ТО-5в_total']) * 0.05

table_data
