/*********************************************
 * OPL 12.10.0.0 Model
 * Author: anast
 * Creation Date: Apr 10, 2023 at 5:28:12 PM
 *********************************************/
int nTasks=...;
int nCPUs=...;
int nCores=...;
int nThreads=...;
range T=1..nTasks;
range C=1..nCPUs;
range H=1..nThreads;
range K=1..nCores;
float rh[h in H]=...;
float rc[c in C]=...;
int CK[c in C, k in K]=...;
int TH[t in T, h in H]=...;
dvar boolean x_hk[h in H, k in K];
dvar boolean x_tc[t in T, c in C];
dvar float+ z;

//Pre-processing

// Objective function
minimize z;

// Constraints
subject to {
  
// Constraint 2: 
forall(h in H)
	sum(k in K) x_hk[h,k] == 1;

// Constraint 3: 
forall(t in T, c in C)
	sum(h in H) sum (k in K ) x_hk == abs(H[t])*x_tc;

//Constraint 4:	 
forall(c in C, k in K)
  sum(h in H) r_h *x_hk <= r_c;	  
	
// Constraint 5:
forall(c in C)
	z >= (1/(abs(K)*rc[c]))*sum(h in H) sum(k in K) rh[h]* x_hk[h,k];
	
}

//Post-processing