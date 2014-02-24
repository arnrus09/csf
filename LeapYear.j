.class public LeapYear
.super java/lang/Object

.method public <init>()V
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
.end method

.method public static main([Ljava/lang/String;)V
     .limit stack 5
     .limit locals 2
	aload_0       
	arraylength   
	iconst_2      
	if_icmpeq  Else
		getstatic java/lang/System.out Ljava/io/PrintStream;
		ldc  "usage:\njava LeapYear BirthYear currentYear"
		invokevirtual java/io/PrintStream.println(Ljava/lang/String;)V
		goto End
	Else:
		getstatic java/lang/System.out Ljava/io/PrintStream;
		aload_0       
		iconst_1     		;get current year from args
		aaload        
		invokestatic java/lang/Integer.parseInt(Ljava/lang/String;)I
		aload_0       
		iconst_0     		;get birth year 
		aaload        
		invokestatic java/lang/Integer.parseInt(Ljava/lang/String;)I
		isub          		;age
		iconst_4      		
		idiv          
		invokevirtual java/io/PrintStream.println(I)V
     	End: 
		return        
.end method
