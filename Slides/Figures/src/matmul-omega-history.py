import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":11})
pts=[(1969,2.8074),(1978,2.796),(1979,2.780),(1981,2.522),(1981.5,2.517),(1982,2.496),
(1986,2.479),(1990,2.375477),(2010,2.3737),(2012,2.372873),(2014,2.3728639),(2020,2.3728596),
(2023,2.371866),(2024,2.371552)]
def steps(start_y,x0,x1):
    xs=[x0];ys=[start_y]
    for x,y in pts:
        if x<x0: continue
        xs+=[x,x];ys+=[ys[-1],y]
    xs.append(x1);ys.append(ys[-1]);return xs,ys
LINE="#006400"
fig,ax=plt.subplots(figsize=(10,5.6))
xs,ys=steps(3,1965,2027)
ax.plot(xs,ys,color=LINE,lw=2.4)
ax.plot([p[0] for p in pts],[p[1] for p in pts],"o",ms=4.5,mfc="white",mec=LINE,mew=1.4)
ax.axhline(2,color="black",lw=0.8,ls="--")
ax.text(1966,2.015,r"$\omega \geq 2$ (trivial lower bound)",fontsize=10)
lab=[(1969,2.8074,"Strassen",(6,6)),(1978,2.796,"Pan",(-18,10)),(1979,2.780,"Bini et al.",(6,8)),
(1981,2.522,"Schönhage",(-70,8)),(1981.5,2.517,"Romani",(8,8)),(1982,2.496,"Coppersmith, Winograd",(-60,-40)),
(1986,2.479,"Strassen",(8,6)),(1990,2.375477,"Coppersmith, Winograd",(20,-22))]
for x,y,t,o in lab:
    ax.annotate(t,(x,y),xytext=o,textcoords="offset points",fontsize=9,arrowprops=dict(arrowstyle="-",lw=0.5,color="gray"))
ax.set_xlim(1965,2027); ax.set_ylim(1.95,3.05)
ax.set_xlabel("Year"); ax.set_ylabel(r"Best known bound on $\omega$")
for s in ["top","right"]: ax.spines[s].set_visible(False)
# zoom box marker on main plot
ax.add_patch(plt.Rectangle((1988,2.366),38,0.016,fill=False,lw=0.6,ls=":",color="black"))
ins=fig.add_axes([0.53,0.50,0.44,0.42])
xs,ys=steps(2.3762,1988,2026.5)
ins.plot(xs,ys,color=LINE,lw=2.2)
late=[p for p in pts if p[0]>=1990]
ins.plot([p[0] for p in late],[p[1] for p in late],"o",ms=4,mfc="white",mec=LINE,mew=1.3)
il=[(1990,"Coppersmith, Winograd",(4,5)),(2010,"Stothers",(-50,-4)),(2012,"Vassilevska Williams",(12,26)),
(2014,"Le Gall",(-16,-18)),(2020,"Alman, V. Williams",(-30,7)),(2023,"Duan, Wu, Zhou",(-80,-6)),
(2024,"V. Williams, Xu, Xu, Zhou",(-130,-22))]
for (x,t,o) in il:
    y=dict(late)[x]
    ins.annotate(t,(x,y),xytext=o,textcoords="offset points",fontsize=7.5,arrowprops=dict(arrowstyle="-",lw=0.4,color="gray"))
for (x,y) in late:
    pass
ins.set_xlim(1988,2026.5); ins.set_ylim(2.3706,2.3762)
ins.tick_params(labelsize=8)
ins.set_title("Zoom: 1990 to 2024",fontsize=9)
for s in ["top","right"]: ins.spines[s].set_visible(False)
fig.savefig("matmul-omega-history.png",dpi=160,bbox_inches="tight"); fig.savefig("matmul-omega-history.svg",bbox_inches="tight")
