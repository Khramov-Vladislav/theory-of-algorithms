"""График доли живых клеток: данные из data/population.txt (вывод Experiments.java)."""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3})

pop = np.genfromtxt("data/population.txt", names=True)

fig, ax = plt.subplots(figsize=(6, 4))

for d in (10, 30, 50, 70, 90):
    ax.plot(pop["t"], pop[f"d{d}"], label=f"{d} %")
ax.set_xlabel("Поколение $t$")
ax.set_ylabel("Доля живых клеток")
ax.set_title("Доля живых клеток ($50 \\times 50$, 20 запусков)")
ax.legend(title="Начальная плотность")

fig.tight_layout()
fig.savefig("automaton_analysis.png", dpi=200)
fig.savefig("automaton_analysis.pdf")
