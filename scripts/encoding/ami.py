import matplotlib.pyplot as plt

bits = "110100011100000011000000"

bit_duration = 1
time = []
signal = []

t = 0
last_level = -1

for b in bits:
    if b == "1":
        last_level = -last_level
        level = last_level
    else:
        level = 0

    time += [t, t + bit_duration]
    signal += [level, level]

    t += bit_duration

fig, ax = plt.subplots(figsize=(14, 4))

ax.step(time, signal, where="post", color="black", linewidth=2)

t_col = 0
last_level = -1
for b in bits:
    if b == "1":
        last_level = -last_level
        color = "red"
        level = last_level
    else:
        color = "blue"
        level = 0
    ax.step([t_col, t_col + bit_duration], [level, level], where="post", color=color, linewidth=2)
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
ax.set_title("AMI кодирование")

ax.grid(True, axis="y", linestyle=":")

plt.tight_layout()
plt.show()
