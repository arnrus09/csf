import java.util.*;
import java.util.concurrent.*;
import java.lang.reflect.*;
import java.io.*;

public class Efficiency2 {
	public static void main(String[] args){
		try{
		System.setOut(new PrintStream( new File("efficiency_out.txt") ) );
		}
		catch(Exception e){
			;
		}
		Integer[] prfArray = new Integer[10000];
		Arrays.fill(prfArray, new Integer(1) );
		List colls = Arrays.asList(new Collection[]{
		Arrays.asList(prfArray),
		new ArrayList<Integer>(Arrays.asList(prfArray)),
		new LinkedList<Integer>(Arrays.asList(prfArray)),
		new HashSet<Integer>(Arrays.asList(prfArray)),
		new LinkedHashSet<Integer>(Arrays.asList(prfArray)),
		new TreeSet<Integer>(Arrays.asList(prfArray)),
		new LinkedBlockingQueue<Integer>(Arrays.asList(prfArray)),
		new LinkedBlockingDeque<Integer>(Arrays.asList(prfArray)),
		new PriorityBlockingQueue<Integer>(Arrays.asList(prfArray)),
		new PriorityQueue<Integer>(Arrays.asList(prfArray)),
		});
		try{
		colTrial(colls);
		}
		catch(Exception e){
			System.out.println("test");
		}
	}
	
	static void colTrial(List<Collection<Integer>> colls) throws NoSuchMethodException, IllegalArgumentException, IllegalAccessException, InvocationTargetException
	{
		Method[] ms = Collection.class.getMethods();
		for( Method m : ms ){
			String methodName = m.getName().toUpperCase();
			boolean printed = false;
			Class[] argTypes = m.getParameterTypes();
			Object[] args = new Object[argTypes.length];
			boolean arrayAsList = true; //flag to specify ArrayList backed by primitive Array
			for( Collection col: colls ){
				String name = col.getClass().getSimpleName();
				for( int i = 0; i < argTypes.length; i++ ){
					if( argTypes[i].equals(Collection.class) ){
						List<Integer> cltn = new ArrayList<Integer>();
						Collections.fill(cltn, new Integer(2));
						args[i] = cltn;
					}
					else if(argTypes[i].toString().equals("class [Ljava.lang.Object;") )
						args[i] = new Object[0];
						else{
						try{
						Object o = argTypes[i].newInstance();
						args[i] = o;
						}
					catch(InstantiationException e){
						System.out.println( e.toString() );
					}
						}
				}
				try{
					long start = System.nanoTime();
						
					m.invoke(col, args);
					long end = System.nanoTime();
					if( !printed ){
						System.out.println(methodName + "\n--------");
						printed = true;
					}
					if( arrayAsList )
						System.out.println( "Array as List" );
					else
						System.out.println( name );
					System.out.println("\t" + m.getName() + ": " + (end - start) + "\n");
						}
				catch(Exception e){}
				finally{
					arrayAsList = false;
				}
				}
		}
		
}
}

