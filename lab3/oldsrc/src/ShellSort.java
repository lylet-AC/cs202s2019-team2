// this algorithm runs O(n^2)
public class ShellSort{
	public static void printArray(int[] arr){
		// print sorted array
		for (int i: arr)
			System.out.print(i + " ");
		System.out.print("\n");
	}
	public static void main(String[] args){
		int[] unsorted = new int[]{14,18,19,37,23,40,29,30,11};
		//int[] unsorted = new int[]{15,19,20,38,24,41,30,31,12};
		int gap = (int) unsorted.length/2;
		while(gap > 0){
			for (int i = gap; i < unsorted.length; i++){
				int temp = unsorted[i];
				int j = i;
				while(j >= gap && unsorted[j-gap] > temp){
					unsorted[j]= unsorted[j-gap];
					j = j - gap;
					System.out.println("i is: " + i 
										+ " j is: " + j);
				}
				unsorted[j] = temp;
			}
			System.out.println("gap value is: " + gap);
			printArray(unsorted);
			System.out.println("---------------------------");

			gap = (int) gap/2;

			
				
		}
		

		// print sorted array
		printArray(unsorted);

	}
}

