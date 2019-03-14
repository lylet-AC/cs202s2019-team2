import java.util.*;

// this algorithm runs O(nlogn) in worst case
public class QuickSort{
	private static int[] unsorted = new int[]{6,9,8,4,7,1,3,2,0,5};
	public static void printPartition(int[] arr, int x,
        int partitionIndex, int y){
        // print partition array

        System.out.print("\t");
        for (int i = x; i < partitionIndex; i++)
            System.out.print(arr[i] + " ");
        System.out.print("|" + arr[partitionIndex] + "| ");
        for (int i = partitionIndex+1; i <= y; i++)
            System.out.print(arr[i] + " ");
        System.out.print("\n");



    }

    public static void printArray(int[] arr){
		// print sorted array
		for (int i: arr)
			System.out.print(i + " ");
		System.out.print("\n");
	}
	public static int partitionArray(int[] a, int x, int y){
		int pivot = a[y];
		int i = x -1;
		for (int j = x; j <= y-1; j++){
			if (a[j] <= pivot){
				i = i + 1;
				// exchange a[i] with a[j]
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;


			}
		}

        // exchange a[i+1] with a[y]
		int temp = a[i+1];
		a[i+1] = a[y];
		a[y] = temp;
        printPartition(a, x, i+1, y);
        return i+1;

	}

	private static int randomGen(int lower, int higher) {
		if (lower>= higher) {
			throw new IllegalArgumentException("Higher must be greater");
		}

		Random r = new Random();
		return r.nextInt((higher - lower + 1) + lower );
	}

	public static int randomizedPartition(int[] a, int x, int y){

		int i = randomGen(x, y);
		int temp = a[i];
		a[i] = a[y];
		a[y] = temp;

		return partitionArray(a, x, y);
	}

	public static void randomQuickSort(int[] a, int x, int y){
		if (x < y){
			int partitionIndex = randomizedPartition(a, x, y);
			randomQuickSort(a, x, partitionIndex-1);
			randomQuickSort(a, partitionIndex+1, y);
		}
	}

	public static void quickSort(int[] a, int x, int y){
		if (x < y){
			int partitionIndex = partitionArray(a, x, y);
			quickSort(a, x, partitionIndex-1);
			quickSort(a, partitionIndex+1, y);
		}



	}
	public static void main(String[] args){

		//int[] unsorted = new int[]{15,19,20,38,24,41,30,31,12};
		/*printArray(unsorted);
        quickSort(unsorted, 0, unsorted.length - 1);
		printArray(unsorted);*/

		printArray(unsorted);
			randomQuickSort(unsorted, 0, unsorted.length - 1);
		printArray(unsorted);



	}
}
