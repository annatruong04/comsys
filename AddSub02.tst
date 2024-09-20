// Sample Test file for AddSub.asm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load AddSub.asm,
output-file AddSub02.out,
compare-to AddSub02.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[3]%D2.6.2;

set PC 0,
set RAM[0] -59,  // Set R0
set RAM[1] 49,  // Set R1
set RAM[2] 53,  // Set R2
set RAM[3] 161;  // Set R3
repeat 100 {
  ticktock;    // Run for 100 clock cycles
}
set RAM[1] 49,  // Restore arguments in case program used them
set RAM[2] 53, 
set RAM[3] 161,
output;        // Output to file

