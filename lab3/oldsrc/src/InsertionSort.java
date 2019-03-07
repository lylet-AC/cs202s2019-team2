// this algorithm runs O(n^2)
public class InsertionSort{
	public static void printArray(int[] arr){
		// print sorted array
		for (int i: arr)
			System.out.print(i + " ");
		System.out.print("\n");
	}
	public static void main(String[] args){
		int[] unsorted = new int[]{5,6,9,0,8,2,7,1,3};
		for (int i = 1; i < unsorted.length; i++){
			int key = unsorted[i];
			int j = i -1;
			while(j >= 0 && unsorted[j] > key){
				unsorted[j+1] = unsorted[j];
				j--;
			}
			unsorted[j+1] = key;
			System.out.println("i value is: " + i);
			printArray(unsorted);
			System.out.println("---------------------------");
		}

		// print sorted array
		//printArray(unsorted);

	}
}

