namespace DataStructures.Sorting
{
    public class MergeSort
    {
        public static void Sort(int[] input)
        {
            // Init.
            int left = 0;
            int right = input.Length - 1;

            // Apply Merge Sort.
            int mid = (left + right) / 2;
            Merge(input, left, mid, right);
        }

        private static void Merge(int[] input, int left, int middle, int right)
        {
            if (left == right)
            {
                return;
            }

            int m = (left + middle) / 2;
            Merge(input, left, m, middle + 1);
            Merge(input, middle, m, right);

            int i = left;
            int j = middle + 1;
            int k = left;

            int[] temp = new int[input.Length];

            while (i <= middle && j <= right)
            {
                if (input[i] <= input[j])
                {
                    temp[k] = input[i];
                    k++;
                    i++;
                }

                if (input[j] < input[i])
                {
                    temp[k] = input[j];
                    k++;
                    j++;
                }
            }

            while (i <= middle)
            {
                temp[k] = input[i];
                i++;
                k++;
            }

            while (j <= right)
            {
                temp[k] = input[j];
                j++;
                k++;
            }

            for (int index = left; index <= right; index++)
            {
                input[index] = temp[index];
            }
        }
    }
}




