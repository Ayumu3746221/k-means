from point import Point
from kmeans import k_means

if __name__ == "__main__":
    num_points = 6
    dims = 2
    # ランダムなデータ点を生成（ここでは2次元の例）
    points = [Point.random(dims) for _ in range(num_points)]
    k = 3

    centers, clusters = k_means(points, k)

    print("最終的なクラスタ中心:")
    for center in centers:
        print(center)

    print("\nクラスタ割り当て:")
    for idx, cluster_points in clusters.items():
        print(f"クラスタ {idx}: {cluster_points}")