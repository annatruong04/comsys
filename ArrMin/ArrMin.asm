// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R1 
A = M 
D = M 

@R0 
M = D

@R1 
D = M -1 

@R2 
M = D + M 

(Loop)
    @R1 
    D = M
    M = D+1 

    @R2 
    D = M 

    @R1 
    D = D-M 

    @end 
    D; JLT 

    @R0 
    D = M
    
    @Edge_case
    D; JLT

    @Check_swap
    0; JMP

(Check_swap)
    @R1 
    A = M 
    D = M 

    @R0 
    D = D - M 

    @Swap 
    D; JLT

    @Loop
    0; JMP



(Swap) // Swap R0 = RAM[RAM[R1]]
    @R1 
    A = M 
    D = M 

    @R0 
    M = D 

    @Loop
    0; JMP


(end)
    @end 
    0; JMP

(Edge_case)
    @R1 
    A = M 
    D = M 

    @Check_swap
    D, JLT

    @Loop
    D; JGT


