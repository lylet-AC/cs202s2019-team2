// this algorithm runs O(n^2)
public class SelectionSort{
	public static void printArray(int[] arr){
		// print sorted array
		for (int i: arr)
			System.out.print(i + " ");
		System.out.print("\n");
	}
	public static void main(String[] args){
		int[] unsorted = new int[]{5,6,9,0,8,2,7,1,3};
		for (int i = 0; i < unsorted.length - 1; i++){
			int min = i;
			for (int j = i + 1; j < unsorted.length; j++){
				if (unsorted[j] < unsorted[min])
					min = j;
			}
			if (min != i){
				int temp = unsorted[i];
				unsorted[i] = unsorted[min];
				unsorted[min] = temp;
			}
			System.out.println("i value is: " + i);
			printArray(unsorted);
			System.out.println("---------------------------");

		}
		//printArray(unsorted);
	}
}