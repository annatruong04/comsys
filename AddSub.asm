// Calculates R1 + R2 - R3 and stores the result in R0.
// (R0, R1, R2, R3 refer to RAM[0], RAM[1], RAM[2], and RAM[3], respectively.)

// Put your code here.
@1
D = M //D = RAM[1]

@2 
D = D + M  //D = RAM[1] + RAM[2]

@3 
D = D - M //D = RAM[1] + RAM[2] - RAM[3]

@0 
M = D

