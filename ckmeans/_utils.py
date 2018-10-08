from collections import namedtuple

KmeansResult = namedtuple(
    'ClusterResult',
    ['clustering', 'k', 'centers', 'sizes', 'within_ss', 'total_ss', 'between_ss']
)

KmeansResult.__doc__ = "Cluster result container"
