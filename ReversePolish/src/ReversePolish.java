import java.util.*;

class ReversePolish{
  static Stack<Integer> myStack = new Stack<Integer>();
      
  public static boolean isDigit(String str){  
    try{  
      int n = Integer.parseInt(str);  
    }
    catch(NumberFormatException nfe){  
      return false;  
    }  
    return true;  
  }
    
  public static void main(String... args){
    for(String arg:args){
      if(isDigit(arg)){
        int n = Integer.parseInt(arg);
        myStack.push(n);
      }
      else{
    int op2 = myStack.pop();
    int op1 = myStack.pop();
    if (arg.equals("+")){
      myStack.push(op1+op2);
    }
    else if (arg.equals("*")){
      myStack.push(op1*op2);
    }
    else if (arg.equals("-")){
      myStack.push(op1-op2);
    }
    else if (arg.equals("/")){
      myStack.push(op1/op2);
    }       
        
    }
  }
  System.out.println(myStack.peek());
}
}
    
    
    
