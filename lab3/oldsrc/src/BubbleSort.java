// this algorithm runs O(n^2)
public class BubbleSort{
	public static void printArray(int[] arr){
		// print sorted array
		for (int i: arr)
			System.out.print(i + " ");
		System.out.print("\n");
	}
	public static void main(String[] args){
		int[] unsorted = new int[]{5,6,9,0,8,2,7,1,3};
		boolean swapped = true;		
		int pass = 1;
		do{
			swapped = false;
			for (int i =0; i < unsorted.length - 1; i++){
				if (unsorted[i] > unsorted[i+1]){
					int temp = unsorted[i];
					unsorted[i] = unsorted[i+1];
					unsorted[i+1] = temp;
					swapped = true;
				}
			}
			System.out.println("pass value is: " + pass);
			printArray(unsorted);
			System.out.println("---------------------------");
			pass++;
		} while(swapped);
		//printArray(unsorted);
	}
}