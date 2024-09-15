// Calculates the absolute value of R1 and stores the result in R0.
// (R0, R1 refer to RAM[0], and RAM[1], respectively.)

// Put your code here.


@1 
D = M 

@Assign 
D; JLT

@0
M = D

(END)
0; JMP

(Assign)
D = -D

@0
M = D

@END
0; JMP
