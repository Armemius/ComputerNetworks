import matplotlib.pyplot as plt

bits = "110100011100000011000000"

bit_duration = 1
time = []
signal = []

t = 0
for b in bits:
    if b == "1":
        level = 1
    else:
        level = -1

    time += [t, t + bit_duration]
    signal += [level, level]

    t += bit_duration

fig, ax = plt.subplots(figsize=(14, 4))

ax.step(time, signal, where="post", color="black", linewidth=2)

for i in range(len(bits)):
    start = i
    end = i + 1
    if bits[i] == "1":
        ax.step([start, end], [1, 1], where="post", color="red", linewidth=2)
    else:
        ax.step([start, end], [-1, -1], where="post", color="blue", linewidth=2)

for i, b in enumerate(bits):
    ax.text(i + 0.5, -1.6, b, ha="center", fontsize=12)
    ax.text(i + 0.5, -2.1, str(i), ha="center", fontsize=10, alpha=0.5)

for i in range(len(bits) + 1):
    ax.axvline(i, linestyle="--", linewidth=0.5, color="gray")

ax.set_ylim(-2.5, 1.5)
ax.set_xlim(0, len(bits))

ax.set_yticks([-1, 0, 1])

ax.set_xlabel("Время")
ax.set_title("NRZ кодирование")

ax.grid(True, axis="y", linestyle=":")

plt.tight_layout()
plt.show()
