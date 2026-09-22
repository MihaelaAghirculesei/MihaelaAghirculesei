import json
import urllib.request
import datetime
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

USERNAME = "MihaelaAghirculesei"
DESKTOP_PATH = "imgs/year-activity.png"
MOBILE_PATH = "imgs/year-activity-mobile.png"

url = f"https://github-contributions-api.jogruber.de/v4/{USERNAME}?y=last"
with urllib.request.urlopen(url) as r:
    data = json.load(r)

contributions = data["contributions"]

monthly = defaultdict(int)
for c in contributions:
    d = datetime.date.fromisoformat(c["date"])
    monthly[(d.year, d.month)] += c["count"]

current_month = (datetime.date.today().year, datetime.date.today().month)
months = sorted(m for m in monthly.keys() if m != current_month)
values = [monthly[m] for m in months]
labels = [datetime.date(y, m, 1).strftime("%b %y") for (y, m) in months]

# Title reflects exactly what's plotted (full months only), not the API's
# raw "last 365 days" total, which would still include the excluded
# current month and silently disagree with the sum of the bars.
total = sum(values)
range_label = ""
if months:
    start = datetime.date(months[0][0], months[0][1], 1).strftime("%b %y")
    end = datetime.date(months[-1][0], months[-1][1], 1).strftime("%b %y")
    range_label = f"{start} – {end}"

max_value = max(values) if values else 1


def color_for(v):
    ratio = v / max_value
    if v == 0:
        return "#161b22"
    elif ratio < 0.25:
        return "#0e4429"
    elif ratio < 0.5:
        return "#006d32"
    elif ratio < 0.75:
        return "#26a641"
    return "#39d353"


def draw_row(ax, m_slice, v_slice, l_slice, value_fontsize, tick_labelsize, bar_width):
    colors = [color_for(v) for v in v_slice]
    bars = ax.bar(l_slice, v_slice, color=colors, edgecolor="none", width=bar_width)
    for bar, v in zip(bars, v_slice):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max_value * 0.03, str(v),
                ha="center", va="bottom", color="#e6edf3", fontsize=value_fontsize, fontweight="bold")
    ax.set_facecolor("#0d1117")
    ax.set_ylim(0, max_value * 1.3)
    ax.tick_params(colors="#8b949e", labelsize=tick_labelsize)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.spines["bottom"].set_visible(True)
    ax.spines["bottom"].set_color("#30363d")
    ax.set_yticks([])


# --- Desktop: single row, all months, compact — this is how the chart
# reads fine already on a normal-width screen, so it's left basically as
# it originally was (same figure size and font sizes as the first version
# of this script), just with the current-month exclusion and the
# consistent title kept from later fixes.
fig, ax = plt.subplots(figsize=(14, 4.5), facecolor="#0d1117")
draw_row(ax, months, values, labels, value_fontsize=9, tick_labelsize=9, bar_width=0.6)
ax.set_title(f"{range_label} · {total} commits", color="#e6edf3", fontsize=13, pad=14, loc="left")
ax.set_ylabel("Commits / month", color="#8b949e", fontsize=9)
plt.tight_layout()
plt.savefig(DESKTOP_PATH, dpi=150, facecolor=fig.get_facecolor())
plt.close(fig)

# --- Mobile: same data, split into rows of 4 months with much larger
# fonts. GitHub always shrinks the desktop image to fit a narrow
# profile-page column, and neither a wider image nor a bigger font alone
# fixes that once 12 bars are packed into ~320px — what actually helps is
# fewer bars per row. Served only below the CSS breakpoint via <picture>
# in the README, so the desktop version above is untouched.
PER_ROW = 4
rows = [
    (months[i:i + PER_ROW], values[i:i + PER_ROW], labels[i:i + PER_ROW])
    for i in range(0, len(months), PER_ROW)
]
n_rows = len(rows)

fig, axes = plt.subplots(n_rows, 1, figsize=(15.5, 6.2 * n_rows), facecolor="#0d1117")
if n_rows == 1:
    axes = [axes]
# No username in the title here either: it's already the page's big H1
# right above this image.
fig.suptitle(f"{range_label} · {total} commits",
             color="#e6edf3", fontsize=60, x=0.02, ha="left", y=0.99)
for ax, (m_slice, v_slice, l_slice) in zip(axes, rows):
    draw_row(ax, m_slice, v_slice, l_slice, value_fontsize=44, tick_labelsize=40, bar_width=0.5)
axes[0].set_ylabel("Commits / month", color="#8b949e", fontsize=40)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(MOBILE_PATH, dpi=150, facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Saved {DESKTOP_PATH} and {MOBILE_PATH} — {range_label} · {total} commits")
