public class InterviewByjusDSQuestion {

    /*

    Given a sorted array with 2 places mis-matched in sorting, find the 2 elements and correct their places

    Input :   {21, 126, 42, 89,  36}
    Output : {21,  36,  42, 89, 126}

    Input :   {21, 42, 36, 89,  126}
    Output : {21,  36,  42, 89, 126}

    Input :   {3, 2, 1}
    Output : {1,  2, 3}

    */

    public static void main(String args[]) {
        int arr[] = {21, 42, 36, 89,  126};

        printArray(arr);
        sortArray(arr);
        printArray(arr);
    }

    public static void printArray(int[] intArray) {
        for (int i = 0; i < intArray.length; i++) {
            System.out.print(intArray[i] + " ");
        }

        System.out.println("");
    }

    public static void sortArray(int[] inputArray) {

        int place1ToSwap = -1;
        int place2ToSwap = -1;

        for (int i = 0; i < inputArray.length; i++) {

            if ((i != inputArray.length - 1) && inputArray[i] > inputArray[i + 1] && place1ToSwap < 0) {
                place1ToSwap = i;
            }

            if ((i > 0) && inputArray[i] < inputArray[i - 1]) {
                place2ToSwap = i;
            }
        }

        int temp = inputArray[place1ToSwap];
        inputArray[place1ToSwap] = inputArray[place2ToSwap];
        inputArray[place2ToSwap] = temp;
    }
}
