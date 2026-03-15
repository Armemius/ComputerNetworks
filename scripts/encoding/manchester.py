import matplotlib.pyplot as plt

bits = "110100011100000011000000"

bit_duration = 1
half = bit_duration / 2

time = []
signal = []
transitions = []

t = 0

for i, b in enumerate(bits):

    if b == "1":
        first = -1
        second = 1
        color = "red"  # LH
    else:
        first = 1
        second = -1
        color = "blue"  # HL

    time += [t, t + half]
    signal += [first, first]

    transitions.append((t + half, first, second, color))

    time += [t + half, t + bit_duration]
    signal += [second, second]

    t += bit_duration


fig, ax = plt.subplots(figsize=(14, 4))

ax.step(time, signal, where="post", linewidth=2, color="black")

for x, y1, y2, color in transitions:
    ax.plot([x, x], [y1, y2], color=color, linewidth=2)

for i, b in enumerate(bits):
    ax.text(i + 0.5, -1.6, b, ha="center", fontsize=12)
    ax.text(i + 0.5, -2.1, str(i), ha="center", fontsize=10, alpha=0.5)

for i in range(len(bits) + 1):
    ax.axvline(i, linestyle="--", linewidth=0.5, color="gray")

ax.set_ylim(-2.5, 1.5)
ax.set_xlim(0, len(bits))

ax.set_yticks([])
ax.set_ylabel("")

ax.set_xlabel("Время")
ax.set_title("Манчестерское кодирование")

ax.grid(True, axis="y", linestyle=":")

plt.tight_layout()
plt.show()
