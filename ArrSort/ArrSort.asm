// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// WE WILL DO SELECTION SORT HERE. 

// for (int i = 0; i < n; i++){
//     for (int j = i + 1; j < n; j++){
//         if (arr[i] > arr[j]) swap(arr[i], arr[j]);
//     }
// }

// Set R2 to the end index of the sorting loop. We will loop until R1 reach R2 and until j reach R2.

@R1 
D = M -1  

@R2 
M = D + M // Now R2 is the end index. 

@R1 
D = M + 1 

@j 
M = D // j starts at R1 + 1
A = M
D = M 


(first_loop)
    @R2 
    D = M 

    @R1 
    D = D - M 

    @end 
    D; JLT

    @second_loop
    0; JMP 

(second_loop)


    @j 
    A = M 
    D = M 

    @overflowa // Happens when j is less than 0. If R1 is greater than 0, automatically swap those 2 values. 
    D; JLT

    @R1 
    A = M 
    D = M

    @overflowb // Happens when R1 is now less than 0. If j is greater than 0 then go to continue 
    D; JLT 

    @j 
    A = M 
    D = M 

    @R1 
    A = M 
    D = D - M 

    @swap 
    D; JLT
    
    @continue
    0; JMP


(continue)
    @j 
    M = M + 1

    @R2 
    D = M 

    @j 
    D = D - M 

    @Increase_R1 // If j reaaches the R2, increase R1 and reassign j 
    D; JLT 

    @second_loop
    0; JMP


(end)
    @R0 
    M = -1

    @end 
    0; JMP 


(swap)
    // temp = arri x
    // arri = arrj 
    // arrj = temp 

    @R1 
    A = M 
    D = M 

    @temp 
    M = D   

    @j 
    A = M 
    D = M

    @R1 
    A = M 
    M = D // arri = arrj 

    @temp 
    D = M 

    @j
    A = M 
    M = D // arrj = temp 

    @second_loop
    0; JMP

(Increase_R1)
    @R1 
    MD = M + 1

    @j 
    M = D

    @first_loop
    0; JMP

(overflowa)
    @R1 
    A = M 
    D = M 

    @swap 
    D; JGT

(overflowb)
    @j
    A = M 
    D = M 

    @continue
    D; JGT

    @j 
    A = M 
    D = M 

    @R1 
    A = M 
    D = D - M 

    @swap 
    D; JLT
    
    @continue
    0; JMP
