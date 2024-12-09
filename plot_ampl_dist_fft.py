import sys
import numpy as np
import matplotlib.pyplot as plt


def parse_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    fft = None
    dist = 0
    data = []

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            if "FFT Num" in line:
                fft = int(line.split(":")[1].strip())
                dist = 0  # Reset dist after each header
        else:
            x, y = map(float, line.split())
            print(f'x = {x}, y = {y}')
            ampl = np.sqrt(x * x + y * y)
            data.append((ampl, fft, dist))
            dist += 1
    return data


def plot_data(data):
    ampl, fft, dist = zip(*data)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(fft, dist, ampl, c="r", marker="o")
    ax.set_xlabel("FFT")
    ax.set_ylabel("Distance")
    ax.set_zlabel("Amplitude")
    plt.show()


def main():
    filename = sys.argv[1]  # Имя файла с входными данными
    print("#" * 50)
    print(f"Для визуализации передан файл: {filename}")
    data = parse_file(filename)
    plot_data(data)


if __name__ == "__main__":
    main()
