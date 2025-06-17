from point import Point

def compute_centroid(points):
    dims = len(points[0].coordinates)
    centroid_coords = [
        sum(pt.coordinates[i] for pt in points) / len(points)
        for i in range(dims)
    ]
    return Point(centroid_coords)

def k_means(points, k, max_iterations=100, tolerance=1e-4):
    dims = len(points[0].coordinates)
    # k個のクラスタ中身をランダムに初期化
    centers = [Point.random(dims) for _ in range(k)]

    for iteration in range(max_iterations):
        clusters = {i: [] for i in range(k)}
        # 各データ点を最も近い中心に割り当て
        for pt in points:
            distances = [pt.distance(center) for center in centers]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(pt)

        new_centers = []
        # 各クラスタの重心を再計算
        for i in range(k):
            if clusters[i]:
                new_centers.append(compute_centroid(clusters[i]))
            else:
                new_centers.append(centers[i])

        # 中心の変化が閾値以下なら終了
        if all(new_centers[i].distance(centers[i]) < tolerance for i in range(k)):
            centers = new_centers
            break

        centers = new_centers

    return centers, clusters