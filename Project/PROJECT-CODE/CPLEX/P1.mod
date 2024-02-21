/*********************************************
 * OPL 22.1.1.0 Model
 * Author: nikol
 * Creation Date: 13 ��� 2023 at 4:23:58 �.�.
 *********************************************/
// Number of measurements.
int n=...;

// Range of measurements.
range N=1..n;

dvar int x_t[n in N];
dvar int x_d[n_i in N, n_j in N];

// Pre-processing
execute {

};

// Objective function
minimize x_t[n];

// Constraints
subject to {
  
// Constrain 1: Calculate all the differences in the array
forall(i,j in 1..n: i<j)
  x_d[i,j] == abs(x_t[j] - x_t[i]);
  
// Constraint 2: Each element should be greater than the previous
forall(i,j in 1..n: i<j)
  (x_t[j] - x_t[i]) >= 1;
  
// Constraint 3: The first element should be 0
x_t[1]==0;

x_t[n] <= 2^n;

// Constraint 4: No two differences should be the same
forall(i,j,u,v in 1..n: i<j && u<v && i!=u && j!=v)
  x_d[i,j] != x_d[u,v];
}

//Post-processing
execute {
  writeln(x_t[n]);
  for (var i=1; i<=n; i++)
  	write(x_t[i] + " ")
}



 