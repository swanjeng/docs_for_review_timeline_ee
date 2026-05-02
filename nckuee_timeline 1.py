import matplotlib.pyplot as plt
from datetime import date
import numpy as np
import matplotlib as mpl

path = "/home/swan/Downloads/LXGWWenKaiMonoTC-Regular.ttf"

mpl.font_manager.fontManager.addfont(path)

mpl.rcParams["font.family"] = "LXGW WenKai Mono TC"
mpl.rcParams["font.size"] = 28

# 日期僅作為等間距設定用
dates = [date(1900, 1, 1), date(1905, 1, 1), date(1910, 1, 1)]
min_date = date(np.min(dates).year - 5, np.min(dates).month, np.min(dates).day)
max_date = date(np.max(dates).year + 5, np.max(dates).month, np.max(dates).day)

label_dates = [date(1897, 7, 1), date(1901, 7, 1), date(1906, 7, 1)]

str1 = """高中畢業 ~ 入學前：
    1. 考 7 月的 APCS，挑戰
       實作 4 級分以上。
    2. 運用台大開放式課程的
       資源進行微積分和線性
       代數的先修。"""

str2 = """大一：
    1. 學習微積分、普通物理、計算機概論、程式
       設計、線性代數、邏輯系統等核心課程。
    2. 選修「電工實驗」、「邏輯系統實驗」、通
       識課「永續發展目標 (SDGs) 導論」等課程。
    3. 參與 電腦網路愛好社 社團。"""

str3 = """大二：
    1. 學習工程數學、電機概論、電路學、電子
       學等核心課程。
    2. 選修「平面顯示器概論」、「單晶片系統
       設計與應用」、「離散數學」、「計算機
       組織」和「資料結構緒論」等課程。"""

labels = [str1, str2, str3]

fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
ax.set_xlim(min_date, max_date)
ax.set_ylim(-2.1, 2)
ax.axhline(0, xmin=0.05, xmax=0.95, color=(0.5, 0, 0), zorder=1, lw=3)

ax.scatter(dates, np.zeros(len(dates)), s=240, color=(1, 0, 0), zorder=2)

label_offsets = [0.3, -1.5, 0.3]
for i in range(len(dates)):
    ax.text(label_dates[i], label_offsets[i], labels[i], ha='left',
            color=(0, 0, 0), linespacing=2, backgroundcolor=(1, 0.9, 0.9))

stems = np.zeros(len(dates))
stems[::2] = 0.3
stems[1::2] = -0.3
markerline, stemline, baseline = ax.stem(
    dates, stems, use_line_collection=True)
plt.setp(stemline, color=(1, 0.5, 0), lw=3)

# hide lines around chart
for spine in ["left", "top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

# hide tick labels
ax.set_xticks([])
ax.set_yticks([])

plt.show()
