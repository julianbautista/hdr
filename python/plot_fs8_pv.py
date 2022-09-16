import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

a = pd.read_csv('fs8_pv_data.txt')

colors = {'Max-likelihood': 'C0',
          'Compressed 2pt': 'C1',
          'Density vs velocity': 'C2'}

plt.figure()

labels_used = []
for i in range(len(a)):
    line = a.iloc[i]
    y = -i 
    low = line['fs8_lower_error_stat']
    upp = line['fs8_upper_error_stat']

    if line['Method'] not in labels_used: 
        label = line['Method']
        labels_used.append(label)
    else: 
        label = None
    
    low_syst = line['fs8_lower_error_syst']
    upp_syst = line['fs8_upper_error_syst']
    
    if not low_syst == "None":
        low_syst = float(low_syst)
        upp_syst = float(upp_syst) 
        low_total = np.sqrt(low**2+low_syst**2)
        upp_total = np.sqrt(upp**2+upp_syst**2)
        plt.errorbar(line['fs8_value'], y, xerr=[[low_total], [upp_total]], fmt='o', color=colors[line['Method']], alpha=0.5, elinewidth=1)
    plt.errorbar(line['fs8_value'], y, xerr=[[low], [upp]], fmt='o', color=colors[line['Method']], label=label, elinewidth=2)
    plt.text(0.1, y, line['Paper'], va='center', ha='center')
    plt.text(0.7, y, line['Dataset'].replace(' ', ', '), va='center', ha='center')

plt.text(0.1, 1, 'Authors', va='center', ha='center', fontweight='bold')
plt.text(0.7, 1, 'Dataset', va='center', ha='center', fontweight='bold')
plt.xlim(-0.1, 0.9)
plt.ylim(-i-2, 2)
plt.xlabel('$f\sigma_8$', fontsize=12)
plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = True, bottom = True)
plt.legend(ncol=3, loc='lower center', frameon=True, fontsize=9)
#plt.axvline()
plt.savefig('plot_fs8_pv.pdf')