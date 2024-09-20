// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Sum = 0 
// n = R1 

// (Check n)
//     if n < 0 go to SWAP 

// (Loop)
//     if n = 0 go to STOP 
//     sum = sum + R2 
//     --n
//     go to Loop 

// (Swap) 
//     n = -n
//     go to Loop

// (STOP)
//     if R1 < 0 sum = -sum
//     R0 = sum 


@sum 
M = 0 
@R1
D = M 
@n 
M = D 
@Swap
D; JLT

(Loop)
    @n 
    D = M 
    @Stop  
    D; JEQ
    @R2 
    D = M 
    @sum 
    M = D+M
    @n 
    M = M - 1
    @Loop
    0;JMP


(Swap)
    @n
    M = -M 
    @Loop
    0; JMP

(Stop)
    @R1 
    D = M 
    @Swap_sum
    D, JLT
    @sum 
    D = M 
    @R0
    M = D 
    @End 
    0; JMP 

(Swap_sum)
    @sum 
    M = -M 
    @sum 
    D = M 
    @R0
    M = D 
    @End 
    0; JMP 

(End)
    @End
    0; JMP