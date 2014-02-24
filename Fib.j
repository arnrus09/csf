.class public Fib
.super java/lang/Object

.method public <init>()V
		aload_0       
		invokespecial java/lang/Object/<init>()V
		return   
.end method     

.method public static main([Ljava/lang/String;)V
    	.limit stack 7
	.limit locals 4     
		bipush 10
		istore_2 		;#2 is number of iterations = 10
		iload_2
		newarray int
		astore_3      		;#3 is the address of the array
		aload_3       
		iconst_0      
		iconst_1       
		iastore       
		aload_3       
		iconst_1      
		iconst_1       
		iastore       
		iconst_2      
		istore_1 		;#1 is loop counter i
	Loop: 
		iload_1
		iload_2
		if_icmpge Exit
		aload_3       
		iload 1
		aload_3       
		iload_1
		iconst_1      
		isub          
		iaload        
		aload_3       
		iload 1
		iconst_2      
		isub          
		iaload        
		iadd          
		iastore       
		iinc 1 1
		goto Loop
	Exit: 
		getstatic java/lang/System.out Ljava/io/PrintStream;
		aload_3       
		invokestatic java/util/Arrays.toString([I)Ljava/lang/String;
		invokevirtual java/io/PrintStream.println(Ljava/lang/String;)V
		return        
.end method

