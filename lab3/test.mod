/*********************************************
 * OPL 12.10.0.0 Model
 * Author: anast
 * Creation Date: Apr 10, 2023 at 8:20:02 PM
 *********************************************/
int nTasks=...;
int nThreads=...;
int nCPUs=...;
int nCores=...;
range T=1..nTasks;
range H=1..nThreads;
range C=1..nCPUs;
range K=1..nCores;
// Data: Tasks, Computers 
float rh[h in H]=...;
float rc[c in C]=...;
// Data: Cores of Computer, Threads of Task
float CK[c in C, k in K]=...;
float TH[t in T, h in H]=...;
int H_t[T]; // number of threads for each task
int K_c[C]; // number of cores for each CPU
// Variables: Task in Computer, Thread in Core
dvar boolean x_tc[t in T, c in C];
dvar boolean x_hk[h in H, k in K];
dvar float+ z;
execute {
for (var t=1; t<nTasks; t++)
		//totalLoad += rh[h];
		for (var h=1; h<nThreads; h++)
			H_t[t] += TH[t][h];
		writeln(H_t[t]); 
}