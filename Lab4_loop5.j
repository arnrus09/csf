.class public Lab4_loop5
      .super java/lang/Object

      .method public <init>()V
         aload_0
         invokespecial java/lang/Object/<init>()V
         return
      .end method

      .method public static main([Ljava/lang/String;)V
		.limit stack 4
		.limit locals 4
		iconst_0
		dup
		istore_1
		istore_2
		iconst_5
		istore_3
	Loop:
		iload_1
		iload_2
		iadd
		istore_2
		iinc 1 1
		iload_1
		iload_3
		if_icmplt Loop
		getstatic java/lang/System/out Ljava/io/PrintStream;
      	iload_2
      	invokevirtual java/io/PrintStream/println(I)V
        return
      .end method
