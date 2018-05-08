/* -*- mode: C -*-  */
/* vim:set ts=2 sts=2 sw=2 et: */
/* 
   IGraph library.
   Copyright (C) 2006-2012  Gabor Csardi <csardi.gabor@gmail.com>
   334 Harvard street, Cambridge, MA 02139 USA
   
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc.,  51 Franklin Street, Fifth Floor, Boston, MA 
   02110-1301 USA

*/

#include <igraph.h>
#include <sys/time.h>

// void show_results(igraph_t *g, igraph_vector_t *membership, igraph_matrix_t *memberships, igraph_vector_t *modularity, FILE* f) {
//   long int i, j, no_of_nodes = igraph_vcount(g);

//   j=igraph_vector_which_max(modularity);
//   for (i=0; i<igraph_vector_size(membership); i++) {
//     if (VECTOR(*membership)[i] != MATRIX(*memberships, j, i)) {
//       fprintf(f, "WARNING: best membership vector element %li does not match the best one in the membership matrix\n", i);
//     }
//   }

//   fprintf(f, "Modularities:\n");
//   igraph_vector_print(modularity);

//   for (i=0; i < igraph_matrix_nrow(memberships); i++) {
//     for (j=0; j < no_of_nodes; j++) {
//       fprintf(f, "%ld ", (long int)MATRIX(*memberships, i, j));
//     }
//     fprintf(f, "\n");
//   }

//   fprintf(f, "\n");
// }

// void read_graph(){
//   FILE *F = fopen("as20graph.txt", "r");     // file for output
//   igraph_t graph;
//   igraph_bool_t directed = false;
//   igraph_read_graph_edgelist(&graph, F, 0, directed);
// }

int main(int argc, char* argv[]) {
  const char* filename = "as20graph.txt";
  const char* outputFile = "out.txt";
  if (argc >= 2){
    filename = argv[1];
    printf("filename: %s \n", filename);
  }
  if (argc >= 3){
    outputFile = argv[2];
    printf("outputFile: %s \n", outputFile);
  }

  
  // igraph_t g;
  igraph_vector_t modularity, membership, edges;
  igraph_matrix_t memberships;
  int i, j, k;

  igraph_vector_init(&modularity,0);
  igraph_vector_init(&membership,0);
  igraph_matrix_init(&memberships,0,0);

  // Read graph
  FILE *F = fopen(filename, "r");     // file for output
  igraph_t graph;
  igraph_bool_t directed = false;

  printf("Loading %s... \n", filename);
  igraph_read_graph_edgelist(&graph, F, 0, directed);

  struct timeval t1, t2;
  double elapsedTime; 

  gettimeofday(&t1, NULL);

  igraph_community_multilevel(&graph, 0, &membership, &memberships, &modularity);

  gettimeofday(&t2, NULL);
  
  
  elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
  elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;   // us to ms
  elapsedTime = elapsedTime/1000.0; // back to seconds

  printf("elapsed time: %f sec.\n", elapsedTime);

  // show_results(&graph, &membership, &memberships, &modularity, stdout);
  igraph_destroy(&graph);

  // Deallocate 
  igraph_vector_destroy(&modularity);
  igraph_vector_destroy(&membership);
  // igraph_vector_destroy(&edges);
  igraph_matrix_destroy(&memberships);

#ifdef __APPLE__
  return 0;
#else
  return 77;
#endif
}