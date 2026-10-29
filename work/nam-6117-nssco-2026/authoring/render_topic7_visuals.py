from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon
D=Path(__file__).resolve().parents[1]/'topics/7/visuals';D.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(D/(name+'.svg'),bbox_inches='tight');fig.savefig(D/(name+'.png'),dpi=140,bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(12,5));ax.axis('off');ax.set_xlim(-1,15);ax.set_ylim(-2,4)
colours=['#a92532','#c52d37','#dc4431','#e5792e','#edaa35','#e6d64b','#adce48','#54a55d','#3a9a97','#4381bb','#546fc2','#7456a9','#8c459b','#853b89','#703579']
for i,c in enumerate(colours):ax.add_patch(Rectangle((i-.45,1),.9,1,fc=c,ec='white'));ax.text(i,.65,str(i),ha='center')
ax.text(7,2.7,'Approximate Universal Indicator colours — pH 0–14',ha='center',fontsize=15)
for lo,hi,txt in [(-.4,6.4,'Acidic'),(6.6,7.4,'Neutral'),(7.6,14.4,'Alkaline')]:ax.plot([lo,hi],[.2,.2],c='#555');ax.text((lo+hi)/2,-.2,txt,ha='center')
ax.text(2,-1,'Litmus: blue → red',ha='center',color='#a72b38');ax.text(12,-1,'Litmus: red → blue',ha='center',color='#265c99')
ax.text(7,-1.7,'Match the supplied indicator chart. pH alone does not distinguish strength from concentration.',ha='center',fontsize=10)
save(fig,'VIS-6117-7-01')
fig,axs=plt.subplots(1,2,figsize=(13,12))
left=[('React','Warm reaction beaker: dilute H₂SO₄.\nAdd CuO with a spatula until excess remains.'),('Filter','Filter funnel and paper retain\nblack excess CuO residue. Keep blue filtrate.'),('Concentrate','Evaporating basin over a water bath.\nRemove some water; do not boil dry.'),('Cool and collect','Crystallising dish: cool for blue crystals.\nCollect, rinse sparingly with cold water and dry.')]
right=[('Mix solutions','AgNO₃ solution + NaCl solution.\nWhite AgCl precipitate forms.'),('Filter','Filter funnel and paper retain AgCl.\nKeep the white solid residue.'),('Wash','Rinse residue with distilled water.\nSoluble impurities pass into the filtrate.'),('Dry','Dry the collected AgCl appropriately.\nProtect from strong light; collect silver waste.')]
for ax,steps,title in zip(axs,[left,right],['Soluble salt: CuSO₄','Insoluble salt: AgCl']):
 ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,16);ax.set_title(title,fontsize=15,pad=12)
 for n,(heading,txt) in enumerate(steps):
  y=13.7-3.5*n;ax.add_patch(Rectangle((.2,y-1.5),9.6,2.9,fc='#edf4f8',ec='#567383'));ax.text(5,y+.8,heading,ha='center',weight='bold');ax.text(5,y-.05,txt,ha='center',va='center',fontsize=10,linespacing=1.5)
  if n<3:ax.annotate('',xy=(5,y-2.05),xytext=(5,y-1.55),arrowprops={'arrowstyle':'->','lw':2})
fig.suptitle('Follow the product through each separation',fontsize=17,y=.97)
fig.text(.5,.04,'Teacher-supervised preparation. Filtration separates solids from solution; it does not remove dissolved impurities from the filtrate.',ha='center',fontsize=10)
fig.tight_layout(rect=[0,.07,1,.94]);save(fig,'VIS-6117-7-02')
(D/'parameters.json').write_text(json.dumps({'pH_range':[0,14],'neutral':7,'colour_status':'approximate schematic; use supplied indicator chart','CuSO4_product_fraction':'filtrate before concentration/cooling','AgCl_product_fraction':'washed filter residue','no_complete_drying_CuSO4':True},indent=2)+'\n')
