import math

Vector = list[float]

def sum(v: Vector, w: Vector) -> Vector:
    """Soma de vetores: v + w = (v_1 + w_1, ..., v_n + w_n)."""
    if len(v) != len(w):
        raise ValueError(f"vectors with different lengths: {len(v)} and {len(w)}")
    return [v_i + w_i for v_i, w_i in zip(v, w, strict=True)]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtração de vetores: v - w = (v_1 - w_1, ..., v_n - w_n)."""
    if len(v) != len(w):
        raise ValueError(f"vectors with different lengths: {len(v)} and {len(w)}")
    return [v_i - w_i for v_i, w_i in zip(v, w, strict=True)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplicação por escalar: c * v = (c * v_1, ..., c * v_n)."""
    return [c * v_i for v_i in v]

def sum_vectors(vectors: list[Vector]) -> Vector:
    """Soma de uma lista de vetores."""
    if not vectors:
        raise ValueError("empty list of vectors")
    n = len(vectors[0])
    if n == 0:
        raise ValueError("vectors with zero length")
    if any(len(v) != n for v in vectors):
        raise ValueError("vectors with different lengths")
    return [sum(v_i for v in vectors) for v_i in zip(*vectors, strict=True)]

def dot(v: Vector, w: Vector) -> float:
    """Produto escalar: v · w = Σ v_i w_i."""
    if len(v) != len(w):
        raise ValueError(f"vectors with different lengths: {len(v)} and {len(w)}")
    return sum(v_i * w_i for v_i, w_i in zip(v, w, strict=True))


def magnitude(v: Vector) -> float:
    """Norma euclidiana: ||v|| = sqrt(v · v)."""
    return math.sqrt(dot(v, v))

def distance(v: Vector, w: Vector) -> float:
    """Distância euclidiana: d(v, w) = ||v - w||."""
    if len(v) != len(w):
            raise ValueError(f"vectors with different lengths: {len(v)} and {len(w)}")
    return magnitude(subtract(v, w))