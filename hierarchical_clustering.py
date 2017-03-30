class hierarchical_clustering():

    def __init__(self, distances, size_constraint, batch_assign = True, existing_clustering = None):
        self.distances = distances
        ensure_distances(distances)
        self.num_data_points = len(distances)
        self.size_constraint = coerce_size_constraint(size_constraint, num_data_points)
        self.batch_assign = coerce_scalar_indicator(batch_assign)
        self.existing_clustering = existing_clustering
      	if ((existing_clustering)!= None) {
   			ensure_scclust(existing_clustering, num_data_points)
   			}
   	def clustering(self):

   	def make_scclust(self):
