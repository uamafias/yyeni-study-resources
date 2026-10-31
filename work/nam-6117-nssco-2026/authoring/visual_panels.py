def save_panels(fig, directory, name, selections):
    for role, indices in selections.items():
        for i, ax in enumerate(fig.axes): ax.set_visible(i in indices)
        fig.canvas.draw()
        boxes=[fig.axes[i].get_tightbbox(fig.canvas.get_renderer()).transformed(fig.dpi_scale_trans.inverted()) for i in indices]
        from matplotlib.transforms import Bbox
        bbox=Bbox.union(boxes).expanded(1.04,1.04)
        for ext in ['svg','png']: fig.savefig(directory/(name+'-'+role+'.'+ext),bbox_inches=bbox,dpi=130)
    for ax in fig.axes: ax.set_visible(True)
