.class public Count 
.super java/lang/Object

.method public <init>()V
		aload_0       
		invokespecial java/lang/Object/<init>()V
		return   
.end method    

.method public static main([Ljava/lang/String;)V
    .limit stack 2
    .limit locals 2
	iconst_1   
	istore_1   
	Loop:       
		iload_1       
		iconst_5      
       		if_icmpgt End
      		getstatic java/lang/System.out Ljava/io/PrintStream;
      		iload_1       
      		invokevirtual java/io/PrintStream.println(I)V
      		iinc 1 1
      		goto Loop
	End:
		return        
.end method
