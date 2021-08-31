namespace DataStructures.Arrays
{
    public enum RotateApproach
    {
        TempStorage,
        OneByOne,
        Juggle
    }

    public static class ArrayExtensions
    {
        public static void Print<T>(this T[] array)
        {
            System.Console.WriteLine("Printing Array : ");
            for (int i = 0; i < array.Length; i++)
            {
                System.Console.Write(string.Format("{0} ", array[i]));
            }
        }

        public static void Print(this object[] array)
        {
            System.Console.WriteLine("Printing Array : ");
            for (int i = 0; i < array.Length; i++)
            {
                System.Console.Write(string.Format("{0} ", array[i]));
            }
        }

        /// <summary>
        /// Rotates arr[] by n elements
        /// </summary>
        /// <param name="array">The input array.</param>
        /// <param name="n">The number of elements to rotate the array by.</param>
        /// <param name="approach">The algorithm used for rotation.</param>
        public static void RotateByN(this object[] array, int n, RotateApproach approach)
        {
            if (array == null || array.Length == 0)
            {
                System.Console.WriteLine("Input array is empty");
                return;
            }

            int length = array.Length;
            if (n > length)
            {
                System.Console.WriteLine("The value of 'n' should not be greater than the length of the array");
                return;
            }

            switch (approach)
            {
                case RotateApproach.TempStorage:
                    {
                        // store temp.
                        object[] temp = new object[n];
                        for (int i = 0; i < n; i++)
                        {
                            temp[i] = array[i];
                        }

                        // shift.
                        for (int i = 0; i < length - n; i++)
                        {
                            array[i] = array[i + n];
                        }

                        // replace.
                        for (int i = 0; i < n; i++)
                        {
                            array[length - n + i] = temp[i];
                        }
                    }
                    break;
                case RotateApproach.OneByOne:
                    break;
                case RotateApproach.Juggle:
                    break;
                default:
                    break;
            }
            Print(array);
        }
    }
}
