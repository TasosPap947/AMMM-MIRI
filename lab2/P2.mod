/*********************************************
 * OPL 22.1.1.0 Model
 * Author: nikol
 * Creation Date: 13 ��� 2023 at 4:23:58 �.�.
 *********************************************/
int nTasks=...;
int nCPUs=...;
range T=1..nTasks;
range C=1..nCPUs;
float rt[t in T]=...;
float rc[c in C]=...;
dvar boolean x_tc[t in T, c in C];
dvar float+ z;

// Pre-processing
execute {
	var totalLoad=0;
	var totalCapacity=0;
	
	for (var t=1;t<=nTasks;t++)
		totalLoad += rt[t];
	for (var c=1;c<=nCPUs;c++)
  		totalCapacity += rc[c];
  			
	
	writeln("Total load "+ totalLoad);
	writeln("Total capacity "+ totalCapacity);
	
	if (totalLoad > totalCapacity) {
  	  writeln("Computers do not have enough capacity");
  	}
  	else {
  	  writeln("Computers have enough capacity");
  	}
};

// Objective function
minimize z;

// Constraints
subject to {
  
// Constraint 1: Total load of one task should add up to 1 (meaning it can be assigned to 1 computer)
forall(t in T)
	sum(c in C) x_tc[t,c] == 1;

// Constraint 2 : Total load in one computer should not exceed its capacity
forall(c in C)
	sum(t in T) rt[t]* x_tc[t,c] <= rc[c];
	
// Constraint 3 : Total load of all computers should not exceed the one with the biggest load
forall(c in C)
	z >= (1/rc[c])*sum(t in T) rt[t]* x_tc[t,c];
	
}

//Post-processing
execute {
	for (var c=1;c<=nCPUs;c++) {
		var load=0;
		for (var t=1;t<=nTasks;t++)
			load+=(rt[t]* x_tc[t][c]);
		load = (1/rc[c])*load;
		writeln("CPU " + c + " loaded at " + 100*load + "%");
	}
};



 