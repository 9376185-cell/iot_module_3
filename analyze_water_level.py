import csv
import numpy as np
import matplotlib.pyplot as plt

CSV_FILENAME = "water_level.csv"
PLOT_FILENAME = "water_level_plot.png"
TANK_HEIGHT_CM = 100.0


def load_water_data(filename: str):
    times, distances, levels = [], [], []
    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("time_s") or not row.get("water_level_cm"):
                continue
            times.append(float(row["time_s"]))
            distances.append(float(row["distance_cm"]))
            levels.append(float(row["water_level_cm"]))
    return np.array(times), np.array(distances), np.array(levels)


def main():
    times, distances, levels = load_water_data(CSV_FILENAME)

    mean_level = float(np.mean(levels))
    min_level = float(np.min(levels))
    max_level = float(np.max(levels))
    std_level = float(np.std(levels))

    print("=" * 60)
    print("АНАЛІЗ ПОКАЗНИКІВ РІВНЯ ВОДИ У РЕЗЕРВУАРІ (HC-SR04)")
    print("=" * 60)
    print(f"Кількість вимірювань:        {len(levels)}")
    print(f"Висота резервуара:           {TANK_HEIGHT_CM:.1f} см")
    print(f"Середній рівень води:        {mean_level:.2f} см")
    print(f"Мінімальний рівень води:     {min_level:.2f} см")
    print(f"Максимальний рівень води:    {max_level:.2f} см")
    print(f"Стандартне відхилення:       {std_level:.2f} см")
    print("=" * 60)

    plt.figure(figsize=(10, 5))
    plt.plot(
        times,
        levels,
        marker="o",
        linewidth=2,
        color="#2563eb",
        label="Поточний рівень води (см)",
    )
    plt.axhline(
        y=mean_level,
        color="#dc2626",
        linestyle="--",
        linewidth=2,
        label=f"Середній рівень води ({mean_level:.2f} см)",
    )

    plt.fill_between(times, levels, alpha=0.12, color="#2563eb")
    plt.title("Динаміка рівня води у резервуарі (сенсор HC-SR04, Wokwi)")
    plt.xlabel("Час вимірювання, с")
    plt.ylabel("Рівень води, см")
    plt.ylim(0, TANK_HEIGHT_CM + 5)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="best")
    plt.tight_layout()

    plt.savefig(PLOT_FILENAME, dpi=160)
    print(f"Графік збережено у файл: {PLOT_FILENAME}")
    plt.show()


if __name__ == "__main__":
    main()