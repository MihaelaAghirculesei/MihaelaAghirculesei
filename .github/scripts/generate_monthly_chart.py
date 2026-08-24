import json
import urllib.request
import datetime
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

USERNAME = "MihaelaAghirculesei"
OUTPUT_PATH = "imgs/year-activity.png"

url = f"https://github-contributions-api.jogruber.de/v4/{USERNAME}?y=last"
with urllib.request.urlopen(url) as r:
    data = json.load(r)

contributions = data["contributions"]
total = data["total"]["lastYear"]

monthly = defaultdict(int)
for c in contributions:
    d = datetime.date.fromisoformat(c["date"])
    monthly[(d.year, d.month)] += c["count"]

months = sorted(monthly.keys())
values = [monthly[m] for m in months]
labels = [datetime.date(y, m, 1).strftime("%b %y") for (y, m) in months]

fig, ax = plt.subplots(figsize=(14, 4.5), facecolor="#0d1117")
ax.set_facecolor("#0d1117")

max_value = max(values) if values else 1
colors = []
for v in values:
    ratio = v / max_value
    if v == 0:
        colors.append("#161b22")
    elif ratio < 0.25:
        colors.append("#0e4429")
    elif ratio < 0.5:
        colors.append("#006d32")
    elif ratio < 0.75:
        colors.append("#26a641")
    else:
        colors.append("#39d353")

bars = ax.bar(labels, values, color=colors, edgecolor="none", width=0.6)

for bar, v in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max_value * 0.02, str(v),
            ha="center", va="bottom", color="#e6edf3", fontsize=9)

ax.set_title(f"{USERNAME} — {total} contributions in the last year", color="#e6edf3", fontsize=13, pad=14, loc="left")
ax.tick_params(colors="#8b949e", labelsize=9)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.spines["bottom"].set_visible(True)
ax.spines["bottom"].set_color("#30363d")
ax.set_ylabel("Commits / month", color="#8b949e", fontsize=9)
ax.set_yticks([])

plt.tight_layout()
plt.savefig(OUTPUT_PATH, dpi=150, facecolor=fig.get_facecolor())
print(f"Saved {OUTPUT_PATH} — {total} contributions in the last year")
