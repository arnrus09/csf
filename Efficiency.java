package performance;
import java.util.*;
import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.PriorityBlockingQueue;
import java.lang.reflect.*;
import java.io.*;

public class Efficiency {
	public static void main(String[] args) throws FileNotFoundException{
		System.setOut(new PrintStream(new File("/Users/russellarnold/efficiency_out.txt")));
		String[] prfArray = new String[1000000];
		Arrays.fill(prfArray, "hello");
		List<Collection> colls = Arrays.asList(new Collection[]{
		Arrays.asList(prfArray),
		new ArrayList<String>(Arrays.asList(prfArray)),
		new LinkedList<String>(Arrays.asList(prfArray)),
		new HashSet<String>(Arrays.asList(prfArray)),
		new LinkedHashSet<String>(Arrays.asList(prfArray)),
		new TreeSet<String>(Arrays.asList(prfArray)),
		new LinkedBlockingQueue<String>(Arrays.asList(prfArray)),
		new LinkedBlockingDeque<String>(Arrays.asList(prfArray)),
		new PriorityBlockingQueue<String>(Arrays.asList(prfArray)),
		new PriorityQueue<String>(Arrays.asList(prfArray)),
		});
		perfTest(colls, "contains");
		perfTest(colls, "equals");
		perfTest(colls, "remove");
		System.out.println( "\t\t\t" + "ITERATION:" );
		int x;
		for(Collection<String> coll : colls){
			String name = coll.getClass().getSimpleName();
			long start = System.nanoTime();
			for( String e : coll)
				x = 0;
			long end = System.nanoTime();
			System.out.println(name + ":\n\t" + (end - start) );
		}
		}
	static void perfTest(List<Collection> colls, String method){
		System.out.println( "\t\t\t" + method.toUpperCase() + ":" );
		for( Collection coll : colls)
			try{
			colTrial(coll, method);
			}
			catch(Exception e){
				System.out.println(coll.getClass().getSimpleName() + " does not support " + method + "\n");
			}
	}
	void getTrial(int[] arr){
		Object x;
		System.out.println(System.nanoTime());
		for( int i = 0; i < arr.length; i++ ){
			x = arr[i];
		}
		System.out.println(System.nanoTime());
	}
	static void colTrial(Collection<String> col, String method) throws NoSuchMethodException, IllegalArgumentException, IllegalAccessException, InvocationTargetException{
		String name = col.getClass().getSimpleName();
		Method m = Collection.class.getMethod(method, Object.class );
		long start = System.nanoTime();
		for( Object obj: col ){
			m.invoke(col, obj);
		}
		long end = System.nanoTime();
		System.out.println(name + ":\n\t" + (end - start) );
}
}
