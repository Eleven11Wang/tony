unstack647="../planecsv/647_face_plane408_176.csv"
stack647="../planecsv/245.180.b.csv"
stack5611="../planecsv/face_plane91_232.csv"
stack5612="../planecsv/face_plane355_63.csv"
unstack561="../planecsv/face_plane359_164.csv"
import matplotlib.pyplot as plt
import lib
wantLs=[unstack647,stack647,unstack561,stack5611,stack5612]
import random
def read_file(filename):
    frameLs=[]
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        frame,event=line.split(",")
        if event=='1':
            frameLs.append(int(frame))
    return frameLs

def makex(nub, lx, nx=0.3):
    randx = [nub] * len(lx)
    for idx, x in enumerate(randx):
        randx[idx] = x + random.uniform(-nx/lx[idx], nx/lx[idx])
    return randx

continuityStck=[]
for stck in wantLs:
    frameLs=read_file(stck)
    continuityLs=lib.findContinuityPlanes(frameLs)
    continuityStck.append(continuityLs)
continuityStck.append([10000])



f, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(4, 6), gridspec_kw={'height_ratios': [1, 2]})
ax2.plot(makex(1, continuityStck[0]), continuityStck[0], 'o', color="m", markersize=5)
ax2.plot(makex(2, continuityStck[1]), continuityStck[1], 'o', color="m", markersize=5)
ax2.plot(makex(3, continuityStck[2]), continuityStck[2], 'o', color="g", markersize=5)
ax2.plot(makex(4, continuityStck[3]), continuityStck[3], 'o', color="g", markersize=5)
ax2.plot(makex(5, continuityStck[4]), continuityStck[4], 'o', color="g", markersize=5)
ax.plot([6], continuityStck[5], 'o', color='k', markersize=5)
ax.set_ylim(9500,10500)  # outliers only
ax2.set_ylim(0, 50)

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()
#plt.ylabel("length(frame)")

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)  # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
plt.xticks(range(1, 7), ["u`AF647", "AF647", 'u`Cy3B', 'Cy3B', 'Cy3B','marker'], fontsize=9, rotation=45)
plt.show()


#f.savefig("VisualizeDistribution_green.pdf")

