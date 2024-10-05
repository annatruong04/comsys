global label
label=0
class VMTranslator:
    def vm_push(segment, offset):
        '''Generate Hack Assembly code for a VM push operation'''
        special_segments = {
            "local": "LCL",
            "this": "THIS",
            "that": "THAT",
            "argument": "ARG"
        }
        def get_segment(segment,offset):
            if segment == "pointer":
                return "R" + str(offset+3)
            elif segment == "constant":
                return str(offset)
            elif segment == "static":
                return str(offset+16)
            elif segment == "temp":
                return "R" + str(offset+5)
            else:
                raise ValueError("Not a valid segment")
        translated_str = ""
        # offset = str(offset)
        if segment in special_segments.keys():
            translated_str = f"@{special_segments[segment]}\nD=M\n@{offset}\nD=D+A\nA=D\nD=M\n"
        elif segment == "pointer" or segment == "static" or segment == "temp":
            segment_str = get_segment(segment,offset)
            translated_str = f"@{segment_str}\n"
            translated_str += "D=M\n"
        elif segment == "constant":
            segment_str = get_segment(segment,offset)
            translated_str = f"@{segment_str}\n"
            translated_str += "D=A\n"
        else:
            raise ValueError("Not a valid segment")
        translated_str+=f"@SP\nA=M\nM=D\n@SP\nM=M+1"
        return translated_str


    def vm_pop(segment, offset):
        '''Generate Hack Assembly code for a VM pop operation'''
        special_segments = {
            "local": "LCL",
            "this": "THIS",
            "that": "THAT",
            "argument": "ARG"
        }
        def get_segment(segment,offset):
            if segment == "pointer":
                return "R" + str(offset+3)
            elif segment == "constant":
                return str(offset)
            elif segment == "static":
                return str(offset+16)
            elif segment == "temp":
                return "R" + str(offset+5)
            else:
                raise ValueError("Not a valid segment")
        translated_str="@SP\nM=M-1\n"
        if segment in special_segments.keys():
            translated_str += f"@{special_segments[segment]}\nD=M\n@{offset}\nD=D+A\n"
        elif segment == "pointer" or segment == "static" or segment == "temp":
            segment_str = get_segment(segment,offset)
            translated_str += f"@{segment_str}\nD=A\n"
        else:
            raise ValueError("Not a valid segment")
        translated_str+=f"@R13\nM=D\n@SP\nA=M\nD=M\nD=M\n@R13\nA=M\nM=D"
        return translated_str

    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=D+M"

    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M-D"

    def vm_neg():
        '''Generate Hack Assembly code for a VM neg operation'''
        return "@SP\nA=M-1\nM=!M\nM=M+1"

    def vm_eq():
        '''Generate Hack Assembly code for a VM eq operation'''
        global label
        label+=1
        return f"@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@EQTRUE{label}\nD;JEQ\n@SP\nA=M-1\nM=0\n@EQFALSE{label}\n0;JMP\n(EQTRUE{label})\n@SP\nA=M-1\nM=-1\n(EQFALSE{label})"

    def vm_gt():
        '''Generate Hack Assembly code for a VM gt operation'''
        global label
        label+=1
        return f"@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@GTTRUE{label}\nD;JGT\n@SP\nA=M-1\nM=0\n@GTFALSE{label}\n0;JMP\n(GTTRUE{label})\n@SP\nA=M-1\nM=-1\n(GTFALSE{label})"

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        global label
        label+=1
        return f"@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@GTTRUE{label}\nD;JLT\n@SP\nA=M-1\nM=0\n@GTFALSE{label}\n0;JMP\n(GTTRUE{label})\n@SP\nA=M-1\nM=-1\n(GTFALSE{label})"

    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M&D"

    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M|D"

    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        return "@SP\nAM=M-1\nM=!M\n@SP\nM=M+1"

    def vm_label(label):
        '''Generate Hack Assembly code for a VM label operation'''
        label_str = f"({label})"
        return label_str

    def vm_goto(label):
        '''Generate Hack Assembly code for a VM goto operation'''
        label_str = f"@{label}\n"
        return label_str+"0;JMP"

    def vm_if(label):
        '''Generate Hack Assembly code for a VM if-goto operation'''
        return f"@SP\nAM=M-1\nD=M\n@{label}\nD;JNE"

    def vm_function(function_name, n_vars):
        '''Generate Hack Assembly code for a VM function operation'''
        translated_str=""
        translated_str+=f"(VMTRANSLATOR.{function_name})"
        for i in range(n_vars):
            translated_str+="\n@SP\nA=M\nM=0\n"
            translated_str+="@SP\nM=M+1"
        return translated_str


    def vm_call(function_name, n_args):
        '''Generate Hack Assembly code for a VM call operation'''
        translated_str="@SP\nD=M\n@R13\nM=D\n"
        #SAVE RETURN ADDRESS
        translated_str+=f"@VMTRANSLATOR_RET.{function_name}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        #SAVE FRAME 
        translated_str+="@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        translated_str+="@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        translated_str+=f"@R13\nD=M\n@{n_args}\nD=D-A\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n"
        translated_str+=f"@VMTRANSLATOR.{function_name}\n0;JMP\n(VMTRANSLATOR_RET.{function_name})"
        return translated_str

    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        #FIND RETURN VALUE POINTER AND FRAME POINTER
        translated_str = "@LCL\nD=M\n@13\nM=D\n\n@5\nA=D-A\nD=M\n@14\nM=D\n"
        #SAVE RETURN VALUE TO FIRST ARG VALUE
        translated_str += "@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\n"
        #RESTORE CALLERS SP
        translated_str += "@ARG\nD=M+1\n@SP\nM=D\n"
        #RESTORE SEGMENT VARIABLES
        translated_str += "\n@13\nAM=M-1\nD=M\n@THAT\nM=D\n@13\nAM=M-1\nD=M\n@THIS\nM=D\n@13\nAM=M-1\nD=M\n@ARG\nM=D\n@13\nAM=M-1\nD=M\n@LCL\nM=D"
        #JUMP TO RESULT
        translated_str += "\n@14\nA=M\n0;JMP"
        return translated_str

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

# output = VMTranslator.vm_call("hello",2)
# print(output)