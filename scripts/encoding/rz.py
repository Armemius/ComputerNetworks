import matplotlib.pyplot as plt

bits = "110100011100000011000000"

bit_duration = 1
half = bit_duration / 2

time = []
signal = []

t = 0

for b in bits:
    if b == "1":
        first = 1
    else:
        first = -1

    time += [t, t + half]
    signal += [first, first]

    time += [t + half, t + bit_duration]
    signal += [0, 0]

    t += bit_duration

fig, ax = plt.subplots(figsize=(14, 4))

ax.step(time, signal, where="post", color="black", linewidth=2)

t_col = 0
for b in bits:
    if b == "1":
        ax.step([t_col, t_col + half], [1, 1], where="post", color="red", linewidth=2)
    else:
        ax.step([t_col, t_col + half], [-1, -1], where="post", color="blue", linewidth=2)
    t_col += bit_duration

for i, b in enumerate(bits):
    ax.text(i + 0.5, -1.6, b, ha="center", fontsize=12)
    ax.text(i + 0.5, -2.1, str(i), ha="center", fontsize=10, alpha=0.5)

for i in range(len(bits) + 1):
    ax.axvline(i, linestyle="--", linewidth=0.5, color="gray")

ax.set_ylim(-2.5, 1.5)
ax.set_xlim(0, len(bits))

ax.set_yticks([-1, 0, 1])

ax.set_xlabel("Время")
ax.set_title("RZ кодирование")

ax.grid(True, axis="y", linestyle=":")

plt.tight_layout()
plt.show()
